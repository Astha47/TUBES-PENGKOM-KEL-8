from array import array
from ast import Num, While
from asyncio.base_subprocess import WriteSubprocessPipeProto
from unittest import result
import random

# Encription
def LibraryRandomizer(MLib,Mseed):
    NewLib = []
    Loops = int(len(Mseed)/2)
    
    for h in range(Loops):
        for i in range(Mseed[1+(h*2)]):
            for j in range (92-Mseed[h*2]):
                NewLib = NewLib + [MLib[j+Mseed[h*2]]]
            for k in range(Mseed[h*2]):
                NewLib = NewLib + [MLib[k]]
            MLib = NewLib
            NewLib = []
    return MLib

def LibraryRotare(lib):
    newlib = []
    for i in range (91):
        newlib = newlib + [lib[i+1]]
    newlib = newlib + [lib[0]]
    return newlib

def EnigmaMiniEncrypt(matrix):

    # creating seed
    MatrixSeeds = []
    for i in range(4):
        seedA = random.randint(1,20)
        seedB = random.randint(10,92)
        MatrixSeeds = MatrixSeeds +[seedA]+[seedB]
    
    # memecah seed
    SeedAo = []
    for x in range(4):
        SeedAo = SeedAo + [MatrixSeeds[x]]
    
    SeedBo = []
    for x in range(4):
        SeedBo = SeedBo + [MatrixSeeds[x+4]]

    # main library
    A = ['%', '?', '}', 'E', 'W', 'b', '6', 'w', 'A', '4', 'U', '8', 'f', '5', 'T', '@', '*', "'", 'y', '^', ',', '.', '!', ':', '_', 'k', '-', '3', 'v', ';', '1', 'a', 'G', '{', 'J', '2', 'X', 'o', 'c', '0', 'x', 'M', 'z', ']', ' ', 'O', 'B', '9', 'L', '[', '+', 'K', 'V', '|', '(', '/', ')', 'g', 'q', 'p', 'F', 'j', 't', '#', 'm', 'Y', '>', 'P', 'i', 's', '=', 'l', 'S', 'H', '<', 'I', '7', '&', 'R', 'd', 'u', '$', 'Q', 'e', 'C', 'N', 'r', 'Z', 'h', '~', 'D', 'n']
    B = ['k', '8', 'd', 'E', 'f', 'Y', 'a', '?', 'L', '^', '4', '=', '5', ':', 'W', 'N', 'm', 'Q', 'y', 'h', '6', 'J', 'X', 'v', 'U', '#', '}', '$', ']', '<', ')', 'A', 'w', '_', '7', '3', 'M', '1', '*', 'R', 'K', 'j', ' ', '!', 'g', 't', '2', 'l', 'I', 'V', ',', "'", 'b', 'H', 'T', 'Z', 'c', '/', 'z', '+', 'O', 'e', '@', 'r', 'q', '.', 'o', '{', '0', '9', ';', 'G', '%', 'F', '-', '~', 'p', 'x', '[', 'i', '(', 'C', 'n', '&', 'B', 'P', 'D', 'u', '|', '>', 's', 'S']

    # definiting new library by seed
    A = LibraryRandomizer(A,SeedAo)
    B = LibraryRandomizer(B,SeedBo)

    # enrypting
    EncryptedMatrix = []
    for h in range(len(matrix)):
        string = str(matrix[h])
        StringEncrypted = ""
        for i in range (len(string)):
            A = LibraryRotare(A)
            for j in range (92):
                if str(string[i]) == str(A[j]):
                    found = j
                    StringEncrypted = StringEncrypted + str(B[found])
                    break
            
        EncryptedMatrix = EncryptedMatrix + [str(StringEncrypted)] + MatrixSeeds
    
    return EncryptedMatrix

