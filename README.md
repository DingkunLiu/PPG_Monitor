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
Communication: Serial Port: Baud Rate: 115200  
GUI: programmed in PyQt5  
PPG wave display: use matplotlib  
Real time heart rate calculation: Pan Tompkins algorithm  
HRV(Heart rate variability) analysis: When stop collection, user could press "HRV" buttom to   
  plot n-t curve and histogram of heart rate. Result can be found in PC directory.  

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



