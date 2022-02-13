from UI.login import Ui_Login_win as login
from UI.signup import Ui_signup_window as signup
from UI.editor import Ui_editor_window as editor
from UI.welcome import Ui_MainWindow as welcome

from PyQt5 import QtWidgets

class loader:#load the login form 
    
    windows = [welcome,signup,login,editor]

    @staticmethod
    def load(func):
        win = QtWidgets.QMainWindow()
        ui = func()
        ui.setupUi(win)
        return ui,win