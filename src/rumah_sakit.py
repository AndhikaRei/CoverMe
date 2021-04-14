import mysql.connector

# ================================================= Function ===============================================
def create_database(cursor,DB_NAME):
    # Membuat database apabila belum ada
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Berhasil membuat database {} !".format(DB_NAME))

def create_table_rs(cursor,DB_NAME):
    # Menambahkan tabel rumah sakit
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    Table_Name = 'rumah_sakit'
    Table_Syntax =(
        "CREATE TABLE `rumah_sakit` ("
        " `ID_RS` int NOT NULL AUTO_INCREMENT,"
        " `Nama_RS` varchar(250) UNIQUE NOT NULL,"
        " `Harga_RS` int NOT NULL,"
        " `Kapasitas` int NOT NULL ,"
        " `Jumlah_Pasien` int NOT NULL DEFAULT 0,"
        " PRIMARY KEY (`ID_RS`)"
        ") ENGINE=InnoDB"
    )
    try:
        print("Berhasil membuat tabel ({}) ".format(Table_Name), end="")
        print()
        cursor.execute(Table_Syntax)
        return [1,"Berhasil membuat tabel" + Table_Name]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def add_new_rs(db,cursor,DB_NAME,val):
    # Menambahkan rumah sakit baru
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("INSERT INTO rumah_sakit(Nama_RS, Harga_RS, Kapasitas) VALUES (%s, %s, %s)")
        cursor.execute(sql, val)
        db.commit()
        log_id = cursor.lastrowid
        print("Menambahkan Rumah Sakit dengan id {}".format(log_id))
        return [1,"Menambahkan Rumah Sakit dengan id"+str(log_id)]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_rs_admin(cursor,DB_NAME):
    # Mendapatkan rs yang bisa dilihat admin
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT * FROM rumah_sakit")
        cursor.execute(sql)
        result = cursor.fetchall()
        return [1,result]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_rs_klien(cursor,DB_NAME):
    # Mendapatkan rs yang bisa dipesan klien
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT Nama_RS,Harga_RS,Kapasitas,Jumlah_Pasien FROM rumah_sakit WHERE Jumlah_Pasien < Kapasitas")
        cursor.execute(sql)
        result = cursor.fetchall()
        return [1,result]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def tambah_pasien(db,cursor,DB_NAME,nama_rs):
    # Menambah pasien di rumah sakit tertentu
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("UPDATE rumah_sakit SET Jumlah_Pasien = Jumlah_Pasien + 1 WHERE Nama_RS = %s")
        val = (nama_rs,)
        cursor.execute(sql,val)
        print(cursor)
        db.commit()
        return [1,"Pasien berhasil ditambahkan"]

    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def kurangi_pasien(db,cursor,DB_NAME,nama_rs):
    # Mengurangi pasien di rumah sakit tertentu
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("UPDATE rumah_sakit SET Jumlah_Pasien = Jumlah_Pasien - 1 WHERE Nama_RS = %s")
        val = (nama_rs,)
        cursor.execute(sql,val)
        db.commit()
        return [1,"Pasien berhasil dikurangi"]

    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_idRS(db,cursor,DB_Name,nama_rs):
    try:
        sql = ("SELECT ID_RS FROM rumah_sakit WHERE Nama_RS = %s")
        val = (nama_rs,)
        cursor.execute(sql,val)
        res = cursor.fetchone()
        return [1,res[0]]

    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]


# =========================================================================================================

# ============================================= Main Program ==============================================
# config = {
#     'user': 'root',
#     'password': '',
#     'host': 'localhost'
# }
# DB_NAME = 'Cover_Me'
# db = mysql.connector.connect(**config)
# cursor = db.cursor()

# # Membuat Database
# create_database(cursor,DB_NAME)

# # Membuat Tabel
# create_table_rs(cursor,DB_NAME)

# # Mengisi data rumah sakit
# val = ("RS CEMPAKA", 50000, 2)
# add_new_rs(db,cursor,DB_NAME,val)

# # Mendapatkan data rs untuk tabel admin 
# data = get_rs_admin(cursor,DB_NAME)
# print(data[1])

# # Mendapatkan data rs untuk tabel user
# data = get_rs_klien(cursor,DB_NAME)
# print(data[1])

# # Menambah jumlah pasien
# num = tambah_pasien(db,cursor,DB_NAME,"RS CEMPAKA")
# print(num)

# # Mengurangi jumlah pasien
# num = kurangi_pasien(db,cursor,DB_NAME,"RS CEMPAKA")
# print(num)

# =========================================================================================================