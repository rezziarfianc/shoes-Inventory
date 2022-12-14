import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import controllers.__product as product

def back(suboption,option):
    print("\n")
    print("------------------- Aksi --------------------")
    print("0. Kembali ")
    print("99. Akhiri Program\n")


    ask = input(" Masukan kode aksi (0/99) ? ")

    if(ask == '0'):
        os.system('cls')
        submenu(option)
    elif(ask == '99'):
        exit()
    else:
        os.system('cls')
        if(option == '1'):
            aksesinput(suboption)
        elif(option == '2'):
            aksesinput(suboption)
    

def menu():
    global option
    print("| Welcome To Gimme Shoes Inventory |\n")
    print('===========================================\n')
    print("Menu :")
    print("1. Input Barang")
    print("2. Data Barang\n")
    print("99. Akhiri Program\n")
    print('============================================\n')
    option = input("Silahkan masukkan kode menu (1/2) : ")

    os.system('cls')
    submenu(option)

def submenu(option):
    global suboption
    if(option == '1'):
        
        print("==============| Input Barang |==============\n")
        print("1. Input Barang Masuk")
        print("2. Input Barang Keluar\n")
        print("0. Kembali ")
        print("99. Akhiri Program\n")
        print('============================================\n')

        suboption = input("Silahkan masukkan kode menu (1/2) : ")

        aksesinput(suboption,option)
    elif(option == '2'):
        print("===============| Data Barang |===============\n")
        print("1. Data Semua Barang")
        print("2. Data Barang Masuk")
        print("3. Data Barang Keluar\n")
        print("0. Kembali ")
        print("99. Akhiri Program\n")
        print('=============================================\n')
        suboption = input("Silahkan masukkan kode menu (1/2/3) : ")

        aksesdata(suboption,option)
    elif(option == '99'):
        exit()
    else:
        os.system('cls')
        print("\u001b[31mKode menu tidak valid!\u001b[0m")
        menu()


def aksesinput(suboption,option):
    if(suboption == '1'):
        product.input_barang_masuk()
    elif(suboption == '2'):
        product.input_barang_keluar()
    elif(suboption == '0'):
        os.system('cls')
        menu()
    elif(suboption == '99'):
        exit()
    else:
        os.system('cls')
        print('\u001b[31mKode menu tidak valid!\u001b[0m')
        submenu(option)

def aksesdata(suboption,option):
    os.system('cls')
    if(suboption == '1'):
        print('--------------------- Data Semua Barang -------------------------')
        print("\n")
        product.list()
        back(suboption,option)
    elif(suboption == '2'):
        print('-------------------------------- Data Barang Masuk -----------------------------------')
        print("\n")
        product.list_masuk()
        back(suboption,option)
    elif(suboption == '3'):
        print('-------------------------------- Data Barang Keluar ----------------------------------')
        print("\n")
        product.list_keluar()
        back(suboption,option)
    elif(suboption == '0'):
        os.system('cls')
        menu()
    elif(suboption == '99'):
        exit()
    else:
        os.system('cls')
        print('\u001b[31mKode menu tidak valid!\u001b[0m')
        submenu(option)