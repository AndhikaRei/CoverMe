# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RS_Admin.ui'
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
from Init_DBData import *
from datetime import date

class UI_RSAdminWindow(object):
    def setupUi(self, RSAdminWindow, ID_Pengguna=1):
        self.RSAdminWindow = RSAdminWindow
        self.RSAdminWindow.setObjectName("RSAdminWindow")
        self.RSAdminWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(RSAdminWindow)
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
"color: rgb(80, 80, 80);\n"
"border-bottom-width:1px;")
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
        self.button_laporan.setStyleSheet("Text-align:left;\n"
"background-color: rgb(251, 242, 215);\n"
"color: rgb(150, 150, 150);")
        self.button_laporan.setFlat(True)
        self.button_laporan.setObjectName("button_laporan")
        self.icon_laporan = QtWidgets.QLabel(self.centralwidget)
        self.icon_laporan.setGeometry(QtCore.QRect(20, 233, 20, 20))
        self.icon_laporan.setText("")
        self.icon_laporan.setPixmap(QtGui.QPixmap("../img/laporan-gray.png"))
        self.icon_laporan.setScaledContents(True)
        self.icon_laporan.setObjectName("icon_laporan")
        self.icon_rs = QtWidgets.QLabel(self.centralwidget)
        self.icon_rs.setGeometry(QtCore.QRect(20, 263, 20, 20))
        self.icon_rs.setText("")
        self.icon_rs.setPixmap(QtGui.QPixmap("../img/hospital-white.png"))
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
        self.button_rs.setStyleSheet("background-color: rgb(218, 114, 60);\n"
"color: rgb(255, 255, 255);\n"
"Text-align:left;")
        self.button_rs.setFlat(False)
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
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(260, 120, 431, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formDataRS = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formDataRS.setContentsMargins(0, 0, 0, 0)
        self.formDataRS.setObjectName("formDataRS")
        self.label_nama = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_nama.setFont(font)
        self.label_nama.setObjectName("label_nama")
        self.formDataRS.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nama)
        self.label_harga = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
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
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_kapasitas.setFont(font)
        self.label_kapasitas.setObjectName("label_kapasitas")
        self.formDataRS.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_kapasitas)
        self.input_kapasitas = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_kapasitas.setFont(font)
        self.input_kapasitas.setObjectName("input_kapasitas")
        self.formDataRS.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_kapasitas)
        self.input_nama_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_nama_2.setFont(font)
        self.input_nama_2.setObjectName("input_nama_2")
        self.formDataRS.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_nama_2)
        self.header_tambah = QtWidgets.QLabel(self.centralwidget)
        self.header_tambah.setGeometry(QtCore.QRect(260, 80, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.header_tambah.setFont(font)
        self.header_tambah.setStyleSheet("QLabel{\n"
"    color: rgb(145, 9, 30);\n"
"}")
        self.header_tambah.setObjectName("header_tambah")
        self.button_tambah = QtWidgets.QPushButton(self.centralwidget)
        self.button_tambah.setGeometry(QtCore.QRect(720, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_tambah.setFont(font)
        self.button_tambah.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_tambah.setStyleSheet("QPushButton{\n"
"    background-color: rgb(218, 114, 60);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.button_tambah.setObjectName("button_tambah")
        self.header_tambah_2 = QtWidgets.QLabel(self.centralwidget)
        self.header_tambah_2.setGeometry(QtCore.QRect(260, 240, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.header_tambah_2.setFont(font)
        self.header_tambah_2.setStyleSheet("QLabel{\n"
"    color: rgb(145, 9, 30);\n"
"}")
        self.header_tambah_2.setObjectName("header_tambah_2")
        self.tabel_rs = QtWidgets.QTableWidget(self.centralwidget)
        self.tabel_rs.setGeometry(QtCore.QRect(260, 280, 561, 301))
        self.tabel_rs.setColumnCount(5)
        self.tabel_rs.setObjectName("tabel_rs")
        self.tabel_rs.setRowCount(0)
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
        self.tabel_rs.verticalHeader().setVisible(False)
        self.tabel_rs.verticalHeader().setDefaultSectionSize(30)
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
        self.formLayoutWidget.raise_()
        self.header_tambah.raise_()
        self.button_tambah.raise_()
        self.header_tambah_2.raise_()
        self.tabel_rs.raise_()
        RSAdminWindow.setCentralWidget(self.centralwidget)

        # Fungsionalitas tambahan
        # Inisialisasi ID Pengguna
        self.ID_Pengguna = ID_Pengguna

        # Melakukan setup SQL
        self.setupSql()

        # Ketika tombol tambah data diklik
        self.button_tambah.clicked.connect(self.submitData)
        self.button_laporan.clicked.connect(self.to_update_laporan)
        self.button_home.clicked.connect(self.to_Admin_Home)
        self.button_pesanan.clicked.connect(self.to_Admin_Pesanan)
        self.button_logout.clicked.connect(self.logout)

        # Load Table dari database
        self.loadTable()

        # Menulis text dari GUI
        self.retranslateUi(self.RSAdminWindow)
        QtCore.QMetaObject.connectSlotsByName(self.RSAdminWindow)



    def retranslateUi(self, RSAdminWindow):
        _translate = QtCore.QCoreApplication.translate
        RSAdminWindow.setWindowTitle(_translate("RSAdminWindow", "RSAdminWindow"))
        self.topbar.setText(_translate("RSAdminWindow", "     Rumah Sakit"))
        today = date.today()
        d2 = today.strftime("%d %B %Y")
        self.label_date.setText(_translate("RSAdminWindow", d2))
        self.button_home.setText(_translate("RSAdminWindow", "              Home"))
        self.button_laporan.setText(_translate("RSAdminWindow", "              Laporan Harian"))
        self.button_rs.setText(_translate("RSAdminWindow", "              Rumah Sakit"))
        self.button_pesanan.setText(_translate("RSAdminWindow", "              Daftar Pesanan"))
        self.button_logout.setText(_translate("RSAdminWindow", "              Logout"))
        Nama_User = get_nama(self.cursor,self.DB_NAME,self.ID_Pengguna)
        self.label.setText(_translate("RSAdminWindow", Nama_User[1]))
        Email_User = get_email(self.cursor,self.DB_NAME,self.ID_Pengguna)
        self.label_email.setText(_translate("RSAdminWindow", Email_User[1]))
        self.label_nama.setText(_translate("RSAdminWindow", "Nama Rumah Sakit"))
        self.label_harga.setText(_translate("RSAdminWindow", "Harga Rumah Sakit"))
        self.label_kapasitas.setText(_translate("RSAdminWindow", "Kapasitas"))
        self.header_tambah.setText(_translate("RSAdminWindow", "Tambah Data Rumah Sakit"))
        self.button_tambah.setText(_translate("RSAdminWindow", "Simpan"))
        self.header_tambah_2.setText(_translate("RSAdminWindow", "Data Rumah Sakit"))
        item = self.tabel_rs.horizontalHeaderItem(0)
        item.setText(_translate("RSAdminWindow", "ID"))
        item = self.tabel_rs.horizontalHeaderItem(1)
        item.setText(_translate("RSAdminWindow", "Nama Rumah Sakit"))
        item = self.tabel_rs.horizontalHeaderItem(2)
        item.setText(_translate("RSAdminWindow", "Harga Rumah Sakit"))
        item = self.tabel_rs.horizontalHeaderItem(3)
        item.setText(_translate("RSAdminWindow", "Kapasitas"))
        item = self.tabel_rs.horizontalHeaderItem(4)
        item.setText(_translate("RSAdminWindow", "Jumlah Pasien"))

    def setupSql(self):
        # Melakukan setup koneksi SQL
        self.DB_NAME = get_DB_NAME()
        self.db = mysql.connector.connect(**get_config())
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
        from Login_User import Ui_LoginScreen
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self.window)
        self.window.show()
        self.RSAdminWindow.close()
        print("Logout")
        return

    def to_update_laporan(self):
        # Navigate to update laporan page
        from Laporan_Admin import Ui_LaporanAdminWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LaporanAdminWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.RSAdminWindow.close()
        print("Update Laporan")
        return

    def to_Admin_Home(self):
        # Navigate to update laporan page
        from Home_Admin import Ui_HomeAdminWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeAdminWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.RSAdminWindow.close()
        print("Admin_Home ")
        return

    def to_Admin_Pesanan(self):
        # Navigate to update laporan page
        from Pesanan_Admin import Ui_PesananAdminWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PesananAdminWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.RSAdminWindow.close()
        print("Admin_Pesanan ")
        return

if __name__ == "__main__":
    import sys
    InitDB()
    app = QtWidgets.QApplication(sys.argv)
    RSAdminWindow = QtWidgets.QMainWindow()
    ui = UI_RSAdminWindow()
    ui.setupUi(RSAdminWindow)
    RSAdminWindow.show()
    sys.exit(app.exec_())
