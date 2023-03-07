import csv
import os
import time
from secrets import choice

def LoginMainMenu():
    action = True
    errornotification = "   Input yang ada masukkan salah, coba lagi"
    error = False

    while action:
        os.system('cls')
        print("===============================================")
        print("|             LOGIN USER ACCOUNT              |")
        print("===============================================")
        print("|                                             |")
        print("|                 SIGN IN (1)                 |")
        print("|                                             |")
        print("|                 SIGN UP (2)                 |")
        print("|                                             |")
        print("|             DELETE ACCOUNT (3)              |")
        print("|                                             |")
        print("^                                             ^")
        if error:
            print()
            print(errornotification)
        print()
        UserChoice = str(input("                Pilih opsi : "))
        error = False
        if UserChoice == "1" or UserChoice == "2" or UserChoice == "3":
            action = False
        else:
            error = True
    return UserChoice

def SignUp(Accountinfo,Accountpass):
    actionusername = True
    actionpass = True
    error_usernameadded = False
    error_lenPass = False

    while actionusername:
        os.system('cls')
        print("===============================================")
        print("|              ADD USER ACCOUNT               |")
        print("===============================================")
        if error_usernameadded:
            print("|                                             |")
            print("|     *Username tersebut telah digunakan      |")
            print("|         coba gunakan username lain          |")
        print("|                                             |")
        print("|               Input Username                |")
        print("^                                             ^")
        username = input("             : ")
        error_usernameadded = False

        for i in range(len(Accountinfo)):
            if Accountinfo[i] == username:
                error_usernameadded = True

        if error_usernameadded:
            actionusername = True
        else:
            actionusername = False

    while actionpass:
        os.system('cls')
        print("===============================================")
        print("|              ADD USER ACCOUNT               |")
        print("===============================================")
        print("|                                             |")
        if error_lenPass:
            print("|       *Password anda terlalu pendek.        |")
            print("|             Masukkan 8 karakter             |")
        else:
            print("|      *Minimal panjang password adalah       |")
            print("|                  8 karakter                 |")
        print("|                                             |")
        print("|                  Password :                 |")
        print("^                                             ^")
        print("             :",username)
        print(".                                             .")
        print("|               Input Password                |")
        print("^                                             ^")
        password = input("             : ")
        error_lenPass = False

        if len(password)<8:
            error_lenPass = True
        else:
            error_lenPass = False

        actionpass = error_lenPass
    
    # confirmation
    actionconfirmation = True
    errorconfirmation = False
    while actionconfirmation:
        os.system('cls')
        confirmation = ""
        print("===============================================")
        print("|              ADD USER ACCOUNT               |")
        print("===============================================")
        print("|                                             |")
        print("|                 KONFIRMASI                  |")
        print("|                                             |")
        if errorconfirmation:
            print("|             *Input tidak valid               |")
        print("|              Simpan akun ini?               |")
        print("^                                             ^")
        print("             :",username)
        print(".                                             .")
        print("|                   Y or N                    |")
        print("^                                             ^")
        confirmation = input("             : ")
        
        confirmation = confirmation.lower()
        errorconfirmation = False
        if confirmation == "y" or confirmation == "n":
            actionconfirmation = False

    if confirmation == "y":
        for i in range(4):
            os.system('cls')
            print("===============================================")
            print("|              ADD USER ACCOUNT               |")
            print("===============================================")
            print("|                                             |")
            print("|                 Menyimpan:                  |")
            if i == 0:
                print("^           (                    )            ^")
                print("^                     0%                      ^")
                time.sleep(0.5)
            elif i == 1:
                print("^           (======              )            ^")
                print("^                    30%                      ^")
                time.sleep(0.5)
            elif i == 2:
                print("^           (============        )            ^")
                print("^                    60%                      ^")
                time.sleep(1)
            elif i == 3:
                print("^           (====================)            ^")
                print("^                    100%                     ^")
        time.sleep(2)
        Accountinfo = Accountinfo + [username]
        Accountpass = Accountpass + [password]
        
    LoginMenu(Accountinfo,Accountpass)

def SignIn(Accountinfo,Accountpass):
    actionusername = True
    actionpass = True
    error_username = False
    error_Pass = False

    while actionusername:
        os.system('cls')
        print("===============================================")
        print("|            LOG IN USER ACCOUNT              |")
        print("===============================================")
        if error_username:
            print("|                                             |")
            print("|     *Username tersebut tidak ditemukan      |")
            print("|         coba gunakan username lain          |")
        print("|                                             |")
        print("|               Input Username                |")
        print("^                                             ^")
        username = input("             : ")
        error_username = False

        for i in range(len(Accountinfo)):
            if Accountinfo[i] == username:
                UserIndex = i

        if UserIndex:
            actionusername = False
        else:
            actionusername = True

    while actionpass:
        os.system('cls')
        print("===============================================")
        print("|            LOG IN USER ACCOUNT              |")
        print("===============================================")
        if error_lenPass:
            print("|                                             |")
            print("|       *Password anda terlalu pendek.        |")
            print("|             Masukkan 8 karakter             |")
            print("|                                             |")
            print("|                  Username :                 |")
            print("^                                             ^")
            print("             :",username)
            print(".                                             .")
        else:
            print("|                                             |")
            
            print("|      *Minimal panjang password adalah       |")
            print("|                  8 karakter                 |")
            print("|                                             |")
            print("|                  Username :                 |")
            print("^                                             ^")
            print("             :",username)
            print(".                                             .")
        print("|               Input Password                |")
        print("^                                             ^")
        password = input("             : ")
        error_lenPass = False

        if len(password)<8:
            error_lenPass = True
        else:
            error_lenPass = False

        actionpass = error_lenPass
    Accountinfo = Accountinfo + [username]
    Accountpass = Accountpass + [password]

    LoginMenu(Accountinfo,Accountpass)


def SignIn():
    print()

def DelAccount():
    print()

def LoginMenu(Accountinfo,Accountpass):
    select = LoginMainMenu()

    if select == "1":
        IndexAccount = SignIn(Accountinfo,Accountpass)
    elif select == "2":
        SignUp(Accountinfo,Accountpass)
    elif select == "3":
        DelAccount()

    return IndexAccount

Accountinfo = []
Accountpass = []
LoginMenu(Accountinfo,Accountpass)
