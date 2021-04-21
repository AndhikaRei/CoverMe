# import pytest
import mysql.connector
from update_laporan import *

# Test Database SQL
config = {
    "user": "root",
    "password": "root",
    "host": "localhost",
}

DB_NAME = "Cover_Me"
db = mysql.connector.connect(**config)

# Cursor database
cursor = db.cursor()

# Membuat Database - Apabila database sudah ada tidak akan menjadi masalah
create_database(cursor,DB_NAME)


def test_input_kasus_positif_valid():
    """
    Test input kasus positif valid
    """
    result = set_kasus_positif(db, cursor, DB_NAME, 175)
    assert (result[0] == 1)

def test_input_kasus_positif_negatif():
    """
    Test input kasus positif negatif
    """
    result = set_kasus_positif(db, cursor, DB_NAME, -200)
    assert (result[0] == 0)

def test_input_kasus_positif_bukan_integer():
    """
    Test input kasus positif bukan integer, misal string
    """
    result = set_kasus_positif(db, cursor, DB_NAME, "hehehehe")
    assert (result[0] == 0)

def test_input_pasien_sembuh_valid():
    """
    Test input pasien sembuh valid
    """
    result = set_pasien_sembuh(db, cursor, DB_NAME, 175)
    assert (result[0] == 1)

def test_input_pasien_sembuh_negatif():
    """
    Test input pasien sembuh negatif
    """
    result = set_pasien_sembuh(db, cursor, DB_NAME, -200)
    assert (result[0] == 0)

def test_input_pasien_sembuh_bukan_integer():
    """
    Test input pasien sembuh bukan integer, misal string
    """
    result = set_pasien_sembuh(db, cursor, DB_NAME, "hehehehe")
    assert (result[0] == 0)

def test_input_pasien_meninggal_valid():
    """
    Test input pasien meninggal valid
    """
    result = set_pasien_sembuh(db, cursor, DB_NAME, 175)
    assert (result[0] == 1)

def test_input_pasien_meninggal_negatif():
    """
    Test input pasien meninggal negatif
    """
    result = set_pasien_sembuh(db, cursor, DB_NAME, -200)
    assert (result[0] == 0)

def test_input_pasien_meninggal_bukan_integer():
    """
    Test input pasien meninggal bukan integer, misal string
    """
    result = set_pasien_sembuh(db, cursor, DB_NAME, "hehehehe")
    assert (result[0] == 0)

def test_get_kasus_positif():
    """
    Test get kasus positif
    """
    result = set_kasus_positif(db, cursor, DB_NAME, 100)
    result2 = get_kasus_positif(cursor, DB_NAME)[1][0][0]
    assert (result2 == 100)

def test_get_pasien_sembuh():
    """
    Test get pasien sembuh
    """
    result = set_pasien_sembuh(db, cursor, DB_NAME, 100)
    result2 = get_pasien_sembuh(cursor, DB_NAME)[1][0][0]
    assert (result2 == 100)

def test_get_pasien_meninggal():
    """
    Test get pasien meninggal
    """
    result = set_pasien_meninggal(db, cursor, DB_NAME, 100)
    result2 = get_pasien_meninggal(cursor, DB_NAME)[1][0][0]
    assert (result2 == 100)