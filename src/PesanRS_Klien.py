from PyQt5 import QtCore, QtGui, QtWidgets
from autentikasi import *
from pesanan import *
from rumah_sakit import *
import mysql.connector
from Init_DBData import *
from datetime import date

class Ui_PesanRSKlienWindow(object):
    def setupUi(self, PesanRSKlienWindow, ID_Pengguna=1):
        self.PesanRSKlienWindow = PesanRSKlienWindow
        self.ID_Pengguna = ID_Pengguna
        self.PesanRSKlienWindow.setObjectName("PesanRSKlienWindow")
        self.PesanRSKlienWindow.resize(900, 600)
        self.PesanRSKlienWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(PesanRSKlienWindow)
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
        self.button_suhu = QtWidgets.QPushButton(self.centralwidget)
        self.button_suhu.setGeometry(QtCore.QRect(0, 226, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_suhu.setFont(font)
        self.button_suhu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_suhu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_suhu.setAutoFillBackground(False)
        self.button_suhu.setStyleSheet("Text-align:left;\n"
"background-color: rgb(251, 242, 215);\n"
"color: rgb(150, 150, 150);")
        self.button_suhu.setFlat(True)
        self.button_suhu.setObjectName("button_suhu")
        self.icon_suhu = QtWidgets.QLabel(self.centralwidget)
        self.icon_suhu.setGeometry(QtCore.QRect(20, 233, 20, 20))
        self.icon_suhu.setText("")
        self.icon_suhu.setPixmap(QtGui.QPixmap("../img/termo-gray.png"))
        self.icon_suhu.setScaledContents(True)
        self.icon_suhu.setObjectName("icon_suhu")
        self.icon_pesan = QtWidgets.QLabel(self.centralwidget)
        self.icon_pesan.setGeometry(QtCore.QRect(20, 263, 20, 20))
        self.icon_pesan.setText("")
        self.icon_pesan.setPixmap(QtGui.QPixmap("../img/order-white.png"))
        self.icon_pesan.setScaledContents(True)
        self.icon_pesan.setObjectName("icon_pesan")
        self.button_pesan = QtWidgets.QPushButton(self.centralwidget)
        self.button_pesan.setGeometry(QtCore.QRect(0, 257, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_pesan.setFont(font)
        self.button_pesan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_pesan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_pesan.setAutoFillBackground(False)
        self.button_pesan.setStyleSheet("background-color: rgb(218, 114, 60);\n"
"color: rgb(255, 255, 255);\n"
"Text-align:left;")
        self.button_pesan.setFlat(False)
        self.button_pesan.setObjectName("button_pesan")
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
        self.header_pesan = QtWidgets.QLabel(self.centralwidget)
        self.header_pesan.setGeometry(QtCore.QRect(260, 80, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.header_pesan.setFont(font)
        self.header_pesan.setStyleSheet("QLabel{\n"
"    color: rgb(145, 9, 30);\n"
"}")
        self.header_pesan.setObjectName("header_pesan")
        self.button_pesan_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_pesan_2.setGeometry(QtCore.QRect(740, 480, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_pesan_2.setFont(font)
        self.button_pesan_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_pesan_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(218, 114, 60);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.button_pesan_2.setObjectName("button_pesan_2")
        self.tabel_pesan = QtWidgets.QTableWidget(self.centralwidget)
        self.tabel_pesan.setGeometry(QtCore.QRect(260, 130, 591, 341))
        self.tabel_pesan.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabel_pesan.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabel_pesan.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_pesan.setColumnCount(4)
        self.tabel_pesan.setObjectName("tabel_pesan")
        self.tabel_pesan.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pesan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pesan.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pesan.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pesan.setHorizontalHeaderItem(3, item)
        self.tabel_pesan.verticalHeader().setVisible(False)
        self.tabel_pesan.verticalHeader().setDefaultSectionSize(30)
        self.background.raise_()
        self.topbar.raise_()
        self.icon_notif.raise_()
        self.icon_calendar.raise_()
        self.label_date.raise_()
        self.button_home.raise_()
        self.icon_home.raise_()
        self.button_suhu.raise_()
        self.icon_suhu.raise_()
        self.button_pesan.raise_()
        self.icon_pesan.raise_()
        self.button_pesanan.raise_()
        self.icon_pesanan.raise_()
        self.button_logout.raise_()
        self.icon_logout.raise_()
        self.icon_avatar.raise_()
        self.label.raise_()
        self.label_email.raise_()
        self.header_pesan.raise_()
        self.button_pesan_2.raise_()
        self.tabel_pesan.raise_()
        self.PesanRSKlienWindow.setCentralWidget(self.centralwidget)

        # Setup koneksi ke database SQL
        self.setupSQL()
        
        # Apabila tombol pesan RS diklik
        self.button_pesan_2.clicked.connect(self.showConfirmBox)
        
        # Apabila tombol Logout di klik
        self.button_logout.clicked.connect(self.logout)
        
        # Apabila tombol Home di klik
        self.button_home.clicked.connect(self.toKlienHome)
        
        # Apabila tombol Suhu Harian di klik
        self.button_suhu.clicked.connect(self.to_suhu_harian)
        
        #Tombol pesanan diklik
        self.button_pesanan.clicked.connect(self.to_Klien_Pesanan)
        self.loadTable()
        
        self.retranslateUi(PesanRSKlienWindow)
        QtCore.QMetaObject.connectSlotsByName(PesanRSKlienWindow)

    def retranslateUi(self, PesanRSKlienWindow):
        _translate = QtCore.QCoreApplication.translate
        PesanRSKlienWindow.setWindowTitle(_translate("PesanRSKlienWindow", "PesanRSKlienWindow"))
        self.topbar.setText(_translate("PesanRSKlienWindow", "     Pesan Rumah Sakit"))
        today = date.today()
        d2 = today.strftime("%d %B %Y")
        self.label_date.setText(_translate("PesanRSKlienWindow", d2))
        self.button_home.setText(_translate("PesanRSKlienWindow", "              Home"))
        self.button_suhu.setText(_translate("PesanRSKlienWindow", "              Suhu Harian"))
        self.button_pesan.setText(_translate("PesanRSKlienWindow", "              Pesan RS"))
        self.button_pesanan.setText(_translate("PesanRSKlienWindow", "              Pesanan"))
        self.button_logout.setText(_translate("PesanRSKlienWindow", "              Logout"))
        Nama_User = get_nama(self.cursor,self.DB_NAME,self.ID_Pengguna)
        self.label.setText(_translate("PesanRSKlienWindow", Nama_User[1]))
        Email_User = get_email(self.cursor,self.DB_NAME,self.ID_Pengguna)
        self.label_email.setText(_translate("PesanRSKlienWindow", Email_User[1]))
        self.header_pesan.setText(_translate("PesanRSKlienWindow", "Daftar Rumah Sakit yang Tersedia"))
        self.button_pesan_2.setText(_translate("PesanRSKlienWindow", "Pesan"))
        item = self.tabel_pesan.horizontalHeaderItem(0)
        item.setText(_translate("PesanRSKlienWindow", "Nama Rumah Sakit"))
        item = self.tabel_pesan.horizontalHeaderItem(1)
        item.setText(_translate("PesanRSKlienWindow", "Harga Rumah Sakit"))
        item = self.tabel_pesan.horizontalHeaderItem(2)
        item.setText(_translate("PesanRSKlienWindow", "Kapasitas"))
        item = self.tabel_pesan.horizontalHeaderItem(3)
        item.setText(_translate("PesanRSKlienWindow", "Jumlah Pasien  "))

    def setupSQL(self):
        # Melakukan setup koneksi ke database
        self.DB_NAME = get_DB_NAME()
        self.db = mysql.connector.connect(**get_config())
        self.cursor = self.db.cursor()

    def pesanRS(self, i):
        # Melakukan pemesanan rumah sakit oleh klien
        # Apabila pesanan tidak valid (sudah pernah pesan atau masih ada pemesanan berlangsung) akan dimunculkan pesan kesalahan
        if (i.text()=="&Yes"):
            Nama_RS = str(self.tabel_pesan.selectedItems()[0].text())
            ID_RS = get_idRS(self.db,self.cursor,self.DB_NAME,Nama_RS)[1]
            res= add_new_pesanan(self.db,self.cursor,self.DB_NAME,ID_RS,self.ID_Pengguna)
            if (res[0]==1):
                self.showSucc("Pesanan berhasil dibuat")
            else:
                self.showAlert(res[1])
        else :
            print("Gjadi Pesen")

    def showAlert(self,err):
        # Menampilkan pesan kesalahan
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Peringatan")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(err)
        x = msg.exec_()

    def showSucc(self,succ):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Berhasil")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(succ)
        x = msg.exec_()

    def showConfirmBox(self):
        # Menampilkan confirmation box apabila tombol pemesanan diklik
        # Apabila Klien belum memilih rumah sakit akan ditampilkan pesan kesalahan
        try:
            print(self.tabel_pesan.selectedItems()[0].text())
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Konfirmasi Pemesanan")
            msg.setText("Apakah anda yakin ingin memesan :")
            msg.setInformativeText("Nama: "+self.tabel_pesan.selectedItems()[0].text() +"\nHarga :"+self.tabel_pesan.selectedItems()[1].text())
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
            msg.buttonClicked.connect(self.pesanRS)
            x = msg.exec_()
        except:
            self.showAlert("Anda belum memilih rumah sakit")

    def loadTable(self):
        # Melakukan konfigurasi ukuran tabel dan load dari database
        self.tabel_pesan.setColumnWidth(0,225)
        self.tabel_pesan.setColumnWidth(1,150)
        self.tabel_pesan.setColumnWidth(2,105)
        self.tabel_pesan.setColumnWidth(3,109)
        res = get_rs_klien(self.cursor,self.DB_NAME)
        if (res[0]==1):
            data = res[1]
            self.tabel_pesan.setRowCount(len(data))
            idx = 0
            for row in data:
                self.tabel_pesan.setItem(idx, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.tabel_pesan.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabel_pesan.setItem(idx, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabel_pesan.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                idx = idx + 1
        else: 
            self.showAlert(res[1])
	
    def logout(self):
        # Melakukan logout
        from Login_User import Ui_LoginScreen
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self.window)
        self.window.show()
        self.PesanRSKlienWindow.close()
        print("Logout")
        return

    def toKlienHome(self,ID_Pengguna):
        # Navigate to klien home page
        from Home_Klien import Ui_HomeKlienWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeKlienWindow()
        self.ui.setupUi(self.window,self.ID_Pengguna)
        self.window.show()
        self.PesanRSKlienWindow.close()
        print("Klien_Home")
    
    def to_suhu_harian(self):
        # Navigate to suhu harian page
        from Suhu_Klien import Ui_SuhuKlienWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SuhuKlienWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.PesanRSKlienWindow.close()
        print("Suhu Harian")
        return

    def to_Klien_Pesanan(self):
        # Navigate to update laporan page
        from Pesanan_Klien import Ui_PesananKlienWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PesananKlienWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.PesanRSKlienWindow.close()
        print("Klien_Pesanan ")
        return

if __name__ == "__main__":
    import sys
    InitDB()
    app = QtWidgets.QApplication(sys.argv)
    PesanRSKlienWindow = QtWidgets.QMainWindow()
    ui = Ui_PesanRSKlienWindow()
    ui.setupUi(PesanRSKlienWindow)
    PesanRSKlienWindow.show()
    sys.exit(app.exec_())
