import mysql.connector
from encryption import encrypt_password, check_password


# FUNGSIONALITAS SQL
def create_database(cursor,DB_NAME):
    # Membuat database baru jika belum ada
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Berhasil membuat database {} !".format(DB_NAME))


def create_table_user(cursor,DB_NAME):
    # Membuat table user
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    Table_Name = "user"
    Table_Syntax =(
        "CREATE TABLE `user` ("
        " `ID_Pengguna` int AUTO_INCREMENT,"
        " `Nama_Pengguna` varchar(250) NOT NULL,"
        " `Username` varchar(100) UNIQUE NOT NULL,"
        " `Password` varchar(100) NOT NULL,"
        " `Email` varchar(100) NOT NULL ,"
        " `Alamat` varchar(250) NOT NULL ,"
        " `Tanggal_Lahir` Date NOT NULL,"
        " `Nomor_Telepon` VARCHAR(50) NOT NULL,"
        " `Role` VARCHAR(50) NOT NULL DEFAULT 'Klien',"
        " PRIMARY KEY (`ID_Pengguna`)"
        ")"
    )
    try:
        cursor.execute(Table_Syntax)
        print("Berhasil membuat tabel ({}) ".format(Table_Name), end="")
        print()
        return [1,"Berhasil membuat tabel" + Table_Name]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]
 
   
def create_table_klien(cursor,DB_NAME):
    # Membuat table user klien
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    Table_Name = "klien"
    Table_Syntax =(
        "CREATE TABLE `klien` ("
        " `ID_Pengguna` int,"
        " `Riwayat` int DEFAULT 0,"
        " `Status_Akun` varchar(25) DEFAULT 'Biasa',"
        " PRIMARY KEY (`ID_Pengguna`),"
        " FOREIGN KEY (`ID_Pengguna`) REFERENCES user(`ID_Pengguna`)"
        ")"
    )
    try:
        cursor.execute(Table_Syntax)
        print("Berhasil membuat tabel ({}) ".format(Table_Name), end="")
        print()
        return [1,"Berhasil membuat tabel" + Table_Name]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]
    

def add_new_admin(db,cursor,DB_NAME,val):
    # Menambahkan data admin baru
    # @Param
    # db : database yang sedang connect
    # cursor : cursor database
    # DB_Name : nama database
    # val : tupple nama_pengguna, username, password, email, alamat, tanggal_lahir, nomor_telepon, Role
    # Note, password belum diencrypsi
    # Return pesan sukses/error beserta kodenya
    val[2] = encrypt_password(val[2])
    
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql_addAdmin = ("INSERT INTO user(nama_pengguna, username, password, email, alamat, tanggal_lahir, nomor_telepon, Role)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);")
        cursor.execute(sql_addAdmin, val)
        log_id = cursor.lastrowid
        db.commit()
        
        print("Menambahkan Admin dengan id {}".format(log_id))
        return [1,"Menambahkan Admin  dengan id"+str(log_id)]
    # Ada duplicate
    except mysql.connector.IntegrityError as err:    
        # print(err.msg)
        return [-1,err.msg]
    # Error lainnya
    except mysql.connector.Error as err:
        # print(err.msg)
        return [0,err.msg]
    
def add_new_user(db,cursor,DB_NAME,val):
    # Menambahkan data pengguna baru
    # @Param
    # db : database yang sedang connect
    # cursor : cursor database
    # DB_Name : nama database
    # val : tupple nama_pengguna, username, password, email, alamat, tanggal_lahir, nomor_telepon
    # Note, password belum diencrypsi
    # Return pesan sukses/error beserta kodenya
    val[2] = encrypt_password(val[2])
    
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql_addUser = ("INSERT INTO user(nama_pengguna, username, password, email, alamat, tanggal_lahir, nomor_telepon)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s);")
        cursor.execute(sql_addUser, val)
        
        log_id = cursor.lastrowid
        sql_addKlien = ("INSERT INTO klien(ID_Pengguna)"
               "VALUES (%s);")
        cursor.execute(sql_addKlien, [log_id])
        
        db.commit()
        
        print("Menambahkan User dengan id {}".format(log_id))
        return [1,"Menambahkan User dengan id"+str(log_id)]
    # Ada duplicate
    except mysql.connector.IntegrityError as err:    
        # print(err.msg)
        return [-1,err.msg]
    # Error lainnya
    except mysql.connector.Error as err:
        # print(err.msg)
        return [0,err.msg]

