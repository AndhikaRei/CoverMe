import pytest
import mysql.connector
from rumah_sakit import *
from autentikasi import *
from pesanan import *

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
create_table_user(cursor,DB_NAME)
create_table_klien(cursor,DB_NAME)
create_table_rs(cursor,DB_NAME)
create_table_transaksi(cursor,DB_NAME)

def test_add_new_pesanan():
    """
    Test menambah pesanan baru
    """
    result = add_new_pesanan(db,cursor,DB_NAME,1,1)
    assert (result[0] == 1)

def test_add_another_pesanan():
    """
    Test menambah pesanan meski sudah ada
    """
    result = add_new_pesanan(db,cursor,DB_NAME,1,1)
    assert (result[0] == 0 and result[1] == "Masih ada pesanan yang berlangsung")

def test_get_pesanan_admin():
    """
    Test mangambil semua pesanan 
    """
    result = get_pesanan_admin(cursor,DB_NAME)
    assert result[0] == 1

def test_get_pesanan_klien():
    """
    Test mangambil pesanan satu klien 
    """
    result = get_pesanan_klien(cursor,DB_NAME, 1)
    assert (result[0] == 1)

def test_pesanan_ongoing():
    """
    Test mangambil pesanan klien dengan status bukan -2
    """
    result = get_pesanan_ongoing(cursor,DB_NAME, 1)
    succ = result[0] == 1 and len(result[1]) == 1

    all_result = get_all_pesanan_ongoing(cursor,DB_NAME)
    all_succ = all_result[0] == 1 and len(all_result[1]) == 1
    assert (succ and all_succ)

def test_pesanan_accept():
    """
    Test mengubah status pesanan menjadi 1 (acc)
    """

    result = get_pesanan_ongoing(cursor,DB_NAME, 1)
    ID_Pesanan = result[1][0][4]
    ubah_status(db,cursor,DB_NAME,ID_Pesanan,1)
    result = get_pesanan_ongoing(cursor,DB_NAME, 1)
    succ = result[0] == 1 and len(result[1]) == 1
    
    all_result = get_all_pesanan_ongoing(cursor,DB_NAME)
    all_succ = all_result[0] == 1 and len(all_result[1]) == 0
    assert (succ and all_succ)

def test_add_unsolved_pesanan():
    """
    Test menambah pesanan meski belum batal/bayar
    """
    result = add_new_pesanan(db,cursor,DB_NAME,1,1)
    assert (result[0] == 0 and result[1] == "Masih ada pesanan yang berlangsung")


def test_pesanan_reject():
    """
    Test mengubah status pesanan menjadi -1 (rej)
    """
    result = get_pesanan_ongoing(cursor,DB_NAME, 1)
    ID_Pesanan = result[1][0][4]
    ubah_status(db,cursor,DB_NAME,ID_Pesanan,-1)
    result = get_pesanan_ongoing(cursor,DB_NAME, 1)
    succ = (result[0] == 1 and len(result[1]) == 1)
    
    all_result = get_all_pesanan_ongoing(cursor,DB_NAME)
    all_succ = (all_result[0] == 1 and len(all_result[1]) == 0)

def test_pesanan_batal_or_bayar():
    """
    Test mengubah status pesanan menjadi -2 (rej)
    """
    result = get_pesanan_ongoing(cursor,DB_NAME, 1)
    ID_Pesanan = result[1][0][4]
    ubah_status(db,cursor,DB_NAME,ID_Pesanan,-2)
    result = get_pesanan_ongoing(cursor,DB_NAME, 1)
    succ = (result[0] == 1 and len(result[1]) == 0)
    
    all_result = get_all_pesanan_ongoing(cursor,DB_NAME)
    all_succ = (all_result[0] == 1 and len(all_result[1]) == 0)
