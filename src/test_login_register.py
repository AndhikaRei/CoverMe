import random
import pytest
import mysql.connector
from encryption import encrypt_password, check_password
from autentikasi import *


# Test Enkripsi
password = ["", "a", "4200", "-21"]
encrypt = []
for pw in password:
    encrypt.append(encrypt_password(pw)) 

pe = []
for i in range(len(password)):
    pe.append((password[i],encrypt[i]))
    

@pytest.mark.parametrize("password, encrypt",pe)
def test_check_encrypt(password, encrypt):
    """Test Apakah Enkripsi Berhasil
    """
    assert check_password(password, encrypt) == True
    
    
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

def test_input_user_new():
    """Test menambah userbaru, dengan username random
    """
    us = random.randrange(1,10000000000000)
    val = ["Azhar", us, "4200", "azhar@gmail.com", "Bandung", "2001-04-20", "08822313412"]
    result = add_new_user(db,cursor,DB_NAME,val)
    assert result[0] == 1


def test_input_user_already_exist():
    """Test menambah userbaru yang sudah ada
    """
    val1 = ["Azhar", "azhar", "4200", "azhar@gmail.com", "Bandung", "2001-04-20", "08822313412"]
    add_new_user(db,cursor,DB_NAME,val1)
    
    val2 = ["Azhar", "azhar", "4200", "azhar@gmail.com", "Bandung", "2001-04-20", "08822313412"]
    result = add_new_user(db,cursor,DB_NAME,val2)
    assert result[0] == -1

    
def test_login_success():
    """Test untuk cek apakah login sukses dari username yang sudah terdaftar
    """
    val1 = ["Azhar", "azhar", "4200", "azhar@gmail.com", "Bandung", "2001-04-20", "08822313412"]
    add_new_user(db,cursor,DB_NAME,val1)
    
    val2 = ["azhar","4200"]
    result = get_user_id(cursor,DB_NAME,val2)
    assert result[0] == 1
    
def test_login_unsuccess_username():
    """Test untuk cek apakah login gagal dari username yang tidak terdaftar
    """
    val1 = ["Azhar", "azhar", "4200", "azhar@gmail.com", "Bandung", "2001-04-20", "08822313412"]
    add_new_user(db,cursor,DB_NAME,val1)
    
    val2 = ["","4200"]
    result = get_user_id(cursor,DB_NAME,val2)
    assert result[0] == -2
    
    
def test_login_unsuccess_password():
    """Test untuk cek apakah login gagal dari password yang tidak sesuai
    """
    val1 = ["Azhar", "azhar", "4200", "azhar@gmail.com", "Bandung", "2001-04-20", "08822313412"]
    add_new_user(db,cursor,DB_NAME,val1)
    
    val3 = ["azhar","4210"]
    result = get_user_id(cursor,DB_NAME,val3)
    assert result[0] == -1
