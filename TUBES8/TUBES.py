from ast import Num
import os
import csv
import plistlib

phoneData = []

def Main_Menu():
    print("What do you want to do?")
    print("S) Search for a specific phone number")
    print("L) List all of the phone number")
    print("N) Create new phone data")
    print("D) Delete existing phone data")
    print("E) Edit existing phone data")
    print("Q) Quit")
    print("Input: ",end='')
    opsi = input()
    if opsi.upper() in ['S','L','N','D','E','Q']:
        return opsi.upper()
    else:
        return None

def Sub_Menu():

    Load()
    
    while True:
        opsi = Main_Menu()
        if opsi == 'Q':
            print("Goodbye~")
            break
        elif opsi == 'S':
            Search_Menu()
        elif opsi == 'L':
            List_Menu()
        elif opsi == 'N':
            New_Menu()
        elif opsi == 'D':
            Pilih = input("Which contact do you want to delete?")
            Delete_Menu(Pilih)

        elif opsi == 'E':
            Pilih = input("Which number do you want to edit? ")
            Edit_Menu(Pilih)
        else:
            print("Please input a valid option!")

    Save()

    print(phoneData)

def Search_Menu():
    print("blm jadi")

def List_Menu():
    print(phoneData) #belum selesai

def New_Menu():
    print("Please input new phone data")
    name = input("Enter Name: ")
    num = input("Enter Phone Number: ")
    if not num.isdigit():
        print("Please input numbers only")
        return False
    dummyPhone = [name, num]
    phoneData.append(dummyPhone)

def NumCheck(Pilih):
    if not Pilih.isdigit():
        print("Please input a number")
        return False
    Pilih = int(Pilih)
    if Pilih < 1 or Pilih > len(phoneData):
        print("Please input a correct number")
        return False
    return True
    

def Delete_Menu(Pilih):
    if not NumCheck(Pilih):
        return
    Pilih = int(Pilih)
    del phoneData[Pilih-1]
    print(f"Succesfuly delete phone number{Pilih}")
    
def Edit_Menu(Pilih):
    if not NumCheck(Pilih):
        return
    Pilih = int(Pilih)

    index = phoneData[Pilih-1]
    print("Enter new data for existing phone number")

    print(index[0])
    newname = input("Enter new name: ")
    if newname == "":
        newname = index[0]
    
    print(index[1])
    newnum = input("Enter new number: ")
    if newnum == "":
        newnum = index[1]

    index = [newname, newnum]
    phoneData[Pilih-1] = index

#Fungsi simpan dan save
def Save():
    s = open("PhoneData.csv", 'w', newline='')
    for i in phoneData:
        csv.writer(s).writerow(i)
    s.close()

def Load():
    if os.access("PhoneData.csv",os.F_OK):
        s = open("PhoneData.csv")
        for row in csv.reader(s):
            phoneData.append(row)
        s.close()

if __name__ == '__main__':
    Sub_Menu()


