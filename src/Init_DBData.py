from rumah_sakit import *
from pesanan import *
from autentikasi import *
from update_laporan import *


def get_config():
    return  { 'user': 'root', 'password': 'root', 'host': 'localhost', 'port': '3306'}
def get_DB_NAME():
    return'Cover_Me'

def InitDB():
    config = get_config()
    DB_NAME = get_DB_NAME()
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Drop database
    cursor.execute("DROP DATABASE Cover_Me")

    # Membuat Database
    create_database(cursor,DB_NAME)

    # Membuat Tabel
    create_table_rs(cursor,DB_NAME)
    create_table_user(cursor,DB_NAME)
    create_table_klien(cursor,DB_NAME)
    create_table_transaksi(cursor,DB_NAME)
    create_table_laporan(db,cursor,DB_NAME)

    # Mengisi/Modifikasi data 
    add_new_rs(db,cursor,DB_NAME,("RS CEMPAKA", 50000, 2))
    add_new_user(db, cursor, DB_NAME, ["Azhar", "azhar", "4200", "azhar@gmail.com", "Bandung", "2001-04-20", "08822313412"])
    add_new_user(db, cursor, DB_NAME, ["Anantha", "anantha", "4100", "nan@gmail.com", "Bandung", "2001-04-29", "08822313412"])
    add_new_user(db, cursor, DB_NAME, ["Reihan", "reihan", "4000", "rei@gmail.com", "Bandung", "2001-04-25", "08822313412"])
    add_new_user(db, cursor, DB_NAME, ["Kinan", "kinantan", "4300", "kin@gmail.com", "Bandung", "2001-04-23", "08822313412"])
    add_new_admin(db, cursor, DB_NAME, ["Adm MA", "admin_azhar", "42002", "azhar2@gmail.com", "Bandung", "2001-04-20", "08822313412","Admin"])
    add_new_admin(db, cursor, DB_NAME, ["Adm GA", "admin_anantha", "41002", "nan2@gmail.com", "Bandung", "2001-04-29", "08822313412","Admin"])
    add_new_admin(db, cursor, DB_NAME, ["Adm RA", "admin_reihan", "40002", "rei2@gmail.com", "Bandung", "2001-04-25", "08822313412","Admin"])
    add_new_admin(db, cursor, DB_NAME, ["Adm KA", "admin_kinantan", "43002", "kin2@gmail.com", "Bandung", "2001-04-23", "08822313412","Admin"])
    set_kasus_positif(db,cursor,DB_NAME,150)
    set_pasien_sembuh(db,cursor,DB_NAME,100)
    set_pasien_meninggal(db,cursor,DB_NAME,50)





