from PyQt5 import QtWidgets
from UI.load import loader
from Validation import *
import sys

app=QtWidgets.QApplication(sys.argv)
    
ui,win = loader.load(loader.windows[0])
win.show()
app.exec_()
print(ui.clicked)

#if clicked on welcome the the next window is loaded
if ui.clicked == 1:
    if (True):
        ui,win = loader.load(loader.windows[1])
        win.show()
        app.exec_()
    else :
        ui,win = loader.load(loader.windows[2])
        win.show()
        app.exec_()



