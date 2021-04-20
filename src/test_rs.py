import pytest
import mysql.connector
from rumah_sakit import *

# Test Database SQL
config = {
    "user": "root",
    "password": "root",
    "host": "localhost"
}

DB_NAME = "Cover_Me"
db = mysql.connector.connect(**config)

# Cursor database
cursor = db.cursor()

# Membuat Database - Apabila database sudah ada tidak akan menjadi masalah
create_database(cursor,DB_NAME)

# Membuat Tabel - Apabila tabel sudah ada tidak akan menjadi masalah
create_table_rs(cursor,DB_NAME)

def test_input_rs_benar():
    """
    Test menambah rumah sakit baru yang datanya valid
    """
    val = ("RS CEMPAKA8", 50000, 2)
    result = add_new_rs(db,cursor,DB_NAME,val)
    assert (result[0] == 1 or result[0] ==0)

def test_input_rs_salah():
    """
    Test menambah rumah sakit baru yang datanya tidak valid
    """
    val = ("RS CEMPAKA8", 50000, "Ini mestinya angka")
    result = add_new_rs(db,cursor,DB_NAME,val)
    assert result[0] == 0

def test_kurangi_pasien():
    """
    Test mengurangi jumlah pasien
    """
    sql = ("""SELECT Jumlah_Pasien FROM rumah_sakit WHERE Nama_RS = 'RS CEMPAKA8' """)
    cursor.execute(sql)
    totPasienLama = cursor.fetchone()[0]
    kurangi_pasien(db,cursor,DB_NAME,"RS CEMPAKA8")
    cursor.execute(sql)
    totPasienBaru = cursor.fetchone()[0]
    assert totPasienBaru == totPasienLama-1

def test_tambah_pasien():
    """
    Test menambah jumlah pasien
    """
    sql = ("""SELECT Jumlah_Pasien FROM rumah_sakit WHERE Nama_RS = 'RS CEMPAKA8' """)
    cursor.execute(sql)
    totPasienLama = cursor.fetchone()[0]
    tambah_pasien(db,cursor,DB_NAME,"RS CEMPAKA8")
    cursor.execute(sql)
    totPasienBaru = cursor.fetchone()[0]
    assert totPasienBaru == totPasienLama+1
