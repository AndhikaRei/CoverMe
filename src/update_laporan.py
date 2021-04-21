import mysql.connector

# ================================================= Function ===============================================
def create_database(cursor,DB_NAME):
    # Membuat database apabila belum ada
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Berhasil membuat database {} !".format(DB_NAME))

def create_table_laporan(db,cursor,DB_NAME):
    # Menambahkan tabel transaksi
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    Table_Name = 'data_harian_covid_19'
    Table_Syntax =(
        "CREATE TABLE `data_harian_covid_19` ("
        " `ID` int NOT NULL AUTO_INCREMENT,"
        " `Kasus_Positif` int NOT NULL,"
        " `Pasien_Sembuh` int NOT NULL,"
        " `Pasien_Meninggal` int NOT NULL,"
        " PRIMARY KEY (`ID`)"
        ")"
    )
    try:
        print("Berhasil membuat tabel ({}) ".format(Table_Name), end="")
        print()
        cursor.execute(Table_Syntax)
        
        # # Mengisi data laporan
        insert_dummy_data(db, cursor, DB_NAME)
        return [1,"Berhasil membuat tabel" + Table_Name]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def insert_dummy_data(db, cursor, DB_NAME) :
    # Set value pertama dari tabel data_harian_covid_19
    # Kasus Positif 0, Pasien Sembuh 0, Pasien Meninggal 0
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("""INSERT INTO data_harian_covid_19 (Kasus_Positif, Pasien_Sembuh, Pasien_Meninggal) VALUES (0,0,0)""")
        cursor.execute(sql)
        db.commit()
        print("Menambahkan dummy data")
        return [1,"Menambahkan dummy data ke data_harian_covid_19"]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_kasus_positif(cursor,DB_NAME):
    # Mendapatkan pesanan yang bisa dilihat admin
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT Kasus_Positif FROM data_harian_covid_19")
        cursor.execute(sql)
        result = cursor.fetchall()
        return [1,result]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def set_kasus_positif(db, cursor,DB_NAME, new_kasus_positif):
    # Mendapatkan pesanan yang bisa dilihat admin
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("UPDATE data_harian_covid_19 SET Kasus_Positif = %s")
        val = (new_kasus_positif,)
        old = get_kasus_positif(cursor, DB_NAME)[1][0][0]
        cursor.execute(sql,val)
        db.commit()
        if(int(new_kasus_positif)<=0):
            set_kasus_positif(db,cursor,DB_NAME, old)
            return [0,"Kasus positif tidak valid"]
        else:
            return [1,"Kasus positif berhasil diubah"]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_pasien_sembuh(cursor,DB_NAME):
    # Mendapatkan pesanan yang bisa dilihat admin
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT Pasien_Sembuh FROM data_harian_covid_19")
        cursor.execute(sql)
        result = cursor.fetchall()
        return [1,result]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def set_pasien_sembuh(db, cursor,DB_NAME, new_pasien_sembuh):
    # Mendapatkan pesanan yang bisa dilihat admin
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("UPDATE data_harian_covid_19 SET Pasien_Sembuh = %s")
        val = (new_pasien_sembuh,)
        old = get_pasien_sembuh(cursor, DB_NAME)[1][0][0]
        cursor.execute(sql,val)
        db.commit()
        if(int(new_pasien_sembuh)<=0):
            set_pasien_sembuh(db,cursor,DB_NAME, old)
            return [0,"Pasien sembuh tidak valid"]
        else:
            return [1,"Pasien Sembuh berhasil diubah"]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_pasien_meninggal(cursor,DB_NAME):
    # Mendapatkan pesanan yang bisa dilihat admin
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("SELECT Pasien_Meninggal FROM data_harian_covid_19")
        cursor.execute(sql)
        result = cursor.fetchall()
        return [1,result]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def set_pasien_meninggal(db, cursor,DB_NAME, new_pasien_meninggal):
    # Mendapatkan pesanan yang bisa dilihat admin
    # Return pesan sukses/error beserta kodenya
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("UPDATE data_harian_covid_19 SET Pasien_Meninggal = %s")
        val = (new_pasien_meninggal,)
        old = get_pasien_meninggal(cursor, DB_NAME)[1][0][0]
        cursor.execute(sql,val)
        db.commit()
        if(int(new_pasien_meninggal)<=0):
            set_pasien_meninggal(db,cursor,DB_NAME, old)
            return [0,"Pasien Meninggal tidak valid"]
        else:
            return [1,"Pasien Meninggal berhasil diubah"]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]


# =========================================================================================================

# ============================================= Main Program ==============================================
# config = {
#     'user': 'root',
#     'password': 'root',
#     'host': 'localhost',
#     'port' : '3307'
# }
# DB_NAME = 'Cover_Me'
# db = mysql.connector.connect(**config)
# cursor = db.cursor()

# # # Membuat Database
# # create_database(cursor,DB_NAME)

# # # Membuat Tabel
# create_table_laporan(db,cursor,DB_NAME)

# # # Masukan data kasus_positif, pasien sembuh, pasien meninggal 
# set_kasus_positif(cursor,DB_NAME,150)
# set_pasien_sembuh(cursor,DB_NAME,100)
# set_pasien_meninggal(cursor,DB_NAME,50)

# # # Mendapatkan data kasus_positif, pasien sembuh, pasien meninggal 
# positif = get_kasus_positif(cursor,DB_NAME)
# sembuh = get_pasien_sembuh(cursor,DB_NAME)
# meninggal = get_pasien_meninggal(cursor,DB_NAME)
# print(positif, sembuh, meninggal)


# =========================================================================================================