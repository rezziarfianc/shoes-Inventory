import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.__database import db
from tabulate import tabulate
import controllers.__view as view

def list():
    cursor = db.cursor(dictionary=True)
    sql = "SELECT m.nama as merk, sr.nama as series, sp.ukuran, sp.stok FROM sepatu sp LEFT JOIN series sr ON sr.id = sp.id_series LEFT JOIN merk m ON m.id = sr.id_merk ORDER BY sp.id DESC"
    cursor.execute(sql)

    data = cursor.fetchall()

    no = []
    merk = []
    series = []
    ukuran = []
    stok = []
    index = 0

    for d in data:
        index += 1
        no.append(index)
        merk.append(d['merk'])
        series.append(d['series'])
        ukuran.append(d['ukuran'])
        stok.append(d['stok'])

    table = tabulate({
                    "No" : no,
                    "Merk" : merk,
                    "Series" : series,
                    "Ukuran" : ukuran,
                    "Stok" : stok}, headers="keys")

    return print(table)

def list_masuk():
    cursor = db.cursor(dictionary=True)
    sql = "SELECT m.nama as merk, sr.nama as series, sp.ukuran, bm.jumlah, bm.stok_sebelum, bm.stok_sesudah, DATE_FORMAT(bm.created_at, '%d %M %Y') as tanggal FROM barang_masuk bm LEFT JOIN sepatu sp ON sp.id = bm.id_sepatu LEFT JOIN series sr ON sr.id = sp.id_series LEFT JOIN merk m ON m.id = sr.id_merk ORDER BY bm.id DESC"
    cursor.execute(sql)

    data = cursor.fetchall()

    no = []
    merk = []
    series = []
    ukuran = []
    jumlah = []
    stok_sebelum = []
    stok_sesudah = []
    tanggal = []
    index = 0

    for d in data:
        index += 1
        no.append(index)
        merk.append(d['merk'])
        series.append(d['series'])
        ukuran.append(d['ukuran'])
        jumlah.append(d['jumlah'])
        stok_sebelum.append(d['stok_sebelum'])
        stok_sesudah.append(d['stok_sesudah'])
        tanggal.append(d['tanggal'])

    table = tabulate({
                    "No" : no,
                    "Merk" : merk,
                    "Series" : series,
                    "Ukuran" : ukuran,
                    "Jumlah Masuk" : jumlah,
                    "Stok Sebelum" : stok_sebelum,
                    "Stok Sesudah" : stok_sesudah,
                    "Tanggal" : tanggal}, headers="keys")

    return print(table)


def list_keluar():
    cursor = db.cursor(dictionary=True)
    sql = "SELECT m.nama as merk, sr.nama as series, sp.ukuran, bk.jumlah, bk.stok_sebelum, bk.stok_sesudah, DATE_FORMAT(bk.created_at, '%d %M %Y') as tanggal FROM barang_keluar bk LEFT JOIN sepatu sp ON sp.id = bk.id_sepatu LEFT JOIN series sr ON sr.id = sp.id_series LEFT JOIN merk m ON m.id = sr.id_merk ORDER BY bk.id DESC"
    cursor.execute(sql)

    data = cursor.fetchall()

    no = []
    merk = []
    series = []
    ukuran = []
    jumlah = []
    stok_sebelum = []
    stok_sesudah = []
    tanggal = []
    index = 0

    for d in data:
        index += 1
        no.append(index)
        merk.append(d['merk'])
        series.append(d['series'])
        ukuran.append(d['ukuran'])
        jumlah.append(d['jumlah'])
        stok_sebelum.append(d['stok_sebelum'])
        stok_sesudah.append(d['stok_sesudah'])
        tanggal.append(d['tanggal'])

    table = tabulate({
                    "No" : no,
                    "Merk" : merk,
                    "Series" : series,
                    "Ukuran" : ukuran,
                    "Jumlah Keluar" : jumlah,
                    "Stok Sebelum" : stok_sebelum,
                    "Stok Sesudah" : stok_sesudah,
                    "Tanggal" : tanggal}, headers="keys")

    return print(table)


