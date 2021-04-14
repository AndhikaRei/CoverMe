# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from autentikasi import *
from Klien_PesanRS import *
from Admin_RS import *


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        self.LoginWindow = LoginWindow
        self.LoginWindow.setObjectName("LoginWindow")
        self.LoginWindow.resize(974, 621)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gambar_1 = QtWidgets.QLabel(self.centralwidget)
        self.gambar_1.setGeometry(QtCore.QRect(25, 140, 231, 291))
        self.gambar_1.setAutoFillBackground(False)
        self.gambar_1.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.gambar_1.setText("")
        self.gambar_1.setTextFormat(QtCore.Qt.AutoText)
        self.gambar_1.setPixmap(QtGui.QPixmap("../img/dummy.jpg"))
        self.gambar_1.setScaledContents(True)
        self.gambar_1.setWordWrap(False)
        self.gambar_1.setObjectName("gambar_1")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(50, 50, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label_info")
        self.size_background = QtWidgets.QLabel(self.centralwidget)
        self.size_background.setGeometry(QtCore.QRect(775, -15, 211, 626))
        self.size_background.setAutoFillBackground(False)
        self.size_background.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.size_background.setText("")
        self.size_background.setTextFormat(QtCore.Qt.AutoText)
        self.size_background.setScaledContents(False)
        self.size_background.setWordWrap(False)
        self.size_background.setObjectName("size_background")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(550, 80, 356, 486))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_login = QtWidgets.QLabel(self.page)
        self.label_login.setGeometry(QtCore.QRect(125, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_login.setFont(font)
        self.label_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login.setObjectName("label_login")
        self.label_username = QtWidgets.QLabel(self.page)
        self.label_username.setGeometry(QtCore.QRect(25, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(self.page)
        self.label_password.setGeometry(QtCore.QRect(25, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.box_username = QtWidgets.QLineEdit(self.page)
        self.box_username.setGeometry(QtCore.QRect(120, 110, 181, 31))
        self.box_username.setObjectName("box_username")
        self.box_password = QtWidgets.QLineEdit(self.page)
        self.box_password.setGeometry(QtCore.QRect(120, 150, 181, 31))
        self.box_password.setObjectName("box_password")
        self.login_Button = QtWidgets.QPushButton(self.page)
        self.login_Button.setGeometry(QtCore.QRect(135, 215, 93, 28))
        self.login_Button.setObjectName("login_Button")
        self.label_1 = QtWidgets.QLabel(self.page)
        self.label_1.setGeometry(QtCore.QRect(95, 270, 116, 16))
        self.label_1.setObjectName("label_1")
        self.frame_login = QtWidgets.QLabel(self.page)
        self.frame_login.setGeometry(QtCore.QRect(0, 0, 356, 376))
        self.frame_login.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);")
        self.frame_login.setText("")
        self.frame_login.setObjectName("frame_login")
        self.button_toRegister = QtWidgets.QPushButton(self.page)
        self.button_toRegister.setGeometry(QtCore.QRect(210, 265, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.button_toRegister.setFont(font)
        self.button_toRegister.setObjectName("button_toRegister")
        self.frame_login.raise_()
        self.label_login.raise_()
        self.label_username.raise_()
        self.label_password.raise_()
        self.box_password.raise_()
        self.box_username.raise_()
        self.login_Button.raise_()
        self.label_1.raise_()
        self.button_toRegister.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setAutoFillBackground(False)
        self.page_2.setObjectName("page_2")
        self.label_login_2 = QtWidgets.QLabel(self.page_2)
        self.label_login_2.setGeometry(QtCore.QRect(120, 25, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_login_2.setFont(font)
        self.label_login_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login_2.setObjectName("label_login_2")
        self.frame_login_2 = QtWidgets.QLabel(self.page_2)
        self.frame_login_2.setGeometry(QtCore.QRect(0, 0, 356, 486))
        self.frame_login_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);")
        self.frame_login_2.setText("")
        self.frame_login_2.setObjectName("frame_login_2")
        self.label_login_3 = QtWidgets.QLabel(self.page_2)
        self.label_login_3.setGeometry(QtCore.QRect(130, 30, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_login_3.setFont(font)
        self.label_login_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login_3.setObjectName("label_login_3")
        self.label_password_2 = QtWidgets.QLabel(self.page_2)
        self.label_password_2.setGeometry(QtCore.QRect(25, 165, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_password_2.setFont(font)
        self.label_password_2.setObjectName("label_password_2")
        self.box_telepon = QtWidgets.QLineEdit(self.page_2)
        self.box_telepon.setGeometry(QtCore.QRect(140, 285, 191, 31))
        self.box_telepon.setObjectName("box_telepon")
        self.box_alamat = QtWidgets.QLineEdit(self.page_2)
        self.box_alamat.setGeometry(QtCore.QRect(140, 205, 191, 31))
        self.box_alamat.setObjectName("box_alamat")
        self.label_email = QtWidgets.QLabel(self.page_2)
        self.label_email.setGeometry(QtCore.QRect(25, 325, 106, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.box_password_2 = QtWidgets.QLineEdit(self.page_2)
        self.box_password_2.setGeometry(QtCore.QRect(140, 165, 191, 31))
        self.box_password_2.setObjectName("box_password_2")
        self.label_alamat = QtWidgets.QLabel(self.page_2)
        self.label_alamat.setGeometry(QtCore.QRect(25, 205, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_alamat.setFont(font)
        self.label_alamat.setObjectName("label_alamat")
        self.label_username_2 = QtWidgets.QLabel(self.page_2)
        self.label_username_2.setGeometry(QtCore.QRect(25, 125, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_username_2.setFont(font)
        self.label_username_2.setObjectName("label_username_2")
        self.dateEdit = QtWidgets.QDateEdit(self.page_2)
        self.dateEdit.setGeometry(QtCore.QRect(140, 245, 191, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(105, 435, 116, 16))
        self.label_2.setObjectName("label_2")
        self.button_register = QtWidgets.QPushButton(self.page_2)
        self.button_register.setGeometry(QtCore.QRect(130, 380, 93, 28))
        self.button_register.setObjectName("button_register")
        self.box_email = QtWidgets.QLineEdit(self.page_2)
        self.box_email.setGeometry(QtCore.QRect(140, 325, 191, 31))
        self.box_email.setObjectName("box_email")
        self.box_nama = QtWidgets.QLineEdit(self.page_2)
        self.box_nama.setGeometry(QtCore.QRect(140, 85, 191, 31))
        self.box_nama.setObjectName("box_nama")
        self.label_nama = QtWidgets.QLabel(self.page_2)
        self.label_nama.setGeometry(QtCore.QRect(25, 85, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nama.setFont(font)
        self.label_nama.setObjectName("label_nama")
        self.label_tanggal_lahir = QtWidgets.QLabel(self.page_2)
        self.label_tanggal_lahir.setGeometry(QtCore.QRect(25, 245, 106, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_tanggal_lahir.setFont(font)
        self.label_tanggal_lahir.setObjectName("label_tanggal_lahir")
        self.label_telepon = QtWidgets.QLabel(self.page_2)
        self.label_telepon.setGeometry(QtCore.QRect(25, 285, 106, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_telepon.setFont(font)
        self.label_telepon.setObjectName("label_telepon")
        self.box_username_2 = QtWidgets.QLineEdit(self.page_2)
        self.box_username_2.setGeometry(QtCore.QRect(140, 125, 191, 31))
        self.box_username_2.setObjectName("box_username_2")
        self.button_toLogin = QtWidgets.QPushButton(self.page_2)
        self.button_toLogin.setGeometry(QtCore.QRect(220, 430, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.button_toLogin.setFont(font)
        self.button_toLogin.setObjectName("button_toLogin")
        self.stackedWidget.addWidget(self.page_2)
        self.gambar_2 = QtWidgets.QLabel(self.centralwidget)
        self.gambar_2.setGeometry(QtCore.QRect(265, 140, 231, 161))
        self.gambar_2.setAutoFillBackground(False)
        self.gambar_2.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.gambar_2.setText("")
        self.gambar_2.setTextFormat(QtCore.Qt.AutoText)
        self.gambar_2.setPixmap(QtGui.QPixmap("../img/dummy.jpg"))
        self.gambar_2.setScaledContents(True)
        self.gambar_2.setWordWrap(False)
        self.gambar_2.setObjectName("gambar_2")
        self.gambar_3 = QtWidgets.QLabel(self.centralwidget)
        self.gambar_3.setGeometry(QtCore.QRect(265, 310, 231, 241))
        self.gambar_3.setAutoFillBackground(False)
        self.gambar_3.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.gambar_3.setText("")
        self.gambar_3.setTextFormat(QtCore.Qt.AutoText)
        self.gambar_3.setPixmap(QtGui.QPixmap("../img/dummy.jpg"))
        self.gambar_3.setScaledContents(True)
        self.gambar_3.setWordWrap(False)
        self.gambar_3.setObjectName("gambar_3")
        self.gambar_4 = QtWidgets.QLabel(self.centralwidget)
        self.gambar_4.setGeometry(QtCore.QRect(25, 440, 231, 111))
        self.gambar_4.setAutoFillBackground(False)
        self.gambar_4.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.gambar_4.setText("")
        self.gambar_4.setTextFormat(QtCore.Qt.AutoText)
        self.gambar_4.setPixmap(QtGui.QPixmap("../img/dummy.jpg"))
        self.gambar_4.setScaledContents(True)
        self.gambar_4.setWordWrap(False)
        self.gambar_4.setObjectName("gambar_4")
        self.size_background.raise_()
        self.stackedWidget.raise_()
        self.gambar_1.raise_()
        self.label_info.raise_()
        self.gambar_2.raise_()
        self.gambar_3.raise_()
        self.gambar_4.raise_()
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        
        self.box_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.box_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        
        # Fungsionalitas Tambahan
        # Setup SQL
        self.setupSQL()
        
        # Ketika tombol toRegister diklik
        self.button_toRegister.clicked.connect(self.toRegister)
        # Ketika tombol toLogin diklik
        self.button_toLogin.clicked.connect(self.toLogin)
        
        # Ketika tombol login diklik
        self.login_Button.clicked.connect(self.login)
        
        # Ketika tombol register diklik
        self.button_register.clicked.connect(self.register)
        

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Cover Me"))
        self.label_info.setText(_translate("LoginWindow", "KAMI TIDAK PEDULI"))
        self.label_login.setText(_translate("LoginWindow", "LOGIN"))
        self.label_username.setText(_translate("LoginWindow", "Username"))
        self.label_password.setText(_translate("LoginWindow", "Password"))
        self.login_Button.setText(_translate("LoginWindow", "Login"))
        self.label_1.setText(_translate("LoginWindow", "Belum punya akun?"))
        self.button_toRegister.setText(_translate("LoginWindow", "Register"))
        self.label_login_2.setText(_translate("LoginWindow", "REGISTER"))
        self.label_login_3.setText(_translate("LoginWindow", "REGISTER"))
        self.label_password_2.setText(_translate("LoginWindow", "Password"))
        self.label_email.setText(_translate("LoginWindow", "Email"))
        self.label_alamat.setText(_translate("LoginWindow", "Alamat"))
        self.label_username_2.setText(_translate("LoginWindow", "Username"))
        self.label_2.setText(_translate("LoginWindow", "Sudah punya akun?"))
        self.button_register.setText(_translate("LoginWindow", "Register"))
        self.label_nama.setText(_translate("LoginWindow", "Nama"))
        self.label_tanggal_lahir.setText(_translate("LoginWindow", "Tanggal Lahir"))
        self.label_telepon.setText(_translate("LoginWindow", "Telepon"))
        self.button_toLogin.setText(_translate("LoginWindow", "Login"))
    
    def showAlert(self,err):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(err)
        x = msg.exec_()

    def showSucc(self,succ):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(succ)
        x = msg.exec_()
    
    def setupSQL(self):
        # Configurasi
        config = {
            "user": "root",
            "password": "root",
            "host": "localhost",
            "port" : "3307"
        }
        # Nama database
        self.DB_NAME = "Cover_Me"
        # Database yang sedang connect
        self.db = mysql.connector.connect(**config)
        # Cursor database
        self.cursor = self.db.cursor()
    
    
    def toRegister(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def toLogin(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def login(self):
        username = self.box_username.text()
        password = self.box_password.text()
        
        if len(username) == 0 or len(password) == 0:
            self.showAlert("Kolom username atau password tidak boleh kosong")
            return
        
        val = [username, password]
        result = get_user_id(self.cursor,self.DB_NAME, val)
        
        if result[0] == 1:
            self.showSucc("Login berhasil")
            ID_Pengguna = result[1]
            Role = get_role(self.cursor,self.DB_NAME, ID_Pengguna)[1]
            print(Role)
            if (Role =="Klien"):
                self.toKlienHome(ID_Pengguna)
            else :
                self.to_Admin_Home(ID_Pengguna)
            return
        if result[0] == -1:
            self.showAlert("Password salah")
            return
        if result[0] == -2:
            self.showAlert("Username tidak ditemukan")
            return
        if result[0] == 0:
            print(result[1])
            self.showAlert("General Error")
            return
        
    def register(self):
        nama = self.box_nama.text()
        username = self.box_username_2.text()
        password = self.box_password_2.text()
        alamat = self.box_alamat.text()
        tanggal_lahir = str(self.dateEdit.date().toPyDate())
        telepon = self.box_telepon.text()   
        email = self.box_email.text()
        
        val = [nama, username, password, email, alamat, tanggal_lahir, telepon]
        for data in val:
            if len(data) == 0:
                self.showAlert("Tidak boleh ada kolom yang kosong")
                return
        
        regex_email = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
        if not re.search(regex_email, email):
            self.showAlert("Format email salah")
            return
        
        result = add_new_user(self.db, self.cursor, self.DB_NAME, val)
        
        if result[0] == 1:
            self.showSucc("Registrasi berhasil, silahkan login")
            self.box_nama.setText("")
            self.box_username_2.setText("")
            self.box_password_2.setText("")
            self.box_alamat.setText("")
            self.box_telepon.setText("")   
            self.box_email.setText("")
            return
        
        if result[0] == -1:
            self.showAlert("Username sudah digunakan")
            return
        
        if result[0] == 0:
            print(result[1])
            self.showAlert("General Error")
            return
        
    def to_Admin_Home(self, ID_Pengguna):
        # Navigate to update laporan page
        from Admin_Home import Ui_AdminHomeWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminHomeWindow()
        self.ui.setupUi(self.window, ID_Pengguna)
        self.window.show()
        self.LoginWindow.close()
        print("Admin_Home")
        return
    
    def toKlienHome(self,ID_Pengguna):
        from Klien_PesanRS import Ui_PesanRSWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PesanRSWindow()
        self.ui.setupUi(self.window,ID_Pengguna)
        self.window.show()
        self.LoginWindow.close()
        print("To klien")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
