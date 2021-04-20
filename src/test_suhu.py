import pytest
import mysql.connector
from autentikasi import *
from suhu_harian import *

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
create_table_klien(cursor,DB_NAME)

def test_input_suhu_positif_valid():
    """
    Test cek suhu harian klien dengan input yang positif dan valid
    """
    result = set_riwayat_by_id(db, cursor, DB_NAME, 2, 27.4)
    assert (result[0] == 1)

def test_input_suhu_positif_not_valid():
    """
    Test cek suhu harian klien dengan input yang tidak valid
    """
    result = set_riwayat_by_id(db, cursor, DB_NAME, 2, 38)
    assert (result[0] == 0)

def test_input_suhu_aman():
    """
    Test cek suhu harian klien dengan input yang termasuk dalam rentang aman
    """
    result = set_riwayat_by_id(db, cursor, DB_NAME, 2, 36)
    result2 = get_latest_keadaan_by_id(cursor, DB_NAME, 2)
    assert (result2 == "Aman")

def test_input_suhu_bahaya():
    """
    Test cek suhu harian klien dengan input yang termasuk dalam rentang bahaya
    """
    result = set_riwayat_by_id(db, cursor, DB_NAME, 2, 39)
    result2 = get_latest_keadaan_by_id(cursor, DB_NAME, 2)
    assert (result2 == "Bahaya")
