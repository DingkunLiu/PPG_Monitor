import sys
import struct
import serial
import os


class dataCollector():
    baudrate = 115200
    fs = 100
    serialtimeout = 0
    FSR = 4.096
    # uint16
    datatype = 2
    # file IO
    fileIO = None

    def __init__(self):
        assert self.datatype == 2 or self.datatype == 4
        try:
            if sys.platform == 'linux':
                self.serial_port = serial.Serial('/dev/ttyACM0', self.baudrate, timeout=self.serialtimeout)
            elif sys.platform == 'win32':
                self.serial_port = serial.Serial('COM3', self.baudrate, timeout=self.serialtimeout)
            self.reset_input_buffer()
        except Exception as err:
            print(err)

        if os.path.isfile('data'):
            os.remove('data')
        self.fileIO = open('data', 'ab')

    def reset_input_buffer(self):
        self.serial_port.reset_input_buffer()

    def receive_data(self):
        def convert(x):
            return - x / 32767.0 * self.FSR

        nbytes = self.serial_port.inWaiting() // 2 * 2
        bytes_received = self.serial_port.read(nbytes)
        try:
            self.fileIO.write(bytes_received)
        except Exception as err:
            print(err)

        if self.datatype == 2:
            data = struct.unpack('>%dh' % (nbytes // self.datatype), bytes_received)
        elif self.datatype == 4:
            data = struct.unpack('<%df' % (nbytes // self.datatype), bytes_received)
        else:
            data = None
        data = list(map(convert, data))
        return data