def list_merk():
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM merk ORDER BY id ASC"
    cursor.execute(sql)

    kode = []
    nama = []

    data = cursor.fetchall()

    for d in data:
        # print(f"{d['id']}. {d['nama']}")
        kode.append(d['id'])
        nama.append(d['nama'])

    table = tabulate({
        "Kode" : kode,
        "Nama" : nama
    }, headers="keys")
    
    print(table)
    print('----------------')
    print("0. Kembali")
    print('----------------\n')
    
def cek_merk(merk):
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM merk WHERE id = %s ORDER BY id ASC"
    val = (merk,)
    cursor.execute(sql,val)

    data = cursor.fetchone()

    return data

def list_series(merk):
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM series WHERE id_merk = %s ORDER BY kode ASC"
    val = (merk,)
    cursor.execute(sql,val)

    kode = []
    nama = []

    data = cursor.fetchall()

    for d in data:
        # print(f"[ {d['kode']} ] {d['nama']}")
        kode.append(d['kode'])
        nama.append(d['nama'])

    table = tabulate({
        "Kode" : kode,
        "Nama" : nama
    }, headers="keys")

    print(table)
    print('--------------------')
    print("0. Kembali")
    print('--------------------\n')

def cek_series(series):
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM series WHERE kode = %s ORDER BY id ASC"
    val = (series,)
    cursor.execute(sql,val)

    data = cursor.fetchone()

    return data

def cek_sepatu(series,ukuran):

    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM sepatu WHERE id_series = %s AND ukuran = %s ORDER BY id ASC"
    val = (series,ukuran,)
    cursor.execute(sql,val)

    data = cursor.fetchone()

    return data

def input_barang_masuk():
    while True:
        os.system('cls')
        print('--------- Input Barang Masuk ---------')
        print("\n")
        list_merk()
        merk = input("Masukan Kode merk = ")
        if(merk == "0") :
            os.system('cls')
            view.menu()
            break
        cekmerk = cek_merk(merk)
        if(cekmerk) :
            os.system('cls')
            print('--------- Input Barang Masuk ---------')
            print("\n")
            list_series(merk)
            series = input("Masukan kode series = ")
            if(series == "0") :
                os.system('cls')
                input_barang_masuk()
                break
            cekseries = cek_series(series)
            if(cekseries) :
                ukuran = int(input("Masukan ukuran = "))
                
                ceksepatu = cek_sepatu(cekseries['id'],ukuran)

                if(ceksepatu) :
                    print(f"\u001b[32mSepatu tersedia dengan jumlah stok {ceksepatu['stok']} buah\u001b[0m")
                    jumlah = int(input("Masukan jumlah barang masuk = "))
                    idsepatu = ceksepatu['id']
                    stoksebelum = ceksepatu['stok']
                    stoksesudah = ceksepatu['stok'] + jumlah

                    barangmasuk = query_insert_barang_masuk(idsepatu, jumlah, stoksebelum, stoksesudah)
                    stoksepatu = query_update_stok(idsepatu, stoksesudah)
                    
                    print('\u001b[32mData Berhasil di Tambahkan\u001b[0m')

                    ask = input('Ingin input lagi [Y/N] ?')

                    if(ask == 'Y' or ask == 'y') :
                        continue
                    else :
                        os.system('cls')
                        view.menu()
                        break
                        


                else :
                    print('\u001b[32mStok sepatu tidak ada, data akan ditambahkan sebagai stok baru\u001b[0m')
                    jumlah = int(input("Masukan jumlah barang masuk = "))

                    stoksepatu = query_tambah_sepatu(cekseries['id'],ukuran,jumlah)
                    barangmasuk = query_insert_barang_masuk(stoksepatu.lastrowid, jumlah, 0, jumlah)

                    print('\u001b[32mData Berhasil di Tambahkan\u001b[0m')

                    ask = input('Ingin input lagi [Y/N] ?')

                    if(ask == 'Y' or ask == 'y') :
                        continue
                    else :
                        os.system('cls')
                        view.menu()
                        break 

            else :
                ask = input("Series tidak valid, Ingin lanjutkan input ? [Y/N]: ")

                if(ask == 'Y'  or ask == 'y'):

                    continue
                else:

                    os.system('cls')
                    view.menu()
                    break
        else :
            ask = input("Merk tidak valid, Ingin lanjutkan input ? [Y/N]: ")

            if(ask == 'Y'  or ask == 'y'):

                continue
            else:

                os.system('cls')
                view.menu()
                break