def get_username(cursor,DB_NAME,ID_Pengguna):
    # Mendapatkan username lewat ID_Pengguna
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT Username from user where ID_Pengguna = %s")
        val = (ID_Pengguna,)
        cursor.execute(sql, val)
        res = cursor.fetchone()
        if (len(res) > 0):
            print("Berhasil mendapatkan username")
            return [1,res[0]]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_nama(cursor,DB_NAME,ID_Pengguna):
    # Mendapatkan nama pengguna lewat ID_Pengguna
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT Nama_Pengguna from user where ID_Pengguna = %s")
        val = (ID_Pengguna,)
        cursor.execute(sql, val)
        res = cursor.fetchone()
        if (len(res) > 0):
            print("Berhasil mendapatkan nama pengguna")
            return [1,res[0]]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_email(cursor,DB_NAME,ID_Pengguna):
    # Mendapatkan email pengguna lewat ID_Pengguna
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT Email from user where ID_Pengguna = %s")
        val = (ID_Pengguna,)
        cursor.execute(sql, val)
        res = cursor.fetchone()
        if (len(res) > 0):
            print("Berhasil mendapatkan email pengguna")
            return [1,res[0]]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_role(cursor,DB_NAME,ID_Pengguna):
    # Mendapatkan rolelewat ID_Pengguna
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT Role from user where ID_Pengguna = %s")
        val = (ID_Pengguna,)
        cursor.execute(sql, val)
        res = cursor.fetchone()
        if (len(res) > 0):
            print("Berhasil mendapatkan Role")
            return [1,res[0]]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]
    
def get_user_id(cursor,DB_NAME, val):
    # Mendapatkan id user
    # val : tuple berisi username dan password
    # Return pesan sukses/error beserta kodenya
    username = [val[0]]
    password = val[1]
    
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT Id_Pengguna, Password FROM user WHERE username = %s")
        cursor.execute(sql,username)
        result = cursor.fetchall()
        
        if len(result) == 0:
            return [-2, "username tidak ditemukan"]
        
        user_password = result[0][1]
        user_id = result[0][0]
        
        if check_password(password, user_password):
           return [1, user_id]
        else:
            return [-1,"password tidak cocok"]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]



# Main Program
# def main():
    # config = {
    #     "user": "root",
    #     "password": "",
    #     "host": "localhost"
    # }

    # DB_NAME = "Cover_Me"
    # db = mysql.connector.connect(**config)

    # Cursor database
    # cursor = db.cursor()
    
    # # Drop database
    # cursor.execute("DROP DATABASE Cover_Me")

    # # Membuat database "Cover_Me"
    # create_database(cursor,DB_NAME)

    # Membuat tabel user
    # create_table_user(cursor,DB_NAME)

    # Membuat tabel klien
    # create_table_klien(cursor,DB_NAME)
    # password = "Hai"
    
    # Menambah user baru
    # password = encrypt_password("4200")
    # val = ["Azhar", "azhar", "4200", "Gmail@azhar", "Bandung", "2001-04-20", "08822313412"]
    # valAdmin = ["Azhar2", "azhar2", "42002", "Gmail@azhar2", "Bandung", "2001-04-20", "08822313412"]
    # va1 = ["azhar", "4200"]
    # result = get_user_id(cursor, DB_NAME, va1)
    # print(result)
    # add_new_user(db, cursor, DB_NAME, valAdmin)
    # hashed = encrypt_password(password)
    # print(len(hashed))
    
    # check_password(password,hashed)
    
# main()
