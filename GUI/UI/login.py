# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_win(object):
    def setupUi(self, Login_win):
        Login_win.setObjectName("Login_win")
        Login_win.resize(800, 624)
        self.validated = 0
        self.clicked = 0
        self.login = QtWidgets.QWidget(Login_win)
        self.login.setObjectName("login")
        self.gridLayout = QtWidgets.QGridLayout(self.login)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.login_grp = QtWidgets.QGroupBox(self.login)
        self.login_grp.setStyleSheet("background-color: rgb(28, 113, 216);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 50, 255), stop:1 rgba(28, 113, 216, 255));\n"
"")
        self.login_grp.setTitle("")
        self.login_grp.setObjectName("login_grp")
        self.label = QtWidgets.QLabel(self.login_grp)
        self.label.setGeometry(QtCore.QRect(190, 80, 381, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.error = QtWidgets.QLabel(self.login_grp)
        self.error.setEnabled(True)
        self.error.setGeometry(QtCore.QRect(290, 220, 201, 20))
        self.error.setStyleSheet("color: rgb(230, 115, 115);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setWordWrap(True)
        self.error.setObjectName("error")
        self.passwd = QtWidgets.QLineEdit(self.login_grp)
        self.passwd.setGeometry(QtCore.QRect(190, 410, 431, 31))
        self.passwd.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("passwd")
        self.label_2 = QtWidgets.QLabel(self.login_grp)
        self.label_2.setGeometry(QtCore.QRect(190, 370, 81, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.login_btn = QtWidgets.QPushButton(self.login_grp)
        self.login_btn.setGeometry(QtCore.QRect(570, 500, 101, 41))
        self.login_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(53, 132, 228);\n"
"alternate-background-color: rgb(53, 132, 228);\n"
"border-color: rgb(98, 160, 234);\n"
"selection-color: rgb(53, 132, 228);")
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.login_function)
        self.uname = QtWidgets.QLineEdit(self.login_grp)
        self.uname.setGeometry(QtCore.QRect(190, 300, 431, 31))
        self.uname.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.uname.setObjectName("uname")
        self.label_3 = QtWidgets.QLabel(self.login_grp)
        self.label_3.setGeometry(QtCore.QRect(190, 260, 281, 41))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.login_grp, 0, 0, 1, 1)
        Login_win.setCentralWidget(self.login)

        self.retranslateUi(Login_win)
        QtCore.QMetaObject.connectSlotsByName(Login_win)

    def retranslateUi(self, Login_win):
        _translate = QtCore.QCoreApplication.translate
        Login_win.setWindowTitle(_translate("Login_win", "MainWindow"))
        self.label.setText(_translate("Login_win", "Log In"))
        self.error.setText(_translate("Login_win", "Login info incorrect"))
        self.label_2.setText(_translate("Login_win", "Password"))
        self.login_btn.setText(_translate("Login_win", "Login"))
        self.uname.setWhatsThis(_translate("Login_win", "<html><head/><body><p>Username</p></body></html>"))
        self.label_3.setText(_translate("Login_win", "Username (Email id)"))
        self.error.hide()
    def login_function(self):
        
        #
        #validate password
        #if incorrect login info ,
        #self.error.show()
        #  update self.validated  
        #create user db 
        #
        #
        self.clicked=1
        QtWidgets.qApp.quit()