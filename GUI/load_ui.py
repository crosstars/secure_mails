from PyQt5 import QtWidgets
from UI.load import loader
from Validation.validator import *
import sys

app=QtWidgets.QApplication(sys.argv)
    
ui,win = loader.load(loader.windows[0])
win.show()
app.exec_()

while True:
    #if clicked on welcome the the next window is loaded
    if ui.clicked == 1:
        if dbexists():
            ui,win = loader.load(loader.windows[1])
            win.show()
            app.exec_()
        else :
            ui,win = loader.load(loader.windows[2])
            win.show()
            app.exec_()
    else:
        break

    if ui.clicked == 1 :
        if ui.validated or 1 :#add or dbexists()[unimplimented only for testing]: 
        #for testing 
        # SHOULD BE 
        # REMOVED WHEN RUNNING
            ui,win = loader.load(loader.windows[3])
            win.show()
            app.exec_()
            break
        else:
            ui,win = loader.load(loader.windows[0])
            win.show()
            app.exec_()
    else:
        break