def EnigmaMiniDeEncrypt(matrix):

    # mengambil seeds
    MatrixSeeds = []
    for i in range(8):
        MatrixSeeds = MatrixSeeds + [matrix[len(matrix)-8+i]]
    
    # memecah seed
    SeedAo = []
    for x in range(4):
        SeedAo = SeedAo + [MatrixSeeds[x+4]]
    
    SeedBo = []
    for x in range(4):
        SeedBo = SeedBo + [MatrixSeeds[x]]

    # main library
    A = ['k', '8', 'd', 'E', 'f', 'Y', 'a', '?', 'L', '^', '4', '=', '5', ':', 'W', 'N', 'm', 'Q', 'y', 'h', '6', 'J', 'X', 'v', 'U', '#', '}', '$', ']', '<', ')', 'A', 'w', '_', '7', '3', 'M', '1', '*', 'R', 'K', 'j', ' ', '!', 'g', 't', '2', 'l', 'I', 'V', ',', "'", 'b', 'H', 'T', 'Z', 'c', '/', 'z', '+', 'O', 'e', '@', 'r', 'q', '.', 'o', '{', '0', '9', ';', 'G', '%', 'F', '-', '~', 'p', 'x', '[', 'i', '(', 'C', 'n', '&', 'B', 'P', 'D', 'u', '|', '>', 's', 'S']
    B = ['%', '?', '}', 'E', 'W', 'b', '6', 'w', 'A', '4', 'U', '8', 'f', '5', 'T', '@', '*', "'", 'y', '^', ',', '.', '!', ':', '_', 'k', '-', '3', 'v', ';', '1', 'a', 'G', '{', 'J', '2', 'X', 'o', 'c', '0', 'x', 'M', 'z', ']', ' ', 'O', 'B', '9', 'L', '[', '+', 'K', 'V', '|', '(', '/', ')', 'g', 'q', 'p', 'F', 'j', 't', '#', 'm', 'Y', '>', 'P', 'i', 's', '=', 'l', 'S', 'H', '<', 'I', '7', '&', 'R', 'd', 'u', '$', 'Q', 'e', 'C', 'N', 'r', 'Z', 'h', '~', 'D', 'n']
    
    # definiting new library by seed
    A = LibraryRandomizer(A,SeedAo)
    B = LibraryRandomizer(B,SeedBo)


    EncryptedMatrix = []
    for h in range(len(matrix)-8):
        string = str(matrix[h])
        StringEncrypted = ""
        for i in range (len(string)):
            B = LibraryRotare(B)
            for j in range (92):
                if string[i] == A[j]:
                    found = j
                    break
            StringEncrypted = StringEncrypted + str(B[found])
        EncryptedMatrix = EncryptedMatrix + [str(StringEncrypted)]
    
    return EncryptedMatrix

# Search Algorithm

def ReArrangeIntIndex(index):
    NewIndex = []
    CacheIndex = 0

    while len(NewIndex)<len(index):
        for i in range(len(index)):
            if index[i] == CacheIndex:
                NewIndex += [index[i]]
        
        CacheIndex += 1
    
    return NewIndex

def UnDuplicate(index):
    NewIndex = []
    for i in range(len(index)):
        duplicated = False
        for j in range(len(NewIndex)):
            if index[i] == NewIndex [j]:
                duplicated = True
        if duplicated == False:
            NewIndex += [index[i]]
    return NewIndex

def SearchEngine(matrix,keyword):
    result = []
    index = 0
    found = 0

    for i in range (len(matrix)):
        item = str(matrix[i])
        keyword = str(keyword)
        for j in range (len(item)-len(keyword)+1):
            for k in range (len(keyword)):
                if item[j+k].lower() == keyword[k].lower():
                    index += 1
                    if index == len(keyword):
                        found += 1
                else:
                    index = 0
        if found>0:
            result += [i]
        found = 0
    return result

def SearchResult(matrix,index):
    hasil = []
    for i in range (len(index)):
        hasil += [matrix[index[i]]]
    return hasil

def SearchAlgorithm(matrix,keyword):
    Result = ReArrangeIntIndex(UnDuplicate(SearchEngine(matrix,keyword)))
    return Result

