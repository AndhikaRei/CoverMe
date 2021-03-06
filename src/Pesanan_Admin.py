from PyQt5 import QtCore, QtGui, QtWidgets
from autentikasi import *
from pesanan import *
from rumah_sakit import *
from suhu_harian import *
import mysql.connector
from Init_DBData import *
from datetime import date

class Ui_PesananAdminWindow(object):
    def setupUi(self, PesananAdminWindow, ID_Pengguna=1):
        self.PesananAdminWindow=PesananAdminWindow
        self.PesananAdminWindow.setObjectName("PesananAdminWindow")
        self.PesananAdminWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(PesananAdminWindow)
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
        self.icon_pesanan.setPixmap(QtGui.QPixmap("../img/pesanan-white.png"))
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
        self.button_pesanan.setStyleSheet("background-color: rgb(218, 114, 60);\n"
"color: rgb(255, 255, 255);\n"
"Text-align:left;")
        self.button_pesanan.setFlat(False)
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
        self.tabel_pesan = QtWidgets.QTableWidget(self.centralwidget)
        self.tabel_pesan.setGeometry(QtCore.QRect(260, 90, 591, 361))
        self.tabel_pesan.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabel_pesan.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_pesan.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pesan.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pesan.setHorizontalHeaderItem(5, item)
        self.tabel_pesan.verticalHeader().setVisible(False)
        self.tabel_pesan.verticalHeader().setDefaultSectionSize(30)
        self.Reject_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Reject_Button.setGeometry(QtCore.QRect(680, 460, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.Reject_Button.setFont(font)
        self.Reject_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reject_Button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(145, 9, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Reject_Button.setObjectName("Reject_Button")
        self.Accept_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Accept_Button.setGeometry(QtCore.QRect(490, 460, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.Accept_Button.setFont(font)
        self.Accept_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Accept_Button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(92, 184, 92);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Accept_Button.setObjectName("Accept_Button")
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
        self.tabel_pesan.raise_()
        self.Reject_Button.raise_()
        self.Accept_Button.raise_()
        self.PesananAdminWindow.setCentralWidget(self.centralwidget)

        #Setup
        self.setupSql()
        self.ID_Pengguna = ID_Pengguna
        
        #Navigasi
        self.button_laporan.clicked.connect(self.to_update_laporan)
        self.button_home.clicked.connect(self.to_Admin_Home)
        self.button_logout.clicked.connect(self.logout)
        self.button_rs.clicked.connect(self.to_Data_RS)
        
        self.loadTable()
        self.Accept_Button.clicked.connect(self.acceptPesanan)
        self.Reject_Button.clicked.connect(self.rejectPesanan)
        
        self.retranslateUi(PesananAdminWindow)
        QtCore.QMetaObject.connectSlotsByName(PesananAdminWindow)

    def retranslateUi(self, PesananAdminWindow):
        _translate = QtCore.QCoreApplication.translate
        PesananAdminWindow.setWindowTitle(_translate("PesananAdminWindow", "PesananAdminWindow"))
        self.topbar.setText(_translate("PesananAdminWindow", "     Daftar Pesanan"))
        today = date.today()
        d2 = today.strftime("%d %B %Y")
        self.label_date.setText(_translate("LaporanAdminWindow", d2))
        self.button_home.setText(_translate("PesananAdminWindow", "              Home"))
        self.button_laporan.setText(_translate("PesananAdminWindow", "              Laporan Harian"))
        self.button_rs.setText(_translate("PesananAdminWindow", "              Rumah Sakit"))
        self.button_pesanan.setText(_translate("PesananAdminWindow", "              Daftar Pesanan"))
        self.button_logout.setText(_translate("PesananAdminWindow", "              Logout"))
        Nama_User = get_nama(self.cursor,self.DB_NAME,self.ID_Pengguna)
        self.label.setText(_translate("PesananAdminWindow", Nama_User[1]))
        Email_User = get_email(self.cursor,self.DB_NAME,self.ID_Pengguna)
        self.label_email.setText(_translate("PesananAdminWindow", Email_User[1]))
        item = self.tabel_pesan.horizontalHeaderItem(0)
        item.setText(_translate("PesananAdminWindow", "ID"))
        item = self.tabel_pesan.horizontalHeaderItem(1)
        item.setText(_translate("PesananAdminWindow", "Pemesan"))
        item = self.tabel_pesan.horizontalHeaderItem(2)
        item.setText(_translate("PesananAdminWindow", "Riwayat"))
        item = self.tabel_pesan.horizontalHeaderItem(3)
        item.setText(_translate("PesananAdminWindow", "Tanggal Pesan"))
        item = self.tabel_pesan.horizontalHeaderItem(4)
        item.setText(_translate("PesananAdminWindow", "Rumah Sakit"))
        item = self.tabel_pesan.horizontalHeaderItem(5)
        item.setText(_translate("PesananAdminWindow", "Pasien / Kapasitas"))
        self.Reject_Button.setText(_translate("PesananAdminWindow", "Reject"))
        self.Accept_Button.setText(_translate("PesananAdminWindow", "Accept"))

    def setupSql(self):
        # Melakukan setup koneksi SQL
        self.DB_NAME = get_DB_NAME()
        self.db = mysql.connector.connect(**get_config())
        self.cursor = self.db.cursor()

    def loadTable(self):
        self.tabel_pesan.setColumnWidth(0,50)
        self.tabel_pesan.setColumnWidth(1,100)
        self.tabel_pesan.setColumnWidth(2,250)
        self.tabel_pesan.setColumnWidth(3,150)
        self.tabel_pesan.setColumnWidth(4,100)
        self.tabel_pesan.setColumnWidth(5,100)
        res = get_all_pesanan_ongoing(self.cursor,self.DB_NAME)
        if (res[0]==1):
            data = res[1]
            self.tabel_pesan.setRowCount(len(data))
            idx = 0
            for row in data:
                print(row)
                self.tabel_pesan.setItem(idx, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabel_pesan.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                list_keadaan = convert_riwayat_to_listofkeadaan(row[2])
                self.tabel_pesan.setItem(idx, 2, QtWidgets.QTableWidgetItem('-'.join(list_keadaan)))
                self.tabel_pesan.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tabel_pesan.setItem(idx, 4, QtWidgets.QTableWidgetItem(row[4]))
                self.tabel_pesan.setItem(idx, 5, QtWidgets.QTableWidgetItem(str(row[6]) + "/" + str(row[5])))
                idx = idx + 1
        else: 
            print(res[1])

    def showAlert(self,err):
        # Menampilkan pesan kesalahan
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Peringatan")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(err)
        x = msg.exec_()

    def acceptPesanan(self):
        try:
            ID_Pesanan = int(self.tabel_pesan.selectedItems()[0].text())
            pasien = self.tabel_pesan.selectedItems()[5].text().split("/")
            print(pasien)
            if(pasien[0] == pasien[1]):
                self.showAlert("RS penuh")
            else:
                respon = ubah_status(self.db,self.cursor,self.DB_NAME,ID_Pesanan,1)
                nama_RS = self.tabel_pesan.selectedItems()[4].text()
                tambah_pasien(self.db,self.cursor,self.DB_NAME, nama_RS)
                print(respon)
                self.loadTable()
        except:
            self.showAlert("Belum memilih pesanan")

    def rejectPesanan(self):
        try:
            self.ID_Pesanan = int(self.tabel_pesan.selectedItems()[0].text())
            respon = ubah_status(self.db,self.cursor,self.DB_NAME,self.ID_Pesanan,-1)
            print(respon)
            self.loadTable()
        except:
    	    self.showAlert("Belum memilih pesanan")
    
    def logout(self):
        # Melakukan logout
        from Login_User import Ui_LoginScreen
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self.window)
        self.window.show()
        self.PesananAdminWindow.close()
        print("Logout")
        return

    def to_update_laporan(self):
        # Navigate to update laporan page
        from Laporan_Admin import Ui_LaporanAdminWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LaporanAdminWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.PesananAdminWindow.close()
        print("Update Laporan")
        return
	
    def to_Data_RS(self):
        # Navigate to update laporan page
        from RS_Admin import UI_RSAdminWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_RSAdminWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.PesananAdminWindow.close()
        print("Data RS ")
        return

    def to_Admin_Home(self):
        # Navigate to update laporan page
        from Home_Admin import Ui_HomeAdminWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeAdminWindow()
        self.ui.setupUi(self.window, self.ID_Pengguna)
        self.window.show()
        self.PesananAdminWindow.close()
        print("Admin_Home ")
        return


if __name__ == "__main__":
    import sys
    InitDB()
    app = QtWidgets.QApplication(sys.argv)
    PesananAdminWindow = QtWidgets.QMainWindow()
    ui = Ui_PesananAdminWindow()
    ui.setupUi(PesananAdminWindow)
    PesananAdminWindow.show()
    sys.exit(app.exec_())
