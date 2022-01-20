# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signup_window(object):
    def setupUi(self, signup_window):
        signup_window.setObjectName("signup_window")
        signup_window.resize(800, 600)
        self.clicked = 0
        self.validated = 0
        self.signup = QtWidgets.QWidget(signup_window)
        self.signup.setObjectName("signup")
        self.gridLayout = QtWidgets.QGridLayout(self.signup)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.signup_grp = QtWidgets.QGroupBox(self.signup)
        self.signup_grp.setTitle("")
        self.signup_grp.setStyleSheet("background-color: rgb(28, 113, 216);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 50, 255), stop:1 rgba(28, 113, 216, 255));\n"
"")
        self.signup_grp.setObjectName("signup_grp")
        self.uname_2 = QtWidgets.QLineEdit(self.signup_grp)
        self.uname_2.setGeometry(QtCore.QRect(150, 220, 491, 31))
        self.uname_2.setStyleSheet("background-color: rgba(0, 0, 0, 125);")
        self.uname_2.setObjectName("uname_2")
        self.passwd_2 = QtWidgets.QLineEdit(self.signup_grp)
        self.passwd_2.setGeometry(QtCore.QRect(150, 390, 491, 31))
        self.passwd_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_2.setStyleSheet("background-color: rgba(0, 0, 0, 125);")
        self.passwd_2.setObjectName("passwd_2")
        self.label_7 = QtWidgets.QLabel(self.signup_grp)
        self.label_7.setGeometry(QtCore.QRect(150, 360, 181, 32))
        self.label_7.setWordWrap(True)
        self.label_7.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.missmatch = QtWidgets.QLabel(self.signup_grp)
        self.missmatch.setGeometry(QtCore.QRect(240, 430, 311, 21))
        self.missmatch.setStyleSheet("color: rgb(230, 115, 115);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.missmatch.setAlignment(QtCore.Qt.AlignCenter)
        self.missmatch.setWordWrap(True)
        self.missmatch.setObjectName("missmatch")
        self.signup_btn = QtWidgets.QPushButton(self.signup_grp)
        self.signup_btn.setGeometry(QtCore.QRect(330, 490, 131, 41))
        self.signup_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(26, 95, 180);\n"
"background-color: rgb(53, 132, 228);\n"
"selection-background-color: rgb(26, 95, 180);")
        self.signup_btn.clicked.connect(self.signup_function)
        self.signup_btn.setObjectName("signup_btn")
        self.label_5 = QtWidgets.QLabel(self.signup_grp)
        self.label_5.setGeometry(QtCore.QRect(220, 80, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(52)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.passwd_3 = QtWidgets.QLineEdit(self.signup_grp)
        self.passwd_3.setGeometry(QtCore.QRect(150, 300, 491, 31))
        self.passwd_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_3.setStyleSheet("background-color: rgba(0, 0, 0, 125);")
        self.passwd_3.setObjectName("passwd_3")
        self.label_4 = QtWidgets.QLabel(self.signup_grp)
        self.label_4.setGeometry(QtCore.QRect(150, 190, 91, 32))
        self.label_4.setWordWrap(True)
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.signup_grp)
        self.label_6.setGeometry(QtCore.QRect(150, 270, 91, 32))
        self.label_6.setWordWrap(True)
        self.label_6.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.signup_grp, 0, 0, 1, 1)
        signup_window.setCentralWidget(self.signup)

        self.retranslateUi(signup_window)
        QtCore.QMetaObject.connectSlotsByName(signup_window)

    def retranslateUi(self, signup_window):
        _translate = QtCore.QCoreApplication.translate
        signup_window.setWindowTitle(_translate("signup_window", "MainWindow"))
        self.label_7.setText(_translate("signup_window", "Re-enter password"))
        self.missmatch.setText(_translate("signup_window", "Please Retype the password Correctly"))
        self.signup_btn.setText(_translate("signup_window", "Sign Up"))
        self.label_5.setText(_translate("signup_window", "Sign Up"))
        self.label_4.setText(_translate("signup_window", "Username"))
        self.label_6.setText(_translate("signup_window", "Password"))
        self.missmatch.hide()
    def signup_function(self):
        
        #
        #validate password
        #if mismatch ,
        #self.missmatch.show()
        #  update self.validated  
        #create user db 
        #
        #
        self.clicked=1
        QtWidgets.qApp.quit()
