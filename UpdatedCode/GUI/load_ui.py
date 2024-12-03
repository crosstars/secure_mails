from PyQt5 import QtWidgets
from UI.load import loader
#from Validation.validator import *
from Nosdb import connection as conn 
import sys



app=QtWidgets.QApplication(sys.argv)

ref = conn.connect()
ip = conn.ip()


ui,win = loader.load(loader.windows[0])

win.show()
app.exec_()

login_info=None
next = ui.next
while next !=-1:
    #if clicked on welcome the the next window is loaded
    if ui.clicked == 1:
            ui,win = loader.load(loader.windows[next],login_info=login_info,ref=ref)

            # conn.connect_ui(ui,ip,ref)
            # ui.ref = ref
            # ui.ip = ip
            win.show()
            app.exec_()
            if next == 3:
                login_info = ui.login_info

            next = ui.next
    # else:
    #     break

    # if ui.clicked == 1 :
    #     if ui.validated :#add or dbexists()[unimplimented only for testing]: 
    #     #for testing 
    #     # SHOULD BE 
    #     # REMOVED WHEN RUNNING
    #         ui,win = loader.load(loader.windows[3])
    #         conn.connect_ui(ui,ip,ref)

    #         win.show()
    #         app.exec_()
    #         break
    #     else:
    #         ui,win = loader.load(loader.windows[0])
    #         conn.connect_ui(ui,ip,ref)

    #         win.show()
    #         app.exec_()
    # else:
    #     break

