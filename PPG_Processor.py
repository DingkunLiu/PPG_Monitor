import struct
import time

import numpy as np
from scipy import signal

from Serial_Port import dataCollector
from detect_peak import detect_peaks


class heart_Rate():
    def __init__(self, data, fs):
        self.fs = fs
        # initialize threshold
        buffer_max = []
        for part in range(5):
            buffer_max.append(np.max(data[(part * self.fs):((part + 1) * self.fs - 1)]))
        # print(buffer)
        self.SPK = np.mean(buffer_max)
        self.NPK = 0
        # initialize some variable
        self.RRA1 = np.array([])
        self.RRA2 = np.array([])

    def run(self, data):
        # running
        print(self.SPK)
        print(self.NPK)
        beat_index = []
        # find peak
        peaks = detect_peaks(data, mpd=round(0.2 * self.fs))
        for f_mark in peaks:
            T1 = 0.75 * self.NPK + 0.25 * self.SPK
            T2 = 0.5 * T1
            if data[f_mark] > T1:
                beat_index.append(f_mark)
                self.SPK = 0.075 * data[f_mark] + 0.925 * self.SPK
                find_peak = True
            else:
                self.NPK = 0.125 * data[f_mark] + 0.875 * self.NPK
                find_peak = False

            # update RR interval
            if len(beat_index) > 2 and find_peak:
                last_RR = beat_index[-1] - beat_index[-2]
                # search back
                if self.RRA2.shape[0] == 8 and last_RR > 1.66 * self.RRA2.mean():
                    # adjust threshold
                    self.SPK *= .7
                    self.NPK *= .7
                    # print('search back')
                    # find max
                    searback = data[int(beat_index[-2]):int(beat_index[-1])]
                    ind = detect_peaks(searback, threshold=T2)
                    if searback[ind] > T2:
                        # find missing R peak
                        r_temp = beat_index[-1]
                        beat_index[-1] = beat_index[-2] + ind
                        beat_index.append(r_temp)
                        self.SPK = 0.25 * searback[ind] + 0.75 * self.SPK
                        last_RR = beat_index[-1] - beat_index[-2]

                # update RRA1
                if self.RRA1.shape[0] < 8:
                    self.RRA1 = np.append(self.RRA1, last_RR)
                else:
                    self.RRA1[:-1] = self.RRA1[1:]
                    self.RRA1[-1] = last_RR
                if 0.92 * self.RRA1.mean() < last_RR < 1.16 * self.RRA1.mean():
                    # update RRA2
                    if self.RRA2.shape[0] < 8:
                        self.RRA2 = np.append(self.RRA2, last_RR)
                    else:
                        self.RRA2[:-1] = self.RRA2[1:]
                        self.RRA2[-1] = last_RR
        return beat_index


class PPG_Processor():
    def __init__(self, fs):
        self.fs = fs
        self.bl, self.al = signal.butter(3, 20 / self.fs, 'lowpass')  # 10Hz
        self.bh, self.ah = signal.butter(2, .6 / self.fs, 'highpass')  # 0.3Hz
        self.bh_hr, self.ah_hr = signal.butter(3, 10 / self.fs, 'highpass')  # 5Hz
        self.zi_lp = signal.lfilter_zi(self.bl, self.al)
        self.zi_hp = signal.lfilter_zi(self.bh, self.ah)

    def data_processor(self, data):
        data, self.zi_lp = signal.lfilter(self.bl, self.al, data, zi=self.zi_lp)
        data, self.zi_hp = signal.lfilter(self.bh, self.ah, data, zi=self.zi_hp)
        return data.tolist()
        # return data

    def preprocessor(self, data):
        # quad
        preprocessed = signal.filtfilt(self.bh_hr, self.ah_hr, data, method='pad')
        preprocessed **= 2
        # Moving average
        preprocessed = signal.filtfilt(np.ones(round(0.150 * self.fs)) / round(0.150 * self.fs), 1, preprocessed,
                                       method='pad')
        return preprocessed


class PPG_Running(dataCollector, PPG_Processor, heart_Rate):
    # buffer len (in sec)
    bufferlen = 6
    # heart_rate buffer
    hr_buffer = 70 // 60 * bufferlen
    # R ind
    indR = None
    # flag to initialize algorithm
    first_run = True

    def __init__(self):
        dataCollector.__init__(self)
        PPG_Processor.__init__(self, self.fs)
        self.databuffer = []
        self.buffersize = self.fs * self.bufferlen
        self.time = time.time()

    def reset_state(self):
        self.first_run = True

    def receive_data(self):
        data = super(PPG_Running, self).receive_data()
        # debug use only
        # print(time.time() - self.time)
        # parameter for debug
        self.time = time.time()
        self.databuffer += self.data_processor(data)
        if len(self.databuffer) > self.buffersize:
            self.databuffer = self.databuffer[-self.buffersize:]

    def heart_rate(self):
        if len(self.databuffer) < 5 * self.fs:
            return -1
        # preprocessing data
        filter_out = self.preprocessor(self.databuffer)
        # running
        if self.first_run:
            self.first_run = False
            heart_Rate.__init__(self, filter_out, self.fs)
        beat_index = self.run(filter_out)
        # update hr buffer
        print(len(beat_index))
        self.hr_buffer = 0.7 * self.hr_buffer + 0.3 * len(beat_index)
        return self.hr_buffer * 60 // self.bufferlen

    def HRV_analysis(self):
        # load data
        self.fileIO.close()
        with open('data', 'rb') as f:
            data = f.read()
        data_unpacked = struct.unpack('>%dh' % (len(data) // 2), data)
        data_V = - np.array(data_unpacked) / 32767 * self.FSR
        lp = signal.filtfilt(self.bl, self.al, data_V, method='pad')
        pre_processed = self.preprocessor(lp)
        hr = heart_Rate(pre_processed, self.fs)
        beats = hr.run(pre_processed)
        Rate = 60 * self.fs / np.diff(beats)
        self.fileIO = open('data', 'ab')
        return Rate
