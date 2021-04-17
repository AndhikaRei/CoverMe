# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Klien_Pesanan.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from autentikasi import get_username
from PyQt5 import QtCore, QtGui, QtWidgets
from Init_DBData import *
from pesanan import *
from rumah_sakit import *

class Ui_KlienPesananWindow(object):
	def setupUi(self, KlienPesananWindow, ID_Pengguna=1):
		self.KlienPesananWindow = KlienPesananWindow
		KlienPesananWindow.setObjectName("KlienPesananWindow")
		KlienPesananWindow.resize(900, 600)
		KlienPesananWindow.setStyleSheet("")
		self.centralwidget = QtWidgets.QWidget(KlienPesananWindow)
		self.centralwidget.setObjectName("centralwidget")
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
		font.setPointSize(22)
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
		self.Logout.setObjectName("Logout")
		self.header = QtWidgets.QLabel(self.centralwidget)
		self.header.setGeometry(QtCore.QRect(410, 70, 291, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.header.setFont(font)
		self.header.setStyleSheet("QLabel{\n"
"    color: rgb(0, 0, 0);\n"
"}")
		self.header.setObjectName("header")
		self.Nama_Admin_2 = QtWidgets.QLabel(self.centralwidget)
		self.Nama_Admin_2.setGeometry(QtCore.QRect(600, 0, 291, 61))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.Nama_Admin_2.setFont(font)
		self.Nama_Admin_2.setObjectName("Nama_Admin_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(210, 170, 301, 281))
		self.label_3.setText("")
		self.label_3.setPixmap(QtGui.QPixmap("../img/natsuho.jpg"))
		self.label_3.setScaledContents(True)
		self.label_3.setObjectName("label_3")
		self.nama_RS = QtWidgets.QLabel(self.centralwidget)
		self.nama_RS.setGeometry(QtCore.QRect(580, 170, 251, 61))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.nama_RS.setFont(font)
		self.nama_RS.setAlignment(QtCore.Qt.AlignCenter)
		self.nama_RS.setObjectName("nama_RS")
		self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.textEdit.setGeometry(QtCore.QRect(550, 260, 151, 61))
		font = QtGui.QFont()
		font.setFamily("Roboto Mono")
		font.setPointSize(10)
		self.textEdit.setFont(font)
		self.textEdit.setStyleSheet("border: black solid 0px;\n"
"background-color: rgb(240, 240, 240);")
		self.textEdit.setObjectName("textEdit")
		self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
		self.textEdit_2.setGeometry(QtCore.QRect(700, 260, 161, 61))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.textEdit_2.setFont(font)
		self.textEdit_2.setStyleSheet("border: black solid 0px;\n"
"background-color: rgb(240, 240, 240);")
		self.textEdit_2.setObjectName("textEdit_2")
		self.respon_klien = QtWidgets.QPushButton(self.centralwidget)
		self.respon_klien.setGeometry(QtCore.QRect(580, 390, 251, 61))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.respon_klien.setFont(font)
		self.respon_klien.setStyleSheet("QPushButton{\n"
"    background-color: rgb(3, 21, 121);\n"
"    color: rgb(255, 255, 255);\n"
"}")
		self.respon_klien.setObjectName("respon_klien")
		self.status_pesanan = QtWidgets.QPushButton(self.centralwidget)
		self.status_pesanan.setGeometry(QtCore.QRect(620, 350, 171, 41))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(12)
		self.status_pesanan.setFont(font)
		self.status_pesanan.setStyleSheet("QPushButton{\n"
"    background-color: green;\n"
"    color: rgb(255, 255, 255);\n"
"}")
		self.status_pesanan.setObjectName("status_pesanan")
		KlienPesananWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(KlienPesananWindow)
		self.statusbar.setObjectName("statusbar")
		KlienPesananWindow.setStatusBar(self.statusbar)

		self.setupSql()

		# Set ID_Pengguna
		self.ID_Pengguna = ID_Pengguna
		self.ID_Pesanan = -1

		# Connect button navigator
		self.Logout.clicked.connect(self.logout)
		self.PesanRS.clicked.connect(self.to_pesan_rs)
		self.Home.clicked.connect(self.toKlienHome)
		self.SuhuHarian.clicked.connect(self.to_suhu_harian)


		self.respon_klien.clicked.connect(self.ubah_status_pesanan)

		self.retranslateUi(KlienPesananWindow)
		QtCore.QMetaObject.connectSlotsByName(KlienPesananWindow)

	def retranslateUi(self, KlienPesananWindow):
		_translate = QtCore.QCoreApplication.translate
		KlienPesananWindow.setWindowTitle(_translate("KlienPesananWindow", "KlienPesananWindow"))
		self.SuhuHarian.setText(_translate("KlienPesananWindow", "Suhu Harian"))
		self.label.setText(_translate("KlienPesananWindow", "CoverMe"))
		self.PesanRS.setText(_translate("KlienPesananWindow", "Pesan RS"))
		self.Pesanan.setText(_translate("KlienPesananWindow", "Pesanan"))
		self.Home.setText(_translate("KlienPesananWindow", "Home"))
		self.Logout.setText(_translate("KlienPesananWindow", "Logout"))
		username_Pengguna = get_username(self.cursor,self.DB_NAME,self.ID_Pengguna)[1]
		self.Nama_Admin_2.setText(_translate("PesanRSWindow", "Welcome  "+username_Pengguna))

		self.result = get_pesanan_ongoing(self.cursor, self.DB_NAME, self.ID_Pengguna)[1]
		print(self.result)
        

		if(len(self.result) > 0):
			self.ID_Pesanan = self.result[0][4]	
			self.showAll()
			self.header.setText(_translate("KlienPesananWindow", "Pesanan Saat Ini"))
			self.nama_RS.setText(_translate("KlienPesananWindow", self.result[0][0]))
			self.textEdit.setHtml(_translate("KlienPesananWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Mono\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Tanggal pesan :</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Harga :</span></p></body></html>"))
			self.textEdit_2.setHtml(_translate("KlienPesananWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">"+str(self.result[0][2])+"</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">Rp "+str(self.result[0][1])+"</span></p></body></html>"))
			if (self.result[0][3] == -1):
				self.respon_klien.setText(_translate("KlienPesananWindow", "Sudahi Pesanan"))
				self.status_pesanan.setText(_translate("KlienPesananWindow", "Status: Rejected"))
				self.status_pesanan.setStyleSheet("QPushButton{\n"
"    background-color: red;\n"
"    color: rgb(255, 255, 255);\n"
"}")
			elif (self.result[0][3] == 0):
				self.respon_klien.setText(_translate("KlienPesananWindow", "Batalkan Pesanan"))
				self.status_pesanan.setText(_translate("KlienPesananWindow", "Status: Pending"))
				self.status_pesanan.setStyleSheet("QPushButton{\n"
"    background-color: grey;\n"
"    color: rgb(255, 255, 255);\n"
"}")
			elif (self.result[0][3] == 1):
				self.respon_klien.setText(_translate("KlienPesananWindow", "Bayar (Selesai Rawat)"))
				self.status_pesanan.setText(_translate("KlienPesananWindow", "Status: Accepted"))
				self.status_pesanan.setStyleSheet("QPushButton{\n"
"    background-color: green;\n"
"    color: rgb(255, 255, 255);\n"
"}")
		else:
			self.header.setText(_translate("KlienPesananWindow", "Tidak ada Pesanan Saat Ini"))
			self.hideAll()

	def setupSql(self):
		# Melakukan setup koneksi SQL
		self.DB_NAME = get_DB_NAME()
		self.db = mysql.connector.connect(**get_config())
		self.cursor = self.db.cursor()

	def hideAll(self):
		self.label_3.setVisible(False)
		self.status_pesanan.setVisible(False)
		self.respon_klien.setVisible(False)
		self.nama_RS.setVisible(False)
		self.textEdit.setVisible(False)
		self.textEdit_2.setVisible(False)
	def showAll(self):
		self.label_3.setVisible(True)
		self.status_pesanan.setVisible(True)
		self.respon_klien.setVisible(True)
		self.nama_RS.setVisible(True)
		self.textEdit.setVisible(True)
		self.textEdit_2.setVisible(True)

	def ubah_status_pesanan(self):
		respon = ubah_status(self.db,self.cursor,self.DB_NAME,self.ID_Pesanan,-2)
		print(respon)
		if (self.result[0][3] == 1):
			kurangi_pasien(self.db,self.cursor,self.DB_NAME,self.result[0][0])
		self.retranslateUi(self.KlienPesananWindow)

	def logout(self):
		# Melakukan fungsionalitas logout
		from ui_login import Ui_LoginWindow
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_LoginWindow()
		self.ui.setupUi(self.window)
		self.window.show()
		self.KlienPesananWindow.close()
		print("Logout")
		return

	def toKlienHome(self,ID_Pengguna):
		from Klien_Home import Ui_KlienHomeWindow
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_KlienHomeWindow()
		self.ui.setupUi(self.window,self.ID_Pengguna)
		self.window.show()
		self.KlienPesananWindow.close()
		print("Klien_Home")

	def to_pesan_rs(self):
		# Navigate to update laporan page
		from Klien_PesanRS import Ui_PesanRSWindow
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_PesanRSWindow()
		self.ui.setupUi(self.window, self.ID_Pengguna)
		self.window.show()
		self.KlienPesananWindow.close()
		print("Pesan RS")
		return

	def to_suhu_harian(self):
		# Navigate to suhu harian page
		from Klien_Suhu import Ui_SuhuHarianWindow
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_SuhuHarianWindow()
		self.ui.setupUi(self.window, self.ID_Pengguna)
		self.window.show()
		self.KlienPesananWindow.close()
		print("Suhu Harian")
		return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KlienPesananWindow = QtWidgets.QMainWindow()
    ui = Ui_KlienPesananWindow()
    ui.setupUi(KlienPesananWindow)
    KlienPesananWindow.show()
    sys.exit(app.exec_())
