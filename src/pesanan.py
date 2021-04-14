import mysql.connector

# ================================================= Function ===============================================
def create_database(cursor,DB_NAME):
    # Membuat database apabila belum ada
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Berhasil membuat database {} !".format(DB_NAME))

def create_table_transaksi(cursor,DB_NAME):
    # Menambahkan tabel transaksi
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    Table_Name = 'pesanan'
    Table_Syntax =(
        "CREATE TABLE `pesanan` ("
        " `ID_Pesanan` int NOT NULL AUTO_INCREMENT,"
        " `ID_Pengguna` int NOT NULL,"
        " `ID_RS` int NOT NULL,"
        " `Tanggal_Pesanan` datetime DEFAULT NOW() ,"
        " `Status_Pesanan` int DEFAULT 0,"
        " PRIMARY KEY (`ID_Pesanan`),"
        " FOREIGN KEY (`ID_RS`) REFERENCES rumah_sakit(`ID_RS`),"
        " FOREIGN KEY (`ID_Pengguna`) REFERENCES user(`ID_Pengguna`)"
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

def add_new_pesanan(db,cursor,DB_NAME,ID_RS,ID_Pengguna):
    # Menambahkan rumah sakit baru
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("""SELECT * FROM pesanan WHERE (Status_Pesanan = 0 OR Status_Pesanan=1) AND ID_Pengguna = %s""")
        val = (ID_Pengguna,)
        cursor.execute(sql,val)
        result = cursor.fetchall()
        if (len(result) >0):
            return [0,"Masih ada pesanan yang berlangsung"]
        else:
            sql = ("INSERT INTO pesanan(ID_RS, ID_Pengguna) VALUES (%s, %s)")
            val = (ID_RS,ID_Pengguna)
            cursor.execute(sql, val)
            db.commit()
            log_id = cursor.lastrowid
            print("Menambahkan Pesanan dengan id {}".format(log_id))
            return [1,"Menambahkan Pesanan dengan id"+str(log_id)]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]


def get_pesanan_admin(cursor,DB_NAME):
    # Mendapatkan pesanan yang bisa dilihat admin
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT * FROM pesanan")
        cursor.execute(sql)
        result = cursor.fetchall()
        return [1,result]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_pesanan_klien(cursor,DB_NAME,ID_Pengguna):
    # Mendapatkan pesanan klien berdasarkan ID_Pengguna
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT * FROM pesanan WHERE ID_Pengguna = %s")
        val = (ID_Pengguna,)
        cursor.execute(sql,val)
        result = cursor.fetchall()
        return [1,result]
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
# create_table_transaksi(cursor,DB_NAME)


# # Mengisi data pesanan
# ID_Pengguna = 1
# ID_RS = 21
# new = add_new_pesanan(db,cursor,DB_NAME,ID_RS,ID_Pengguna)
# print(new)

# # Mendapatkan data rs untuk tabel admin 
# data = get_pesanan_admin(cursor,DB_NAME)
# print(data)

# # Mendapatkan data rs untuk tabel user

# data = get_pesanan_klien(cursor,DB_NAME,ID_Pengguna)
# print(data)

# =========================================================================================================