def input_barang_keluar():
    while True:
        os.system('cls')
        print('--------- Input Barang Keluar ---------')
        print("\n")
        list_merk()
        merk = input("Masukan nomor merk = ")
        if(merk == "0") :
            os.system('cls')
            view.menu()
            break
        cekmerk = cek_merk(merk)
        if(cekmerk) :
            os.system('cls')
            print('--------- Input Barang Keluar ---------')
            print("\n")
            list_series(merk)
            series = input("Masukan kode series = ")
            if(series == "0") :
                os.system('cls')
                input_barang_keluar()
                break
            cekseries = cek_series(series)
            if(cekseries) :
                ukuran = int(input("Masukan ukuran = "))
                ceksepatu = cek_sepatu(cekseries['id'],ukuran)

                if(ceksepatu) :
                    print(f"\u001b[32mSepatu tersedia dengan jumlah stok {ceksepatu['stok']} buah\u001b[0m")
                    jumlah = int(input("Masukan jumlah barang keluar = "))

                    while(jumlah > ceksepatu['stok']) :
                        print("\u001b[31mJumlah keluar tidak dapat melebihi stok\u001b[0m")
                        jumlah = int(input("Masukan jumlah barang keluar = "))

                    idsepatu = ceksepatu['id']
                    stoksebelum = ceksepatu['stok']
                    stoksesudah = ceksepatu['stok'] - jumlah

                    barangmasuk = query_insert_barang_keluar(idsepatu, jumlah, stoksebelum, stoksesudah)
                    stoksepatu = query_update_stok(idsepatu, stoksesudah)
                    
                    print('\u001b[32mData Berhasil di Tambahkan\u001b[0m')

                    ask = input('Ingin input lagi [Y/N] ?')

                    if(ask == 'Y' or ask == 'y') :
                        continue
                    else :
                        os.system('cls')
                        view.menu()
                        break
                        


                else :

                    print('\u001b[31mStok sepatu tidak ada\u001b[0m')

                    ask = input('Ingin input lagi [Y/N] ?')

                    if(ask == 'Y' or ask == 'y') :
                        continue
                    else :
                        os.system('cls')
                        view.menu()
                        break 

            else :
                ask = input("Series tidak valid, Ingin lanjutkan input ? [Y/N]: ")

                if(ask == 'Y'  or ask == 'y'):

                    continue
                else:

                    os.system('cls')
                    view.menu()
                    break
        else :
            ask = input("Merk tidak valid, Ingin lanjutkan input ? [Y/N]: ")

            if(ask == 'Y'  or ask == 'y'):

                continue
            else:
                os.system('cls')
                view.menu()
                break

        

def query_insert_barang_masuk(idsepatu, jumlah, stoksebelum, stoksesudah) :
    cursor = db.cursor()
    sql = "INSERT INTO barang_masuk (id_sepatu, jumlah, stok_sebelum, stok_sesudah) VALUES (%s, %s, %s, %s)"
    val = (idsepatu, jumlah, stoksebelum, stoksesudah)
    cursor.execute(sql, val)

    db.commit()

    return cursor

def query_insert_barang_keluar(idsepatu, jumlah, stoksebelum, stoksesudah) :
    cursor = db.cursor()
    sql = "INSERT INTO barang_keluar (id_sepatu, jumlah, stok_sebelum, stok_sesudah) VALUES (%s, %s, %s, %s)"
    val = (idsepatu, jumlah, stoksebelum, stoksesudah)
    cursor.execute(sql, val)

    db.commit()

    return cursor

def query_update_stok(idsepatu, stok) :
    cursor = db.cursor()
    sql = "UPDATE sepatu SET stok = %s WHERE id = %s"
    val = (stok, idsepatu)
    cursor.execute(sql, val)

    db.commit()

    return cursor

def query_tambah_sepatu(series, ukuran, stok) :
    cursor = db.cursor()
    sql = "INSERT INTO sepatu (id_series, ukuran, stok) VALUES (%s, %s, %s)"
    val = (series, ukuran, stok)
    cursor.execute(sql, val)

    db.commit()

    return cursor