# AccountOrganizer
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

def SignUp(Accountinfo,Accountpass,DataList):
    actionusername = True
    actionpass = True
    error_usernameadded = False
    error_usernameNULL = False
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
        if error_usernameNULL:
            print("|                                             |")
            print("|        *Username tidak boleh kosong         |")
            print("|         coba gunakan username lain          |")
        print("|                                             |")
        print("|               Input Username                |")
        print("^                                             ^")
        username = input("             : ")
        error_usernameadded = False
        error_usernameNULL = False

        if len(username) == 0:
            error_usernameNULL = True
        else:
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
        print("|                    Nama :                   |")
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
        UserData = Accountinfo + Accountpass
        WritingAccountData(UserData)

        # Creating Database
        duplicationdatabase = True
        while duplicationdatabase:
            namecsv = RandomDatabaseNameMaker()
            duplicationdatabase = False
            for i in range(int(len(DataList))):
                if namecsv == DataList[i]:
                    duplicationdatabase = True
                print(namecsv)
            if duplicationdatabase == False:
                CreateNewFile(namecsv)
                DataList += [namecsv]
                print(DataList)
                WritingDatalist(DataList)

    LoginMenu(Accountinfo,Accountpass,DataList)

def SignIn(Accountinfo,Accountpass,DataList):
    actionlogin = True
    actionpass = True
    error_username = False
    error_Pass = False

    while actionlogin:
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

        UserIndex = -1
        for i in range(len(Accountinfo)):
            if Accountinfo[i] == username:
                UserIndex = i

        if UserIndex>=0:
            actionlogin = False
        else:
            actionlogin = True
            error_username = True

    while actionpass:
        os.system('cls')
        print("===============================================")
        print("|            LOG IN USER ACCOUNT              |")
        print("===============================================")
        if error_Pass:
            print("|                                             |")
            print("|            *Password anda salah             |")
            print("|                 Coba lagi!                  |")
        print("|                                             |")
        print("|                  Username :                 |")
        print("^                                             ^")
        print("             :",username)
        print(".                                             .")
        print("|               Input Password                |")
        print("^                                             ^")
        password = input("             : ")
        error_Pass = False

        if password == Accountpass[UserIndex]:
            AccountIndex = UserIndex
            actionpass = False
        else:
            error_Pass = True
    Accountinfo = Accountinfo + [username]
    Accountpass = Accountpass + [password]

    AccountDataLoader(AccountIndex,DataList)

def DelAccount(Accountinfo,Accountpass,DataList):
    actionlogin = True
    actionpass = True
    error_username = False
    error_Pass = False

    while actionlogin:
        os.system('cls')
        print("===============================================")
        print("|            DELETE USER ACCOUNT              |")
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

        UserIndex = -1
        for i in range(len(Accountinfo)):
            if Accountinfo[i] == username:
                UserIndex = i

        if UserIndex>=0:
            actionlogin = False
        else:
            actionlogin = True
            error_username = True

    while actionpass:
        os.system('cls')
        print("===============================================")
        print("|            DELETE USER ACCOUNT              |")
        print("===============================================")
        if error_Pass:
            print("|                                             |")
            print("|            *Password anda salah             |")
            print("|                 Coba lagi!                  |")
        print("|                                             |")
        print("|                  Username :                 |")
        print("^                                             ^")
        print("             :",username)
        print(".                                             .")
        print("|               Input Password                |")
        print("^                                             ^")
        password = input("             : ")
        error_Pass = False

        if password == Accountpass[UserIndex]:
            AccountIndex = UserIndex
            actionpass = False
        else:
            error_Pass = True
    
    # Confirmation
    actconfirmation = True
    errornotification = "   Input yang ada masukkan salah, coba lagi"
    error = False
    while actconfirmation:
        os.system('cls')
        print("===============================================")
        print("|            DELETE USER ACCOUNT              |")
        print("===============================================")
        print("|                                             |")
        print("|     Anda yakin untuk menghapus akun ini?    |")
        print("|                  (Y or N)                   |")
        print("|                                             |")
        print("|                  Username :                 |")
        print("^                                             ^")
        if error:
            print()
            print(errornotification)
        print()
        confirm= input("                    : ")

        confirm = confirm.lower()

        if confirm == "y" or confirm == "n":
            actconfirmation = False

            # Deleting
            if confirm == "y":
                newAccountinfo = []
                for g in range (int(len(Accountinfo))):
                    if g != AccountIndex:
                        newAccountinfo += [Accountinfo[g]]
                Accountinfo = newAccountinfo

                newAccountpass = []
                for h in range (int(len(Accountpass))):
                    if h != AccountIndex:
                        newAccountpass += [Accountpass[h]]
                Accountpass = newAccountpass
            
                # ReWriting
                UserData = Accountinfo + Accountpass
                WritingAccountData(UserData)

                newDataList = []
                for f in range (int(len(DataList))):
                    if f != AccountIndex:
                        newDataList += [DataList[f]]
                DataList = newDataList
                WritingDatalist(DataList)

                # LoadingScreen
                for i in range(4):
                    os.system('cls')
                    print("===============================================")
                    print("|            DELETE USER ACCOUNT              |")
                    print("===============================================")
                    print("|                                             |")
                    print("|                 Menghapus:                  |")
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
        else:
            error = True

    MainProgram()

