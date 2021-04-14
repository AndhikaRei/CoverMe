# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_RS.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from rumah_sakit import *
import mysql.connector
from autentikasi import *
from ui_login import *
from Admin_Home import *


class Ui_DataRSWindow(object):
	def setupUi(self, DataRSWindow,ID_Pengguna=1):
		# Inisialisasi GUI
		self.DataRSWindow = DataRSWindow
		self.DataRSWindow.setObjectName("DataRSWindow")
		self.DataRSWindow.resize(909, 601)
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		DataRSWindow.setFont(font)
		DataRSWindow.setStyleSheet("QMainWindow{\n"
			"    background-color: rgb(255, 255, 255);\n"
		"}")
		self.widget = QtWidgets.QWidget(self.DataRSWindow)
		self.widget.setObjectName("widget")
		self.Sidebar = QtWidgets.QFrame(self.widget)
		self.Sidebar.setGeometry(QtCore.QRect(0, 0, 211, 591))
		self.Sidebar.setStyleSheet("QFrame{\n"
			"    background-color: rgb(72, 67, 67);\n"
		"}")
		self.Sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.Sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Sidebar.setObjectName("Sidebar")
		self.Laporan_Harian = QtWidgets.QPushButton(self.Sidebar)
		self.Laporan_Harian.setGeometry(QtCore.QRect(20, 180, 171, 51))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.Laporan_Harian.setFont(font)
		self.Laporan_Harian.setStyleSheet("QPushButton{\n"
			"    background-color: rgb(72, 67, 67);\n"
			"    color: rgb(255, 255, 255);\n"
		"}")
		self.Laporan_Harian.setObjectName("Laporan_Harian")
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
		self.RumahSakit = QtWidgets.QPushButton(self.Sidebar)
		self.RumahSakit.setGeometry(QtCore.QRect(20, 250, 171, 51))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.RumahSakit.setFont(font)
		self.RumahSakit.setStyleSheet("QPushButton{\n"
			"    background-color: rgb(72, 67, 67);\n"
			"    color: rgb(255, 255, 255);\n"
		"}")
		self.RumahSakit.setObjectName("RumahSakit")
		self.Daftar_Pesanan = QtWidgets.QPushButton(self.Sidebar)
		self.Daftar_Pesanan.setGeometry(QtCore.QRect(20, 320, 171, 51))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.Daftar_Pesanan.setFont(font)
		self.Daftar_Pesanan.setStyleSheet("QPushButton{\n"
			"    background-color: rgb(72, 67, 67);\n"
			"    color: rgb(255, 255, 255);\n"
		"}")
		self.Daftar_Pesanan.setObjectName("Daftar_Pesanan")
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
		self.Nama_Admin = QtWidgets.QLabel(self.widget)
		self.Nama_Admin.setGeometry(QtCore.QRect(650, 0, 251, 61))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.Nama_Admin.setFont(font)
		self.Nama_Admin.setObjectName("Nama_Admin")
		self.header_tambah = QtWidgets.QLabel(self.widget)
		self.header_tambah.setGeometry(QtCore.QRect(250, 70, 371, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.header_tambah.setFont(font)
		self.header_tambah.setStyleSheet("QLabel{\n"
			"    color: rgb(0, 0, 0);\n"
		"}")
		self.header_tambah.setObjectName("header_tambah")
		self.header_data = QtWidgets.QLabel(self.widget)
		self.header_data.setGeometry(QtCore.QRect(250, 220, 281, 41))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.header_data.setFont(font)
		self.header_data.setStyleSheet("QLabel{\n"
			"    color: rgb(0, 0, 0);\n"
		"}")
		self.header_data.setObjectName("header_data")
		self.button_tambah = QtWidgets.QPushButton(self.widget)
		self.button_tambah.setGeometry(QtCore.QRect(700, 170, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.button_tambah.setFont(font)
		self.button_tambah.setStyleSheet("QPushButton{\n"
			"    background-color: rgb(92, 184, 92);\n"
		"}")
		self.button_tambah.setObjectName("button_tambah")
		self.tabel_rs = QtWidgets.QTableWidget(self.widget)
		self.tabel_rs.setGeometry(QtCore.QRect(250, 270, 611, 301))
		self.tabel_rs.setColumnCount(5)
		self.tabel_rs.setObjectName("tabel_rs")
		self.tabel_rs.setRowCount(0)
		self.tabel_rs.verticalHeader().setVisible(False)
		item = QtWidgets.QTableWidgetItem()
		self.tabel_rs.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabel_rs.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabel_rs.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabel_rs.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabel_rs.setHorizontalHeaderItem(4, item)
		self.tabel_rs.verticalHeader().setDefaultSectionSize(30)
		self.formLayoutWidget = QtWidgets.QWidget(self.widget)
		self.formLayoutWidget.setGeometry(QtCore.QRect(250, 120, 431, 91))
		self.formLayoutWidget.setObjectName("formLayoutWidget")
		self.formDataRS = QtWidgets.QFormLayout(self.formLayoutWidget)
		self.formDataRS.setContentsMargins(0, 0, 0, 0)
		self.formDataRS.setObjectName("formDataRS")
		self.label_nama = QtWidgets.QLabel(self.formLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_nama.setFont(font)
		self.label_nama.setObjectName("label_nama")
		self.formDataRS.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nama)
		self.input_nama_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.input_nama_2.setFont(font)
		self.input_nama_2.setObjectName("input_nama_2")
		self.formDataRS.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_nama_2)
		self.label_harga = QtWidgets.QLabel(self.formLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_harga.setFont(font)
		self.label_harga.setObjectName("label_harga")
		self.formDataRS.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_harga)
		self.input_harga = QtWidgets.QLineEdit(self.formLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.input_harga.setFont(font)
		self.input_harga.setObjectName("input_harga")
		self.formDataRS.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_harga)
		self.label_kapasitas = QtWidgets.QLabel(self.formLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_kapasitas.setFont(font)
		self.label_kapasitas.setObjectName("label_kapasitas")
		self.formDataRS.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_kapasitas)
		self.input_kapasitas = QtWidgets.QLineEdit(self.formLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.input_kapasitas.setFont(font)
		self.input_kapasitas.setObjectName("input_kapasitas")
		self.formDataRS.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_kapasitas)
		self.DataRSWindow.setCentralWidget(self.widget)
		self.Logout.clicked.connect(self.logout)

		# Fungsionalitas tambahan
		# Inisialisasi ID Pengguna
		self.ID_Pengguna = ID_Pengguna

		# Melakukan setup SQL
		self.setupSql()

		# Ketika tombol tambah data diklik
		self.button_tambah.clicked.connect(self.submitData)
		self.Laporan_Harian.clicked.connect(self.to_update_laporan)
		self.Home.clicked.connect(self.to_Admin_Home)


		# Load Table dari database
		self.loadTable()
		
		# Menulis text dari GUI
		self.retranslateUi(self.DataRSWindow)
		QtCore.QMetaObject.connectSlotsByName(self.DataRSWindow)
	
	
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

	def loadTable(self):
		# Menset ukuran tabel data rs di GUI 
		self.tabel_rs.setColumnWidth(0,50)
		self.tabel_rs.setColumnWidth(1,215)
		self.tabel_rs.setColumnWidth(2,140)
		self.tabel_rs.setColumnWidth(3,102)
		self.tabel_rs.setColumnWidth(4,102)

		# Load isi tabel dari database untuk admin
		res = get_rs_admin(self.cursor,self.DB_NAME)
		if (res[0]==1):
			data = res[1]
			self.tabel_rs.setRowCount(len(data))
			idx = 0
			# Memasukkan data hasil load dari database satu persatu
			for row in data:
				print(row)
				self.tabel_rs.setItem(idx, 0, QtWidgets.QTableWidgetItem(str(row[0])))
				self.tabel_rs.setItem(idx, 1, QtWidgets.QTableWidgetItem(row[1]))
				self.tabel_rs.setItem(idx, 2, QtWidgets.QTableWidgetItem(str(row[2])))
				self.tabel_rs.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(row[3])))
				self.tabel_rs.setItem(idx, 4, QtWidgets.QTableWidgetItem(str(row[4])))
				idx = idx + 1
		else: 
			self.showAlert(res[1])

	def submitData(self):
		# Menambah data yang dimasukkan di dalam form ke database 
		# Apabila saat dicek ternyata data tidak valid maka data tidak akan di tambah ke database
		val = (self.input_nama_2.text(), self.input_harga.text(), self.input_kapasitas.text())
		res= add_new_rs(self.db,self.cursor,self.DB_NAME,val)
		if (res[0]==1):
			self.input_nama_2.setText("")
			self.input_kapasitas.setText("")
			self.input_harga.setText("")
			self.loadTable()
			self.showSucc("Data berhasil ditambahkan")
		else:
			self.showAlert(res[1])

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
		from ui_login import Ui_LoginWindow
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_LoginWindow()
		self.ui.setupUi(self.window)
		self.window.show()
		self.DataRSWindow.close()
		print("Logout")
		return

	def to_update_laporan(self):
		# Navigate to update laporan page
		from Admin_UpdateLaporan import Ui_UpdateLaporanWindow
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_UpdateLaporanWindow()
		self.ui.setupUi(self.window, self.ID_Pengguna)
		self.window.show()
		self.DataRSWindow.close()
		print("Update Laporan")
		return
	
	def to_Admin_Home(self):
        # Navigate to update laporan page
		from Admin_Home import Ui_AdminHomeWindow
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_AdminHomeWindow()
		self.ui.setupUi(self.window, self.ID_Pengguna)
		self.window.show()
		self.DataRSWindow.close()
		print("Admin_Home ")
		return

	def retranslateUi(self, DataRSWindow):
		# Menulis ulang text di GUI
		_translate = QtCore.QCoreApplication.translate
		self.DataRSWindow.setWindowTitle(_translate("DataRSWindow", "DataRSWindow"))
		self.Laporan_Harian.setText(_translate("DataRSWindow", "Laporan Harian"))
		self.label.setText(_translate("DataRSWindow", "CoverMe"))
		self.RumahSakit.setText(_translate("DataRSWindow", "Rumah Sakit"))
		self.Daftar_Pesanan.setText(_translate("DataRSWindow", "Daftar Pesanan"))
		self.Home.setText(_translate("DataRSWindow", "Home"))
		self.Logout.setText(_translate("PesanRSWindow", "Logout"))
		username_Admin = get_username(self.cursor,self.DB_NAME,self.ID_Pengguna)[1]
		self.Nama_Admin.setText(_translate("DataRSWindow", "Welcome " + username_Admin))
		self.header_tambah.setText(_translate("DataRSWindow", "Tambah Data Rumah Sakit"))
		self.header_data.setText(_translate("DataRSWindow", "Data Rumah Sakit"))
		self.button_tambah.setText(_translate("DataRSWindow", "+ Tambah Data"))
		item = self.tabel_rs.horizontalHeaderItem(0)
		item.setText(_translate("DataRSWindow", "ID"))
		item = self.tabel_rs.horizontalHeaderItem(1)
		item.setText(_translate("DataRSWindow", "Nama_Rs"))
		item = self.tabel_rs.horizontalHeaderItem(2)
		item.setText(_translate("DataRSWindow", "Harga Rumah Sakit"))
		item = self.tabel_rs.horizontalHeaderItem(3)
		item.setText(_translate("DataRSWindow", "Kapasitas"))
		item = self.tabel_rs.horizontalHeaderItem(4)
		item.setText(_translate("DataRSWindow", "Jumlah Pasien"))
		self.label_nama.setText(_translate("DataRSWindow", "Nama Rumah Sakit"))
		self.label_harga.setText(_translate("DataRSWindow", "Harga Rumah Sakit"))
		self.label_kapasitas.setText(_translate("DataRSWindow", "Kapasitas"))
	

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataRSWindow = QtWidgets.QMainWindow()
    ui = Ui_DataRSWindow()
    ui.setupUi(DataRSWindow)
    DataRSWindow.show()
    
    sys.exit(app.exec_())
