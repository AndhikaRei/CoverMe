# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Laporan_Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from update_laporan import *
from Admin_RS import *
from Admin_Home import *
from autentikasi import *
from Init_DBData import *
from datetime import date

class Ui_LaporanAdminWindow(object):
    def setupUi(self, LaporanAdminWindow, ID_Pengguna=1):
        self.LaporanAdminWindow = LaporanAdminWindow
        self.ID_Pengguna = ID_Pengguna
        self.LaporanAdminWindow.setObjectName("LaporanAdminWindow")
        self.LaporanAdminWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(LaporanAdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.background.setText("")
        self.background.setTextFormat(QtCore.Qt.PlainText)
        self.background.setPixmap(QtGui.QPixmap("../img/background.png"))
        self.background.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.background.setObjectName("background")
        self.topbar = QtWidgets.QLabel(self.centralwidget)
        self.topbar.setGeometry(QtCore.QRect(210, 0, 691, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.topbar.setFont(font)
        self.topbar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(80, 80, 80);")
        self.topbar.setObjectName("topbar")
        self.icon_notif = QtWidgets.QLabel(self.centralwidget)
        self.icon_notif.setGeometry(QtCore.QRect(850, 15, 20, 20))
        self.icon_notif.setText("")
        self.icon_notif.setPixmap(QtGui.QPixmap("../img/notif.png"))
        self.icon_notif.setScaledContents(True)
        self.icon_notif.setObjectName("icon_notif")
        self.icon_calendar = QtWidgets.QLabel(self.centralwidget)
        self.icon_calendar.setGeometry(QtCore.QRect(710, 15, 20, 20))
        self.icon_calendar.setText("")
        self.icon_calendar.setPixmap(QtGui.QPixmap("../img/cal.png"))
        self.icon_calendar.setScaledContents(True)
        self.icon_calendar.setObjectName("icon_calendar")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(740, 15, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(0, 195, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_home.setFont(font)
        self.button_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_home.setAutoFillBackground(False)
        self.button_home.setStyleSheet("Text-align:left;\n"
"background-color: rgb(251, 242, 215);\n"
"color: rgb(150, 150, 150);")
        self.button_home.setFlat(True)
        self.button_home.setObjectName("button_home")
        self.icon_home = QtWidgets.QLabel(self.centralwidget)
        self.icon_home.setGeometry(QtCore.QRect(20, 200, 20, 20))
        self.icon_home.setText("")
        self.icon_home.setPixmap(QtGui.QPixmap("../img/home-gray.png"))
        self.icon_home.setScaledContents(True)
        self.icon_home.setObjectName("icon_home")
        self.button_laporan = QtWidgets.QPushButton(self.centralwidget)
        self.button_laporan.setGeometry(QtCore.QRect(0, 226, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_laporan.setFont(font)
        self.button_laporan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_laporan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_laporan.setAutoFillBackground(False)
        self.button_laporan.setStyleSheet("background-color: rgb(218, 114, 60);\n"
"color: rgb(255, 255, 255);\n"
"Text-align:left;")
        self.button_laporan.setFlat(False)
        self.button_laporan.setObjectName("button_laporan")
        self.icon_laporan = QtWidgets.QLabel(self.centralwidget)
        self.icon_laporan.setGeometry(QtCore.QRect(20, 233, 20, 20))
        self.icon_laporan.setText("")
        self.icon_laporan.setPixmap(QtGui.QPixmap("../img/laporan-white.png"))
        self.icon_laporan.setScaledContents(True)
        self.icon_laporan.setObjectName("icon_laporan")
        self.icon_rs = QtWidgets.QLabel(self.centralwidget)
        self.icon_rs.setGeometry(QtCore.QRect(20, 263, 20, 20))
        self.icon_rs.setText("")
        self.icon_rs.setPixmap(QtGui.QPixmap("../img/hospital-gray.png"))
        self.icon_rs.setScaledContents(True)
        self.icon_rs.setObjectName("icon_rs")
        self.button_rs = QtWidgets.QPushButton(self.centralwidget)
        self.button_rs.setGeometry(QtCore.QRect(0, 257, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_rs.setFont(font)
        self.button_rs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_rs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_rs.setAutoFillBackground(False)
        self.button_rs.setStyleSheet("Text-align:left;\n"
"background-color: rgb(251, 242, 215);\n"
"color: rgb(150, 150, 150);")
        self.button_rs.setFlat(True)
        self.button_rs.setObjectName("button_rs")
        self.icon_pesanan = QtWidgets.QLabel(self.centralwidget)
        self.icon_pesanan.setGeometry(QtCore.QRect(20, 294, 20, 20))
        self.icon_pesanan.setText("")
        self.icon_pesanan.setPixmap(QtGui.QPixmap("../img/pesanan-gray.png"))
        self.icon_pesanan.setScaledContents(True)
        self.icon_pesanan.setObjectName("icon_pesanan")
        self.button_pesanan = QtWidgets.QPushButton(self.centralwidget)
        self.button_pesanan.setGeometry(QtCore.QRect(0, 288, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_pesanan.setFont(font)
        self.button_pesanan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_pesanan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_pesanan.setAutoFillBackground(False)
        self.button_pesanan.setStyleSheet("Text-align:left;\n"
"background-color: rgb(251, 242, 215);\n"
"color: rgb(150, 150, 150);")
        self.button_pesanan.setFlat(True)
        self.button_pesanan.setObjectName("button_pesanan")
        self.button_logout = QtWidgets.QPushButton(self.centralwidget)
        self.button_logout.setGeometry(QtCore.QRect(0, 534, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_logout.setFont(font)
        self.button_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_logout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_logout.setAutoFillBackground(False)
        self.button_logout.setStyleSheet("Text-align:left;\n"
"background-color: rgb(251, 242, 215);\n"
"color: rgb(150, 150, 150);")
        self.button_logout.setFlat(True)
        self.button_logout.setObjectName("button_logout")
        self.icon_logout = QtWidgets.QLabel(self.centralwidget)
        self.icon_logout.setGeometry(QtCore.QRect(20, 540, 20, 20))
        self.icon_logout.setText("")
        self.icon_logout.setPixmap(QtGui.QPixmap("../img/power-gray.png"))
        self.icon_logout.setScaledContents(True)
        self.icon_logout.setObjectName("icon_logout")
        self.icon_avatar = QtWidgets.QLabel(self.centralwidget)
        self.icon_avatar.setGeometry(QtCore.QRect(0, 140, 61, 41))
        self.icon_avatar.setText("")
        self.icon_avatar.setPixmap(QtGui.QPixmap("../img/avatar.png"))
        self.icon_avatar.setScaledContents(True)
        self.icon_avatar.setObjectName("icon_avatar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 146, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(150, 150, 150);")
        self.label.setObjectName("label")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(60, 161, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_email.setFont(font)
        self.label_email.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_email.setObjectName("label_email")
        self.box_positif = QtWidgets.QLabel(self.centralwidget)
        self.box_positif.setGeometry(QtCore.QRect(445, 340, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.box_positif.setFont(font)
        self.box_positif.setStyleSheet("border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 114, 60);")
        self.box_positif.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.box_positif.setObjectName("box_positif")
        self.box_sembuh = QtWidgets.QLabel(self.centralwidget)
        self.box_sembuh.setGeometry(QtCore.QRect(240, 445, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.box_sembuh.setFont(font)
        self.box_sembuh.setStyleSheet("border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 114, 60);")
        self.box_sembuh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.box_sembuh.setObjectName("box_sembuh")
        self.box_meninggal = QtWidgets.QLabel(self.centralwidget)
        self.box_meninggal.setGeometry(QtCore.QRect(650, 445, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_meninggal.setFont(font)
        self.box_meninggal.setStyleSheet("border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 114, 60);")
        self.box_meninggal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.box_meninggal.setObjectName("box_meninggal")
        self.button_edit_positif = QtWidgets.QPushButton(self.centralwidget)
        self.button_edit_positif.setGeometry(QtCore.QRect(455, 345, 41, 23))
        self.button_edit_positif.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_edit_positif.setStyleSheet("background-color: rgb(145, 9, 30);\n"
"color: rgb(255, 255, 255);")
        self.button_edit_positif.setObjectName("button_edit_positif")
        self.button_simpan_positif = QtWidgets.QPushButton(self.centralwidget)
        self.button_simpan_positif.setGeometry(QtCore.QRect(455, 390, 41, 23))
        self.button_simpan_positif.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_simpan_positif.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 184, 92);")
        self.button_simpan_positif.setObjectName("button_simpan_positif")
        self.button_simpan_sembuh = QtWidgets.QPushButton(self.centralwidget)
        self.button_simpan_sembuh.setGeometry(QtCore.QRect(250, 495, 41, 23))
        self.button_simpan_sembuh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_simpan_sembuh.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 184, 92);")
        self.button_simpan_sembuh.setObjectName("button_simpan_sembuh")
        self.button_edit_sembuh = QtWidgets.QPushButton(self.centralwidget)
        self.button_edit_sembuh.setGeometry(QtCore.QRect(250, 450, 41, 23))
        self.button_edit_sembuh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_edit_sembuh.setStyleSheet("background-color: rgb(145, 9, 30);\n"
"color: rgb(255, 255, 255);")
        self.button_edit_sembuh.setObjectName("button_edit_sembuh")
        self.button_simpan_meninggal = QtWidgets.QPushButton(self.centralwidget)
        self.button_simpan_meninggal.setGeometry(QtCore.QRect(660, 495, 41, 23))
        self.button_simpan_meninggal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_simpan_meninggal.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 184, 92);")
        self.button_simpan_meninggal.setObjectName("button_simpan_meninggal")
        self.button_edit_meninggal = QtWidgets.QPushButton(self.centralwidget)
        self.button_edit_meninggal.setGeometry(QtCore.QRect(660, 450, 41, 23))
        self.button_edit_meninggal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_edit_meninggal.setStyleSheet("background-color: rgb(145, 9, 30);\n"
"color: rgb(255, 255, 255);")
        self.button_edit_meninggal.setObjectName("button_edit_meninggal")
        self.box_positif_2 = QtWidgets.QLabel(self.centralwidget)
        self.box_positif_2.setGeometry(QtCore.QRect(230, 140, 651, 171))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.box_positif_2.setFont(font)
        self.box_positif_2.setStyleSheet("border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 114, 60);")
        self.box_positif_2.setText("")
        self.box_positif_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.box_positif_2.setObjectName("box_positif_2")
        self.box_positif_3 = QtWidgets.QLabel(self.centralwidget)
        self.box_positif_3.setGeometry(QtCore.QRect(260, 91, 181, 220))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.box_positif_3.setFont(font)
        self.box_positif_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(251, 242, 215,70%);\n"
"border-radius:5px")
        self.box_positif_3.setText("")
        self.box_positif_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.box_positif_3.setObjectName("box_positif_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(262, 100, 171, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../img/doctor.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 170, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 200, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 230, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 250, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.edit_sembuh = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_sembuh.setEnabled(False)
        self.edit_sembuh.setGeometry(QtCore.QRect(300, 480, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.edit_sembuh.setFont(font)
        self.edit_sembuh.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"qproperty-frame: false;\n"
"color: rgb(145, 9, 30);")
        self.edit_sembuh.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_sembuh.setObjectName("edit_sembuh")
        self.edit_positif = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_positif.setEnabled(False)
        self.edit_positif.setGeometry(QtCore.QRect(505, 375, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.edit_positif.setFont(font)
        self.edit_positif.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"qproperty-frame: false;\n"
"color: rgb(145, 9, 30);")
        self.edit_positif.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_positif.setObjectName("edit_positif")
        self.edit_meninggal = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_meninggal.setEnabled(False)
        self.edit_meninggal.setGeometry(QtCore.QRect(710, 480, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.edit_meninggal.setFont(font)
        self.edit_meninggal.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"qproperty-frame: false;\n"
"color: rgb(145, 9, 30);")
        self.edit_meninggal.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_meninggal.setObjectName("edit_meninggal")
        self.background.raise_()
        self.topbar.raise_()
        self.icon_notif.raise_()
        self.icon_calendar.raise_()
        self.label_date.raise_()
        self.button_home.raise_()
        self.icon_home.raise_()
        self.button_laporan.raise_()
        self.icon_laporan.raise_()
        self.button_rs.raise_()
        self.icon_rs.raise_()
        self.button_pesanan.raise_()
        self.icon_pesanan.raise_()
        self.button_logout.raise_()
        self.icon_logout.raise_()
        self.icon_avatar.raise_()
        self.label.raise_()
        self.label_email.raise_()
        self.box_positif.raise_()
        self.box_sembuh.raise_()
        self.box_meninggal.raise_()
        self.button_edit_positif.raise_()
        self.button_simpan_positif.raise_()
        self.button_simpan_sembuh.raise_()
        self.button_edit_sembuh.raise_()
        self.button_simpan_meninggal.raise_()
        self.button_edit_meninggal.raise_()
        self.box_positif_2.raise_()
        self.box_positif_3.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.edit_sembuh.raise_()
        self.edit_positif.raise_()
        self.edit_meninggal.raise_()
        self.LaporanAdminWindow.setCentralWidget(self.centralwidget)


        # Melakukan setup SQL
        self.setupSql()

        self.retranslateUi(LaporanAdminWindow)
        QtCore.QMetaObject.connectSlotsByName(LaporanAdminWindow)

        # Hide Simpan
        self.hideAllSimpan()
    
        # Connect Button
        self.button_edit_positif.clicked.connect(self.enableKasusPositif)
        self.button_edit_sembuh.clicked.connect(self.enablePasienSembuh)
        self.button_edit_meninggal.clicked.connect(self.enablePasienMeninggal)
        self.button_simpan_positif.clicked.connect(self.simpanKasusPositif)
        self.button_simpan_sembuh.clicked.connect(self.simpanPasienSembuh)
        self.button_simpan_meninggal.clicked.connect(self.simpanPasienMeninggal)
        self.button_logout.clicked.connect(self.logout)
        self.button_rs.clicked.connect(self.to_Data_RS)
        self.button_home.clicked.connect(self.to_Admin_Home)
        self.button_pesanan.clicked.connect(self.to_Admin_Pesanan)
        
        # Set Initial Value
        self.refreshAllValue()

    def retranslateUi(self, LaporanAdminWindow):
        _translate = QtCore.QCoreApplication.translate
        LaporanAdminWindow.setWindowTitle(_translate("LaporanAdminWindow", "LaporanAdminWindow"))
        self.topbar.setText(_translate("LaporanAdminWindow", "     Laporan Harian"))
        today = date.today()
        d2 = today.strftime("%d %B %Y")
        self.label_date.setText(_translate("LaporanAdminWindow", d2))
        self.button_home.setText(_translate("LaporanAdminWindow", "              Home"))
        self.button_laporan.setText(_translate("LaporanAdminWindow", "              Laporan Harian"))
        self.button_rs.setText(_translate("LaporanAdminWindow", "              Rumah Sakit"))
        self.button_pesanan.setText(_translate("LaporanAdminWindow", "              Daftar Pesanan"))
        self.button_logout.setText(_translate("LaporanAdminWindow", "              Logout"))
        Nama_User = get_nama(self.cursor,self.DB_NAME,self.ID_Pengguna)
        self.label.setText(_translate("LaporanAdminWindow", Nama_User[1]))
        Email_User = get_email(self.cursor,self.DB_NAME,self.ID_Pengguna)
        self.label_email.setText(_translate("LaporanAdminWindow", Email_User[1]))
        self.box_positif.setText(_translate("LaporanAdminWindow", "Kasus Positif    "))
        self.box_sembuh.setText(_translate("LaporanAdminWindow", "Pasien Sembuh   "))
        self.box_meninggal.setText(_translate("LaporanAdminWindow", "Pasien Meninggal    "))
        self.button_edit_positif.setText(_translate("LaporanAdminWindow", "Edit"))
        self.button_simpan_positif.setText(_translate("LaporanAdminWindow", "Simpan"))
        self.button_simpan_sembuh.setText(_translate("LaporanAdminWindow", "Simpan"))
        self.button_edit_sembuh.setText(_translate("LaporanAdminWindow", "Edit"))
        self.button_simpan_meninggal.setText(_translate("LaporanAdminWindow", "Simpan"))
        self.button_edit_meninggal.setText(_translate("LaporanAdminWindow", "Edit"))
        self.label_3.setText(_translate("LaporanAdminWindow", "Selamat Datang!"))
        self.label_4.setText(_translate("LaporanAdminWindow", "Role Anda adalah Admin"))
        self.label_5.setText(_translate("LaporanAdminWindow", "Anda dapat mengubah jumlah kasus positif, pasien"))
        self.label_6.setText(_translate("LaporanAdminWindow", "sembuh, dan pasien meninggal setiap harinya"))
        self.edit_sembuh.setText(_translate("LaporanAdminWindow", "100000"))
        self.edit_positif.setText(_translate("LaporanAdminWindow", "100000"))
        self.edit_meninggal.setText(_translate("LaporanAdminWindow", "100000"))

    def setupSql(self):
    # Melakukan setup koneksi SQL
        self.DB_NAME = get_DB_NAME()
        self.db = mysql.connector.connect(**get_config())
        self.cursor = self.db.cursor()
    
    def hideAllSimpan(self):
        self.button_simpan_positif.setVisible(False)
        self.button_simpan_sembuh.setVisible(False)
        self.button_simpan_meninggal.setVisible(False)

    def enableKasusPositif(self):
        self.edit_positif.setEnabled(True)
        self.button_simpan_positif.setVisible(True)
        
    def enablePasienSembuh(self):
        self.edit_sembuh.setEnabled(True)
        self.button_simpan_sembuh.setVisible(True)
    
    def enablePasienMeninggal(self):
        self.edit_meninggal.setEnabled(True)
        self.button_simpan_meninggal.setVisible(True)

    def refreshAllValue(self):
        test = get_kasus_positif(self.cursor, self.DB_NAME)[1][0][0]
        print(test)
        self.edit_positif.setText(str(get_kasus_positif(self.cursor, self.DB_NAME)[1][0][0]))
        self.edit_sembuh.setText(str(get_pasien_sembuh(self.cursor, self.DB_NAME)[1][0][0]))
        self.edit_meninggal.setText(str(get_pasien_meninggal(self.cursor, self.DB_NAME)[1][0][0]))

    def simpanKasusPositif(self):
        new = self.edit_positif.text()
        result = set_kasus_positif(self.db, self.cursor, self.DB_NAME, new)
        if(result[0]==0):
                self.showAlert(result[1])
        else:
                self.showSucc(result[1])
                self.button_simpan_positif.setVisible(False)
                self.edit_positif.setEnabled(False)
        self.refreshAllValue()
                
        
    def simpanPasienSembuh(self):
        new = self.edit_sembuh.text()
        result = set_pasien_sembuh(self.db, self.cursor, self.DB_NAME, new)
        if(result[0]==0):
                self.showAlert(result[1])
        else:
                self.showSucc(result[1])
                self.button_simpan_sembuh.setVisible(False)
                self.edit_sembuh.setEnabled(False)
        self.refreshAllValue()


    def simpanPasienMeninggal(self):
        new = self.edit_meninggal.text()
        result = set_pasien_meninggal(self.db, self.cursor, self.DB_NAME, new)
        if(result[0]==0):
                self.showAlert(result[1])
        else:
                self.showSucc(result[1])
                self.button_simpan_meninggal.setVisible(False)
                self.edit_meninggal.setEnabled(False)
        self.refreshAllValue()


    def showAlert(self,err):
        # Menampilkan pesan kesalahan
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(err)
        x = msg.exec_()
    
    def showSucc(self,succ):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(succ)
        x = msg.exec_()

    def logout(self):
        # Melakukan logout
        from Login_User import Ui_LoginScreen
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self.window)
        self.window.show()
        self.LaporanAdminWindow.close()
        print("Logout")
        return
        
    def to_Data_RS(self):
        # Navigate to update laporan page
        from RS_Admin import UI_RSAdminWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_RSAdminWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.LaporanAdminWindow.close()
        print("Data RS ")
        return

    def to_Admin_Home(self):
        # Navigate to update laporan page
        from Home_Admin import Ui_HomeAdminWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeAdminWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.LaporanAdminWindow.close()
        print("Admin_Home ")
        return

    def to_Admin_Pesanan(self):
        # Navigate to update laporan page
        from Pesanan_Admin import Ui_PesananAdminWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PesananAdminWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.LaporanAdminWindow.close()
        print("Admin_Pesanan ")
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LaporanAdminWindow = QtWidgets.QMainWindow()
    ui = Ui_LaporanAdminWindow()
    ui.setupUi(LaporanAdminWindow)
    LaporanAdminWindow.show()
    sys.exit(app.exec_())
