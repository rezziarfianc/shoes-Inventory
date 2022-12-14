import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.__database import db
import hashlib, pwinput

def login(username,password):
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM user WHERE username = %s LIMIT 1"
    val = (username,)
    cursor.execute(sql,val)

    data = cursor.fetchone()

    os.system('cls')
    
    #note : merah = \u001b[31m, hijau : \u001b[32m, putih = \u001b[37m

    if data :
        if(data['password'] == hashlib.md5(password.encode('utf-8')).hexdigest()):
            output = {'status' : True, 'message' : '\u001b[32mLogin Sukses!\u001b[0m'}
        else:
            output = {'status' : False, 'message' : '\u001b[31mPassword salah!\u001b[0m'}
    else:
        output = {'status' : False, 'message' : '\u001b[31mUsername tidak ditemukan !\u001b[0m'}

    return output

def form_login():
    os.system('cls')

    print('\u001b[37m============ Login ============\n')
    while True:
        username     = input("Username : ")
        password = pwinput.pwinput(prompt='Password : ', mask='*')
        cek_login = login(username,password)

        if cek_login['status'] == True:
            print(cek_login['message']+'\n')
            break
        else:
            print(cek_login['message']+'\n')
            continue



