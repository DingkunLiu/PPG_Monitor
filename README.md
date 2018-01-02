PPG_Monitor
=============
PPG Monitor Using Photoelectric Capacitance Method  

Hardware Requirement  
-------------------  
1. 850nm LED * 1  
2. OPT101 * 1  
3. ADS1115 development board * 1  
4. Arduino development board * 1  
5. PC  

Features:  
----------
**Communication**: Serial Port: Baud Rate: 115200  
**GUI**: programmed in PyQt5  
**Real-time PPG wave display**: with matplotlib  
**Real-time heart rate calculation**: Modified Pan Tompkins algorithm (Differential threshold method)  
**HRV(Heart rate variability) analysis**: (Should pause data processor first.) Press "HRV" buttom to   
  plot heart rate curve over time and heart rate distribution histogram.  
  Result can be found in "./PC/result.png".  

Usage:  
----------  
**Configuration:** pip install -r requirements.txt  
**Run main:** python3 MainGUI.py  

Block Diagram:  
----------  
![Alt text](Img/PPG_EXP.png)  
GUI Main Window:  
----------  
![Alt text](Img/GUI.jpg)  
HRV analysis:  
----------  
![Alt text](Img/result.png)  