def LoginMenu(Accountinfo,Accountpass,DataList):
    select = LoginMainMenu()

    if select == "1":
        IndexAccount = SignIn(Accountinfo,Accountpass,DataList)
    elif select == "2":
        SignUp(Accountinfo,Accountpass,DataList)
    elif select == "3":
        DelAccount(Accountinfo,Accountpass,DataList)

    return IndexAccount

def LoadingAccountData():
    UserData = []
    with open("account.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            Raw = row
            code = [Raw[0]]
            for i in range(len(Raw)-1):
                code = code + [int(Raw[i+1])]
            UserData += EnigmaMiniDeEncrypt(code)
    return UserData

def LoadingUserDatalist():
    DataList = []
    with open("datalist.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            Raw = row
            code = [Raw[0]]
            for i in range(len(Raw)-1):
                code = code + [int(Raw[i+1])]
            DataList += EnigmaMiniDeEncrypt(code)
        return DataList

def UserDataLoader(target):
    accountData = []
    with open(target) as file:
        reader = csv.reader(file)
        for row in reader:
            Raw = row
            code = [Raw[0]]
            for i in range(len(Raw)-1):
                code = code + [int(Raw[i+1])]
            accountData += EnigmaMiniDeEncrypt(code)
    return accountData

def WritingAccountData(UserData):
    
    code = []
    for i in range(int(len(UserData))):
        code += [EnigmaMiniEncrypt([UserData[i]])]

    s = open("account.csv", 'w', newline='')
    for i in range (len(code)):
        csv.writer(s).writerow(code[i])
    s.close()

def WritingDatalist(DataList):
    
    code = []
    for i in range(int(len(DataList))):
        code += [EnigmaMiniEncrypt([DataList[i]])]

    s = open("datalist.csv", 'w', newline='')
    for i in range (len(code)):
        csv.writer(s).writerow(code[i])
    s.close()

def RandomDatabaseNameMaker():
    # ini bisa membuat 1,220,096,908,800 variasi, cukup untuk menyimpan kontak selingkuhan anda
    name = ''.join(random.choice("QWERTYUIOPASDFGHJKLZXCVBNM1234567890") for i in range(8))
    name +=".csv"
    return name

def CreateNewFile(string):
    f= open(string,"w+")
    f.close()

# Contact Organizer
def AccountDataLoader(accountIndex,DataList):
    # Loader File
    target = DataList[accountIndex]
    accountData = UserDataLoader(target)
    
    # Separator
    DataName = []
    DataNum = []
    loops = int(len(accountData)/2)
    for i in range(loops):
        DataName = DataName + [accountData[i]]
    for j in range(loops):
        DataNum = DataNum + [accountData[j+loops]]
    # Main menu launcher
    MainMenuController(DataName,DataNum,target)

def AccountDataWriter(NewData,target):
    code = []
    for i in range(int(len(NewData))):
        code += [EnigmaMiniEncrypt([NewData[i]])]

    s = open(target, 'w', newline='')
    for i in range (len(code)):
        csv.writer(s).writerow(code[i])
    s.close()

def MainMenu():
    action = True
    errornotification = "   Input yang ada masukkan salah, coba lagi"
    error = False

    while action:
        os.system('cls')
        print("===============================================")
        print("|                My_PhoneBook                 |")
        print("===============================================")
        print("|                                             |")
        print("|               Buka Kontak (1)               |")
        print("|                                             |")
        print("|            Tambahkan Kontak (2)             |")
        print("|                                             |")
        #print("|               Edit Kontak (3)               |")
        #print("|                                             |")
        #print("|              Hapus Kontak  (4)              |")
        #print("|                                             |")
        print("|                 Log Out  (3)                |")
        print("^                                             ^")
        if error:
            print()
            print(errornotification)
        print()
        UserChoice = str(input("                Pilih opsi : "))
        error = False
        # or UserChoice == "4" or UserChoice == "5"
        if UserChoice == "1" or UserChoice == "2" or UserChoice == "3":
            action = False
        else:
            error = True
    return UserChoice

def OpenContact(DataName,DataNum,target):
    errornotification = "   Input yang ada masukkan salah, coba lagi"
    error = False
    action = True
    while action:
        os.system('cls')
        print("===============================================")
        print("|                BUKA  KONTAK                 |")
        print("===============================================")
        print("|                                             |")
        print("|               Cari Kontak (1)               |")
        print("|                                             |")
        print("|         Tunjukkan Daftar Kontak (2)         |")
        print("|                                             |")
        print("|                Menu Utama (3)               |")
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
    
    # Percabangan
    if UserChoice == "1":
        SearchContact(DataName,DataNum,target)
    elif UserChoice == "2":
        ShowContact(DataName,DataNum,target)
    elif UserChoice == "3":
        MainMenuController(DataName,DataNum,target)
        
def ShowContact(DataName,DataNum,target):
    actionShow = True
    errorInput = False
    if len(DataName) != 0:
        while actionShow:
            os.system('cls')
            print("===============================================")
            print("|               DAFTAR KONTAK                 |")
            print("===============================================")
            print("|                                             |")
            print("^                                             ^")
            for i in range(int(len(DataName))):
                print("   "+str(i+1)+". "+str(DataName[i])+", "+str(DataNum[i])+".")
            print()
            print("   Pilih aksi :")
            print("        [1] Edit Kontak")
            print("        [2] Hapus Kontak")
            print("        [3] Kembali ke Menu Utama")
            print()
            if errorInput:
                print("   *Input tidak valid, coba lagi!")
                print()
            UserChoice = str(input("        Masukkan pilihan Anda : "))
                
            IndexResult = []
            for i in range (len(DataName)):
                IndexResult += [int(i)]
                
            if UserChoice == "1" or UserChoice == "2" or UserChoice == "3":
                action = False
                if UserChoice == "1":
                    EditContact(DataName,DataNum,target,IndexResult)
                elif UserChoice == "2":
                    DeleteContact(DataName,DataNum,target,IndexResult)
                elif UserChoice == "3":
                    MainMenuController(DataName,DataNum,target)
        
    
    else:
        os.system('cls')
        print("===============================================")
        print("|               DAFTAR KONTAK                 |")
        print("===============================================")
        print("|                                             |")
        print("^                                             ^")
        print("   Tidak ada info yang bisa ditampilkan")
        print("Tekan Enter untuk kembali ke menu utama")
        x = input()
        MainMenuController(DataName,DataNum,target)

    

def SearchContact(DataName,DataNum,target):
    action = True
    error = False
    os.system('cls')
    print("===============================================")
    print("|                CARI  KONTAK                 |")
    print("===============================================")
    print("|                                             |")
    print("|              Masukkan Keyword               |")
    print("^                                             ^")
    keyword = input("           : ")

    while action:
        os.system('cls')
        print("===============================================")
        print("|                CARI  KONTAK                 |")
        print("===============================================")
        print("|                                             |")
        print("|              Masukkan Keyword               |")
        print("^                                             ^")
        print("           : "+str(keyword))
        IndexName = SearchAlgorithm(DataName,keyword)
        IndexNum = SearchAlgorithm(DataNum,keyword)
        IndexResult = IndexName + IndexNum
        IndexResult = UnDuplicate(IndexResult)
        if len(IndexResult) != 0:
            print()
            for i in range(int(len(IndexResult))):
                print("   "+str(i+1) + ". " + str(DataName[IndexResult[i]]) + ", " + str(DataNum[IndexResult[i]]))
            print()
            print("   Pilih aksi :")
            print("        [1] Edit Kontak")
            print("        [2] Hapus Kontak")
            print("        [3] Ulangi Pencarian")
            print("        [4] Kembali ke Menu Utama")
            print()
            if error:
                print("        *Pilihan Anda tidak valid, ulangi pilihan Anda!")
                print()
            error = False
            UserChoice = str(input("        Masukkan pilihan Anda : "))
            if UserChoice == "1" or UserChoice == "2" or UserChoice == "3" or UserChoice == "4":
                action = False
                if UserChoice == "1":
                    EditContact(DataName,DataNum,target,IndexResult)
                elif UserChoice == "2":
                    DeleteContact(DataName,DataNum,target,IndexResult)
                elif UserChoice == "3":
                    SearchContact(DataName,DataNum,target)
                elif UserChoice == "4":
                    MainMenuController(DataName,DataNum,target)
            else:
                error = True
        else:
            print()
            print("     Tidak ada info yang bisa ditampilkan")
            print("    Tekan enter untuk kembali ke menu utama")
            haha = input()
            MainMenuController(DataName,DataNum,target)
        print()
       
def EditContact(DataName,DataNum,target,IndexResult):
    action = True
    error = False
    while action:
        os.system('cls')
        print("===============================================")
        print("|                EDIT  KONTAK                 |")
        print("===============================================")
        print("|                                             |")
        print("^                                             ^")

        for i in range(int(len(IndexResult))):
                print("   ["+str(i+1) + "] " + str(DataName[IndexResult[i]]) + ", " + str(DataNum[IndexResult[i]]))
        print()
        if error:
            print("   *Urutan kontak yang anda masukkan")
            print("       tidak valid, coba lagi!")
            print()
        error = True
        KontakTarget = str(input("   Pilih kontak : "))

        ListAvailable = []
        for j in range (len(IndexResult)):
            ListAvailable += [str(j+1)]
        
        for k in range (len(ListAvailable)):
            if KontakTarget == ListAvailable[k]:
                error = False

        if error == False:
            action = False
            editTarget = int(IndexResult[int(KontakTarget)-1])

    actioneditname = True
    NullName = False
    NameUsed = False
    while actioneditname:
        os.system('cls')
        print("===============================================")
        print("|                EDIT  KONTAK                 |")
        print("===============================================")
        print("|                                             |")
        print("^                                             ^")
        print("    Target : "+str(DataName[editTarget])+", "+str(DataNum[editTarget]+"."))
        print()
        if NullName:
            print("    *Nama tidak boleh kosong")
            print()
        if NameUsed:
            print("    *Nama sudah terpakai, coba nama lain!")
            print()
        newcontactname = input("    Nama Baru  : ")

        if len(newcontactname)<1:
            NullName = True
        else:
            NameUsed = False
            for x in range(len(DataName)):
                if newcontactname == DataName[x]:
                    NameUsed = True
            actioneditname = NameUsed
        
    actioneditnum = True
    NullNum = False
    while actioneditnum:
        os.system('cls')
        print("===============================================")
        print("|                EDIT  KONTAK                 |")
        print("===============================================")
        print("|                                             |")
        print("^                                             ^")
        print("    Target : "+str(DataName[editTarget])+", "+str(DataNum[editTarget]+"."))
        print()
        if NullNum:
            print("    *Nomor telepon tidak boleh kosong")
            print()
        print("    Nama Baru  : "+newcontactname)
        newcontactnum = input("    Nomor Baru : ")

        if len(newcontactnum)<1:
            NullNum = True
        else:
            actioneditnum = False
    
    #confirmation

    actionconfirmation = True
    confirerror = False
    while actionconfirmation:
        os.system('cls')
        print("===============================================")
        print("|                EDIT  KONTAK                 |")
        print("===============================================")
        print("|                                             |")
        print("^                                             ^")
        print("    Target : "+str(DataName[editTarget])+", "+str(DataNum[editTarget]+"."))
        print()
        print("    Nama Baru  : "+newcontactname)
        print("    Nomor Baru : "+newcontactnum)
        print()
        if confirerror:
            print("    *Input tidak valid, coba lagi!")
            print()
        confirm = input("    Konfirmasi ? (Y/N) : ")
        confirm = confirm.lower()

        if confirm == "y" or confirm == "n":
            actionconfirmation = False
            if confirm == "y":
                WriteContactDataLoadingScreen()
                DataName[editTarget] = newcontactname
                DataNum[editTarget] = newcontactnum
                # writing
                NewData = DataName + DataNum
                AccountDataWriter(NewData,target)
                MainMenuController(DataName,DataNum,target)
            elif confirm == "n":
                MainMenuController(DataName,DataNum,target)
        else:
            confirerror = True

def DeleteContact(DataName,DataNum,target,IndexResult):
    action = True
    error = False
    while action:
        os.system('cls')
        print("===============================================")
        print("|                HAPUS KONTAK                 |")
        print("===============================================")
        print("|                                             |")
        print("^                                             ^")

        for i in range(int(len(IndexResult))):
                print("   ["+str(i+1) + "] " + str(DataName[IndexResult[i]]) + ", " + str(DataNum[IndexResult[i]]))
        print()
        if error:
            print("   *Urutan kontak yang anda masukkan")
            print("       tidak valid, coba lagi!")
            print()
        error = True
        KontakTarget = str(input("   Pilih kontak : "))

        ListAvailable = []
        for j in range (len(IndexResult)):
            ListAvailable += [str(j+1)]
        
        for k in range (len(ListAvailable)):
            if KontakTarget == ListAvailable[k]:
                error = False
        
        if error == False:
            action = False
            editTarget = int(IndexResult[int(KontakTarget)-1])
    
    #confirmation
    actionconfirmation = True
    confirerror = False
    while actionconfirmation:
        os.system('cls')
        print("===============================================")
        print("|                HAPUS KONTAK                 |")
        print("===============================================")
        print("|                                             |")
        print("^                                             ^")
        print("    Target : "+str(DataName[editTarget])+", "+str(DataNum[editTarget]+"."))
        print()
        if confirerror:
            print("    *Input tidak valid, coba lagi!")
            print()
        confirm = input("    Konfirmasi ? (Y/N) : ")
        confirm = confirm.lower()

        if confirm == "y" or confirm == "n":
            actionconfirmation = False
            if confirm == "y":
                WriteContactDataLoadingScreen()
                # writing
                newDataName = []
                for p in range (len(DataName)):
                    if p != editTarget:
                        newDataName += [DataName[p]]
                newDataNum = []
                for q in range (len(DataNum)):
                    if q != editTarget:
                        newDataNum += [DataNum[p]]
                NewData = newDataName + newDataNum
                DataName = newDataName
                DataNum = newDataNum
                AccountDataWriter(NewData,target)
                MainMenuController(DataName,DataNum,target)
            elif confirm == "n":
                MainMenuController(DataName,DataNum,target)
        else:
            confirerror = True

def AddContact(DataName,DataNum,target):
    actionname = True
    actionnum = True
    error_nameadded = False
    error_nameNULL = False
    error_numNULL = False

    while actionname:
        os.system('cls')
        print("===============================================")
        print("|              TAMBAHKAN KONTAK               |")
        print("===============================================")
        if error_nameadded:
            print("|                                             |")
            print("|       *Nama tersebut telah digunakan        |")
            print("|           coba gunakan nama lain            |")
        if error_nameNULL:
            print("|                                             |")
            print("|          *Nama tidak boleh kosong           |")
            print("|           coba gunakan nama lain            |")
        print("|                                             |")
        print("|                 Input Nama                  |")
        print("^                                             ^")
        name = input("             : ")
        error_nameadded = False
        error_nameNULL = False

        if len(name) == 0:
            error_nameNULL = True
        else:
            for i in range(len(DataName)):
                if DataName[i] == name:
                    error_nameadded = True

            if error_nameadded:
                actionname = True
            else:
                actionname = False

    while actionnum:
        os.system('cls')
        print("===============================================")
        print("|              TAMBAHKAN KONTAK               |")
        print("===============================================")
        if error_numNULL:
            print("|                                             |")
            print("|         *Nomor tidak boleh kosong           |")
            print("|           coba gunakan nama lain            |")
        print("|                                             |")
        print("|                    Nama :                   |")
        print("^                                             ^")
        print("             :",name)
        print(".                                             .")
        print("|                 Input nomor                 |")
        print("^                                             ^")
        number = input("             : ")
        error_nameadded = False
        error_nameNULL = False

        if len(number) == 0:
            error_numNULL = True
        else:
            actionnum = False
    
    # confirmation
    actionconfirmation = True
    errorconfirmation = False
    while actionconfirmation:
        os.system('cls')
        confirmation = ""
        print("===============================================")
        print("|              TAMBAHKAN KONTAK               |")
        print("===============================================")
        print("|                                             |")
        print("|                 KONFIRMASI                  |")
        print("|                                             |")
        if errorconfirmation:
            print("|             *Input tidak valid               |")
        print("|             Simpan kontak ini?              |")
        print("^                                             ^")
        print("             :",name)
        print("             :",number)
        print(".                                             .")
        print("|                   Y or N                    |")
        print("^                                             ^")
        confirmation = input("             : ")
        
        confirmation = confirmation.lower()
        errorconfirmation = False
        if confirmation == "y" or confirmation == "n":
            actionconfirmation = False

    if confirmation == "y":
        WriteContactDataLoadingScreen()
        DataName = DataName + [name]
        DataNum = DataNum + [number]
        NewContactData = DataName + DataNum
        AccountDataWriter(NewContactData,target)
    MainMenuController(DataName,DataNum,target)

def WriteContactDataLoadingScreen():
    for i in range(4):
        os.system('cls')
        print("===============================================")
        print("|           MENYIMPAN DATA KONTAK             |")
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

# Main program
def MainProgram():
    UserData = LoadingAccountData()
    username = []
    password = []
    datalist = LoadingUserDatalist()
    
    for i in range (int(len(UserData)/2)):
        username += [UserData[i]]
    for j in range (int(len(UserData)/2)):
        password += [UserData[int(j+(len(UserData)/2))]]

    LoginMenu(username,password,datalist)

def MainMenuController(DataName,DataNum,target):
    UserChoice = MainMenu()

    if UserChoice == "1":
        OpenContact(DataName,DataNum,target)
    elif UserChoice == "2":
        AddContact(DataName,DataNum,target)
    #elif UserChoice == "3":
        #EditContact(DataName,DataNum,target)
    #elif UserChoice == "4":
        #DeleteContact(DataName,DataNum,target)
    elif UserChoice == "3":
        MainProgram()

# Autorun

MainProgram()