# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Klien_Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from update_laporan import *
from autentikasi import *
from Klien_PesanRS import *

class Ui_KlienHomeWindow(object):
        def setupUi(self, KlienHomeWindow, ID_Pengguna=2):
                self.KlienHomeWindow = KlienHomeWindow
                self.ID_Pengguna = ID_Pengguna
                self.KlienHomeWindow.setObjectName("KlienHomeWindow")
                self.KlienHomeWindow.resize(900, 600)
                self.centralwidget = QtWidgets.QWidget(KlienHomeWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.Nama_Admin = QtWidgets.QLabel(self.centralwidget)
                self.Nama_Admin.setGeometry(QtCore.QRect(650, 0, 251, 61))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.Nama_Admin.setFont(font)
                self.Nama_Admin.setObjectName("Nama_Admin")
                self.header_tambah = QtWidgets.QLabel(self.centralwidget)
                self.header_tambah.setGeometry(QtCore.QRect(355, 90, 401, 31))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.header_tambah.setFont(font)
                self.header_tambah.setStyleSheet("QLabel{\n"
                "    color: rgb(0, 0, 0);\n"
                "}")
                self.header_tambah.setObjectName("header_tambah")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(310, 130, 491, 281))
                self.label_2.setText("")
                self.label_2.setPixmap(QtGui.QPixmap("../img/nao.jpg"))
                self.label_2.setScaledContents(True)
                self.label_2.setObjectName("label_2")
                self.label_positif = QtWidgets.QLabel(self.centralwidget)
                self.label_positif.setGeometry(QtCore.QRect(310, 425, 141, 21))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(12)
                self.label_positif.setFont(font)
                self.label_positif.setAutoFillBackground(False)
                self.label_positif.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.label_positif.setAlignment(QtCore.Qt.AlignCenter)
                self.label_positif.setObjectName("label_positif")
                self.label_sembuh = QtWidgets.QLabel(self.centralwidget)
                self.label_sembuh.setGeometry(QtCore.QRect(485, 425, 141, 21))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(12)
                self.label_sembuh.setFont(font)
                self.label_sembuh.setAutoFillBackground(False)
                self.label_sembuh.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.label_sembuh.setAlignment(QtCore.Qt.AlignCenter)
                self.label_sembuh.setObjectName("label_sembuh")
                self.label_meninggal = QtWidgets.QLabel(self.centralwidget)
                self.label_meninggal.setGeometry(QtCore.QRect(660, 425, 141, 21))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(12)
                self.label_meninggal.setFont(font)
                self.label_meninggal.setAutoFillBackground(False)
                self.label_meninggal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.label_meninggal.setAlignment(QtCore.Qt.AlignCenter)
                self.label_meninggal.setObjectName("label_meninggal")
                self.label_kasus_positif = QtWidgets.QLabel(self.centralwidget)
                self.label_kasus_positif.setGeometry(QtCore.QRect(310, 450, 141, 81))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.label_kasus_positif.setFont(font)
                self.label_kasus_positif.setAutoFillBackground(False)
                self.label_kasus_positif.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.label_kasus_positif.setText("")
                self.label_kasus_positif.setAlignment(QtCore.Qt.AlignCenter)
                self.label_kasus_positif.setObjectName("label_kasus_positif")
                self.label_pasien_sembuh = QtWidgets.QLabel(self.centralwidget)
                self.label_pasien_sembuh.setGeometry(QtCore.QRect(485, 450, 141, 81))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.label_pasien_sembuh.setFont(font)
                self.label_pasien_sembuh.setAutoFillBackground(False)
                self.label_pasien_sembuh.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.label_pasien_sembuh.setText("")
                self.label_pasien_sembuh.setAlignment(QtCore.Qt.AlignCenter)
                self.label_pasien_sembuh.setObjectName("label_pasien_sembuh")
                self.label_pasien_meninggal = QtWidgets.QLabel(self.centralwidget)
                self.label_pasien_meninggal.setGeometry(QtCore.QRect(660, 450, 141, 81))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.label_pasien_meninggal.setFont(font)
                self.label_pasien_meninggal.setAutoFillBackground(False)
                self.label_pasien_meninggal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.label_pasien_meninggal.setText("")
                self.label_pasien_meninggal.setAlignment(QtCore.Qt.AlignCenter)
                self.label_pasien_meninggal.setObjectName("label_pasien_meninggal")
                self.Sidebar = QtWidgets.QFrame(self.centralwidget)
                self.Sidebar.setGeometry(QtCore.QRect(0, 0, 211, 591))
                self.Sidebar.setStyleSheet("QFrame{\n"
                "    background-color: rgb(72, 67, 67);\n"
                "}")
                self.Sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Sidebar.setObjectName("Sidebar")
                self.SuhuHarian = QtWidgets.QPushButton(self.Sidebar)
                self.SuhuHarian.setGeometry(QtCore.QRect(20, 180, 171, 51))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SuhuHarian.setFont(font)
                self.SuhuHarian.setStyleSheet("QPushButton{\n"
                "    background-color: rgb(72, 67, 67);\n"
                "    color: rgb(255, 255, 255);\n"
                "}")
                self.SuhuHarian.setObjectName("SuhuHarian")
                self.label = QtWidgets.QLabel(self.Sidebar)
                self.label.setGeometry(QtCore.QRect(20, 20, 171, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("QLabel{\n"
                "    color: rgb(255, 255, 255);\n"
                "}")
                self.label.setObjectName("label")
                self.PesanRS = QtWidgets.QPushButton(self.Sidebar)
                self.PesanRS.setGeometry(QtCore.QRect(20, 250, 171, 51))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.PesanRS.setFont(font)
                self.PesanRS.setStyleSheet("QPushButton{\n"
                "    background-color: rgb(72, 67, 67);\n"
                "    color: rgb(255, 255, 255);\n"
                "}")
                self.PesanRS.setObjectName("PesanRS")
                self.Pesanan = QtWidgets.QPushButton(self.Sidebar)
                self.Pesanan.setGeometry(QtCore.QRect(20, 320, 171, 51))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.Pesanan.setFont(font)
                self.Pesanan.setStyleSheet("QPushButton{\n"
                "    background-color: rgb(72, 67, 67);\n"
                "    color: rgb(255, 255, 255);\n"
                "}")
                self.Pesanan.setObjectName("Pesanan")
                self.Home = QtWidgets.QPushButton(self.Sidebar)
                self.Home.setGeometry(QtCore.QRect(20, 110, 171, 51))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.Home.setFont(font)
                self.Home.setStyleSheet("QPushButton{\n"
                "    background-color: rgb(72, 67, 67);\n"
                "    color: rgb(255, 255, 255);\n"
                "}")
                self.Home.setObjectName("Home")
                self.Logout = QtWidgets.QPushButton(self.Sidebar)
                self.Logout.setGeometry(QtCore.QRect(20, 520, 171, 51))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.Logout.setFont(font)
                self.Logout.setStyleSheet("QPushButton{\n"
                "    background-color: rgb(72, 67, 67);\n"
                "    color: rgb(255, 255, 255);\n"
                "}")
                self.KlienHomeWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(KlienHomeWindow)
                self.statusbar.setObjectName("statusbar")
                self.KlienHomeWindow.setStatusBar(self.statusbar)

                # Melakukan setup SQL
                self.setupSql()

                # Mendapatkan semua data
                self.refreshAllValue()
                
                # Connect button navigator
                self.Logout.clicked.connect(self.logout)

                self.retranslateUi(KlienHomeWindow)
                QtCore.QMetaObject.connectSlotsByName(KlienHomeWindow)

        def retranslateUi(self, KlienHomeWindow):
                _translate = QtCore.QCoreApplication.translate
                KlienHomeWindow.setWindowTitle(_translate("KlienHomeWindow", "KlienHomeWindow"))
                Nama_Admin = get_username(self.cursor,self.DB_NAME,self.ID_Pengguna)
                self.Nama_Admin.setText(_translate("KlienHomeWindow", "Welcome "+Nama_Admin[1]))
                self.header_tambah.setText(_translate("KlienHomeWindow", "LAPORAN HARIAN COVID-19"))
                self.label_positif.setText(_translate("KlienHomeWindow", "Kasus Positif"))
                self.label_sembuh.setText(_translate("KlienHomeWindow", "Pasien Sembuh"))
                self.label_meninggal.setText(_translate("KlienHomeWindow", "Pasien Meninggal"))
                self.SuhuHarian.setText(_translate("KlienHomeWindow", "Suhu Harian"))
                self.label.setText(_translate("KlienHomeWindow", "CoverMe"))
                self.PesanRS.setText(_translate("KlienHomeWindow", "Pesan RS"))
                self.Pesanan.setText(_translate("KlienHomeWindow", "Pesanan"))
                self.Home.setText(_translate("KlienHomeWindow", "Home"))
                self.Logout.setText(_translate("MainWindow", "Logout"))

        def setupSql(self):
		# Melakukan setup koneksi SQL
                config = {
                        "user": "root",
                        "password": "root",
                        "host": "localhost",
                        "port" : "3307"
                }
                self.DB_NAME = 'Cover_Me'
                self.db = mysql.connector.connect(**config)
                self.cursor = self.db.cursor()


        def refreshAllValue(self):
                self.label_kasus_positif.setText(str(get_kasus_positif(self.cursor, self.DB_NAME)[1][0][0]))
                self.label_pasien_sembuh.setText(str(get_pasien_sembuh(self.cursor, self.DB_NAME)[1][0][0]))
                self.label_pasien_meninggal.setText(str(get_pasien_meninggal(self.cursor, self.DB_NAME)[1][0][0]))

        def logout(self):
                # Melakukan logout
                from ui_login import Ui_LoginWindow
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_LoginWindow()
                self.ui.setupUi(self.window)
                self.window.show()
                self.KlienHomeWindow.close()
                print("Logout")
                return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KlienHomeWindow = QtWidgets.QMainWindow()
    ui = Ui_KlienHomeWindow()
    ui.setupUi(KlienHomeWindow)
    KlienHomeWindow.show()
    sys.exit(app.exec_())
