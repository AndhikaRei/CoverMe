# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Klien_Suhu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from suhu_harian import *
from update_laporan import *
from autentikasi import *
from Klien_PesanRS import *
from Init_DBData import *

class Ui_SuhuHarianWindow(object):
        def setupUi(self, SuhuHarianWindow, ID_Pengguna=2):
                self.ID_Pengguna = ID_Pengguna
                self.SuhuHarianWindow = SuhuHarianWindow
                self.SuhuHarianWindow.setObjectName("SuhuHarianWindow")
                self.SuhuHarianWindow.setEnabled(True)
                self.SuhuHarianWindow.resize(900, 600)
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(11)
                self.SuhuHarianWindow.setFont(font)
                self.centralwidget = QtWidgets.QWidget(SuhuHarianWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.Nama_Admin = QtWidgets.QLabel(self.centralwidget)
                self.Nama_Admin.setGeometry(QtCore.QRect(650, 0, 251, 61))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.Nama_Admin.setFont(font)
                self.Nama_Admin.setObjectName("Nama_Admin")
                self.header_tambah = QtWidgets.QLabel(self.centralwidget)
                self.header_tambah.setGeometry(QtCore.QRect(270, 400, 351, 31))
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.header_tambah.setFont(font)
                self.header_tambah.setStyleSheet("QLabel{\n"
                "    color: rgb(0, 0, 0);\n"
                "}")
                self.header_tambah.setObjectName("header_tambah")
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
                self.Logout.setObjectName("Logout")
                self.edit_positif = QtWidgets.QLineEdit(self.centralwidget)
                self.edit_positif.setEnabled(True)
                self.edit_positif.setGeometry(QtCore.QRect(270, 440, 461, 21))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.edit_positif.setFont(font)
                self.edit_positif.setStyleSheet("border-style: solid;\n"
                "border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.edit_positif.setText("")
                self.edit_positif.setAlignment(QtCore.Qt.AlignCenter)
                self.edit_positif.setObjectName("edit_positif")
                self.button_cek_suhu = QtWidgets.QPushButton(self.centralwidget)
                self.button_cek_suhu.setEnabled(True)
                self.button_cek_suhu.setGeometry(QtCore.QRect(750, 440, 95, 21))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(10)
                self.button_cek_suhu.setFont(font)
                self.button_cek_suhu.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                "color: rgb(255, 255, 255);")
                self.button_cek_suhu.setObjectName("button_cek_suhu")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setEnabled(False)
                self.label_2.setGeometry(QtCore.QRect(270, 90, 575, 280))
                self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setEnabled(False)
                self.label_3.setGeometry(QtCore.QRect(280, 140, 331, 5))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
                self.label_3.setText("")
                self.label_3.setObjectName("label_3")
                self.gambar_bahaya = QtWidgets.QLabel(self.centralwidget)
                self.gambar_bahaya.setEnabled(True)
                self.gambar_bahaya.setGeometry(QtCore.QRect(620, 140, 215, 221))
                self.gambar_bahaya.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.gambar_bahaya.setText("")
                self.gambar_bahaya.setPixmap(QtGui.QPixmap("../img/sakit.jpg"))
                self.gambar_bahaya.setScaledContents(True)
                self.gambar_bahaya.setWordWrap(False)
                self.gambar_bahaya.setObjectName("gambar_bahaya")
                self.gambar_aman = QtWidgets.QLabel(self.centralwidget)
                self.gambar_aman.setEnabled(True)
                self.gambar_aman.setGeometry(QtCore.QRect(620, 140, 215, 221))
                self.gambar_aman.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                "border-width:1px;\n"
                "border-style: solid;")
                self.gambar_aman.setText("")
                self.gambar_aman.setPixmap(QtGui.QPixmap("../img/sehat.jpg"))
                self.gambar_aman.setScaledContents(True)
                self.gambar_aman.setWordWrap(False)
                self.gambar_aman.setObjectName("gambar_aman")
                self.text_bahaya = QtWidgets.QLabel(self.centralwidget)
                self.text_bahaya.setGeometry(QtCore.QRect(280, 110, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.text_bahaya.setFont(font)
                self.text_bahaya.setStyleSheet("QLabel{\n"
                "    color: rgb(255, 0, 0);\n"
                "}")
                self.text_bahaya.setObjectName("text_bahaya")
                self.text_aman = QtWidgets.QLabel(self.centralwidget)
                self.text_aman.setGeometry(QtCore.QRect(280, 110, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.text_aman.setFont(font)
                self.text_aman.setStyleSheet("QLabel{\n"
                "    color: rgb(0, 255, 0);\n"
                "}")
                self.text_aman.setObjectName("text_aman")
                self.pesan_bahaya = QtWidgets.QTextBrowser(self.centralwidget)
                self.pesan_bahaya.setGeometry(QtCore.QRect(280, 150, 331, 211))
                self.pesan_bahaya.setObjectName("pesan_bahaya")
                self.pesan_aman = QtWidgets.QTextBrowser(self.centralwidget)
                self.pesan_aman.setGeometry(QtCore.QRect(280, 150, 331, 211))
                self.pesan_aman.setObjectName("pesan_aman")
                self.label_2.raise_()
                self.Nama_Admin.raise_()
                self.header_tambah.raise_()
                self.Sidebar.raise_()
                self.edit_positif.raise_()
                self.button_cek_suhu.raise_()
                self.label_3.raise_()
                self.gambar_bahaya.raise_()
                self.gambar_aman.raise_()
                self.text_bahaya.raise_()
                self.text_aman.raise_()
                self.pesan_bahaya.raise_()
                self.pesan_aman.raise_()
                self.SuhuHarianWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(SuhuHarianWindow)
                self.statusbar.setObjectName("statusbar")
                self.SuhuHarianWindow.setStatusBar(self.statusbar)

                # Melakukan setup SQL
                self.setupSql()

                # init ui
                self.refreshLatestSuhu()

                # connect button
                self.button_cek_suhu.clicked.connect(self.cekSuhu)
                self.Logout.clicked.connect(self.logout)
                self.PesanRS.clicked.connect(self.to_pesan_rs)
                self.Home.clicked.connect(self.toKlienHome)
                self.Pesanan.clicked.connect(self.to_Klien_Pesanan)

                self.retranslateUi(SuhuHarianWindow)
                QtCore.QMetaObject.connectSlotsByName(SuhuHarianWindow)

        def retranslateUi(self, SuhuHarianWindow):
                _translate = QtCore.QCoreApplication.translate
                SuhuHarianWindow.setWindowTitle(_translate("SuhuHarianWindow", "SuhuHarianWindow"))
                Nama_Admin = get_username(self.cursor,self.DB_NAME,self.ID_Pengguna)
                self.Nama_Admin.setText(_translate("KlienHomeWindow", "Welcome "+Nama_Admin[1]))
                self.header_tambah.setText(_translate("SuhuHarianWindow", "Masukkan Suhu Tubuh Harian"))
                self.SuhuHarian.setText(_translate("SuhuHarianWindow", "Suhu Harian"))
                self.label.setText(_translate("SuhuHarianWindow", "CoverMe"))
                self.PesanRS.setText(_translate("SuhuHarianWindow", "Pesan RS"))
                self.Pesanan.setText(_translate("SuhuHarianWindow", "Pesanan"))
                self.Home.setText(_translate("SuhuHarianWindow", "Home"))
                self.Logout.setText(_translate("SuhuHarianWindow", "Logout"))
                self.button_cek_suhu.setText(_translate("SuhuHarianWindow", "Cek"))
                self.text_bahaya.setText(_translate("SuhuHarianWindow", "BAHAYA"))
                self.text_aman.setText(_translate("SuhuHarianWindow", "AMAN"))
                self.pesan_bahaya.setHtml(_translate("SuhuHarianWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Roboto\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Suhu Anda Beranda dalam Rentang Bahaya</p>\n"
                "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Apabila Anda tidak merasakan gejala COVID-19 seperti sesak nafas dan nyeri dada, lakukan isolasi mandiri di rumah Anda hingga suhu Anda kembali ke Rentang Aman.</p>\n"
                "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Apabila Anda merasakan gejala COVID-19, segera melakukan pemesanan rumah sakit. Pemesanan rumah sakit dapat dilakukan melalui menu Pesan RS.</p></body></html>"))
                self.pesan_aman.setHtml(_translate("SuhuHarianWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Roboto\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Suhu Anda Beranda dalam Rentang Aman</p>\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lakukan hal berikut untuk mencegah penularan COVID-19:</p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Mencuci tangan dengan benar</p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Menggunakan masker</p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Menjaga daya tahan tubuh</p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. Menerapkan <span style=\" font-style:italic;\">physical distancing</span> dan isolasi mandiri</p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. Membersihkan rumah dan melakukan disinfeksi secara rutin</p></body></html>"))

        def setupSql(self):
		# Melakukan setup koneksi SQL
                self.DB_NAME = get_DB_NAME()
                self.db = mysql.connector.connect(**get_config())
                self.cursor = self.db.cursor()

        def hideAman(self):
                self.text_aman.setVisible(False)
                self.pesan_aman.setVisible(False)
                self.gambar_aman.setVisible(False)

        def showAman(self):
                self.text_aman.setVisible(True)
                self.pesan_aman.setVisible(True)
                self.gambar_aman.setVisible(True)
        
        def hideBahaya(self):
                self.text_bahaya.setVisible(False)
                self.pesan_bahaya.setVisible(False)
                self.gambar_bahaya.setVisible(False)

        def showBahaya(self):
                self.text_bahaya.setVisible(True)
                self.pesan_bahaya.setVisible(True)
                self.gambar_bahaya.setVisible(True)

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
        
        def refreshLatestSuhu(self):
                result = get_latest_keadaan_by_id(self.cursor, self.DB_NAME, self.ID_Pengguna)
                if(result=="Bahaya"):
                        self.hideAman()
                        self.showBahaya()
                else:
                        self.hideBahaya()
                        self.showAman()

        def cekSuhu(self):
                new = self.edit_positif.text()
                result = set_riwayat_by_id(self.db, self.cursor, self.DB_NAME, self.ID_Pengguna, new)
                if(result[0]==0):
                        self.showAlert(result[1])
                        self.edit_positif.setText("")
                else:
                        self.showSucc(result[1])
                        self.edit_positif.setText("")
                self.refreshLatestSuhu()

        def logout(self):
                # Melakukan logout
                from ui_login import Ui_LoginWindow
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_LoginWindow()
                self.ui.setupUi(self.window)
                self.window.show()
                self.SuhuHarianWindow.close()
                print("Logout")
                return

        def to_pesan_rs(self):
                # Navigate to update laporan page
                from Klien_PesanRS import Ui_PesanRSWindow
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_PesanRSWindow()
                self.ui.setupUi(self.window, self.ID_Pengguna)
                self.window.show()
                self.SuhuHarianWindow.close()
                print("Pesan RS")
                return

        def toKlienHome(self,ID_Pengguna):
                # Navigate to klien home page
                from Klien_Home import Ui_KlienHomeWindow
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_KlienHomeWindow()
                self.ui.setupUi(self.window,self.ID_Pengguna)
                self.window.show()
                self.SuhuHarianWindow.close()
                print("Klien_Home")

        def to_Klien_Pesanan(self):
                # Navigate to update laporan page
                from Klien_Pesanan import Ui_KlienPesananWindow
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_KlienPesananWindow()
                self.ui.setupUi(self.window, self.ID_Pengguna)
                self.window.show()
                self.SuhuHarianWindow.close()
                print("Klien_Pesanan ")
                return

if __name__ == "__main__":
    import sys
    InitDB()
    app = QtWidgets.QApplication(sys.argv)
    SuhuHarianWindow = QtWidgets.QMainWindow()
    ui = Ui_SuhuHarianWindow()
    ui.setupUi(SuhuHarianWindow)
    SuhuHarianWindow.show()
    sys.exit(app.exec_())
