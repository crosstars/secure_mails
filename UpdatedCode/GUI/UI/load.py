from UI.login import Ui_Login_win as login
from UI.signup import Ui_signup_window as signup
from UI.editor import Ui_editor_window as editor
from UI.welcome import Ui_MainWindow as welcome
from UI.choser import Ui_Chooser as  chooser

from PyQt5 import QtWidgets

class loader:#load the login form 
    
    windows = [welcome,chooser,signup,login,editor]

    @staticmethod
    def load(func,login_info=None,ref=None):
        win = QtWidgets.QMainWindow()
        ui = func()
        ui.setupUi(win,login_info,ref)
        return ui,win