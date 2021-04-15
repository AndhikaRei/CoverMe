import mysql.connector

# ================================================= Function ===============================================
def get_riwayat_by_id(cursor,DB_NAME, ID_Pengguna):
    cursor.execute("USE {}".format(DB_NAME))
    val = (ID_Pengguna,)
    try:
        sql = ("SELECT Riwayat FROM klien WHERE ID_Pengguna = %s")
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return [1,result]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]

def get_latest_keadaan_by_id(cursor,DB_NAME, ID_Pengguna):
    list_keadaan = convert_riwayat_to_listofkeadaan(get_riwayat_by_id(cursor, DB_NAME, ID_Pengguna)[1][0][0])
    return list_keadaan[0]


def set_riwayat_by_id(db, cursor,DB_NAME, ID_Pengguna, suhu):
    cursor.execute("USE {}".format(DB_NAME))
    try:
        sql = ("UPDATE klien SET Riwayat = %s WHERE ID_Pengguna = %s")
        suhu = float(suhu)
        old_riwayat = get_riwayat_by_id(cursor, DB_NAME, ID_Pengguna)[1][0][0]
        new_riwayat = old_riwayat//2
        if(suhu<25 or suhu >45):
            return [0,"Suhu tidak valid"]
        elif(suhu>=37):
            new_riwayat += 16
        val = (new_riwayat, ID_Pengguna,)
        cursor.execute(sql,val)
        db.commit()
        return [1,"Riwayat suhu tubuh berhasil diubah"]
    except mysql.connector.Error as err:
        print(err.msg)
        return [0,err.msg]
    except ValueError:
        return [0,"Hanya bisa diberi masukan suhu bertipe float"]


def convert_riwayat_to_listofkeadaan(riwayat):
    list_keadaan = []
    while(riwayat > 0):
        if(riwayat%2==1):
            list_keadaan.append("Bahaya")
        else:
            list_keadaan.append("Aman")
        riwayat= riwayat//2

    if(len(list_keadaan)<5):
        for i in range(5-len(list_keadaan)):
            list_keadaan.append("Aman")
    list_keadaan.reverse()
    return list_keadaan

def convert_listofkeadaan_to_riwayat(list_keadaan):
    list_keadaan.reverse()
    riwayat = 0
    for i in range(5):
        if(list_keadaan[i]=="Aman"):
            riwayat=(riwayat/2)
        else:
            riwayat = (riwayat/2)+16
    riwayat = int(riwayat)
    return riwayat


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

# # # Masukan data kasus_positif, pasien sembuh, pasien meninggal 
# result = get_riwayat_by_id(cursor, DB_NAME, 2)
# if(result[0]==1):
#     print(convert_riwayat_to_listofkeadaan(result[1][0][0]))

# result = set_riwayat_by_id(db, cursor, DB_NAME, 2, 27.4)
# print(result[1])
# result = set_riwayat_by_id(db, cursor, DB_NAME, 2, 38)
# print(result[1])
# result = set_riwayat_by_id(db, cursor, DB_NAME, 2, -2)
# print(result[1])
# result = set_riwayat_by_id(db, cursor, DB_NAME, 2, "hehehe")
# print(result[1])

# result = get_riwayat_by_id(cursor, DB_NAME, 2)
# if(result[0]==1):
#     print(convert_riwayat_to_listofkeadaan(result[1][0][0]))

# result = get_latest_keadaan_by_id(cursor, DB_NAME, 2)
# print(result)

# =========================================================================================================