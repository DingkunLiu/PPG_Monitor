from PyQt5 import uic

fin = open('PPG.ui', 'r')
fout = open('myUI.py', 'w')
uic.compileUi(fin, fout, execute=False)
fin.close()
fout.close()
