from tkinter import *
import csv

import csv

class Phonebook:
    kumpulan = {}
    all = []
    def __init__(self,nama:str,nomortelepon:int):

        self.nama = nama
        self.nomortelepon = nomortelepon
        Phonebook.kumpulan[self.nama] = self.nomortelepon
        Phonebook.all.append(self)

    @classmethod
    def instansiCsv(self):
        with open(r"phonebook.csv",'r') as file:
            pembaca = csv.DictReader(file)
            list_dictionary = list(pembaca)
            for objek in list_dictionary:
                Phonebook(nama = objek['nama'],nomortelepon=int(objek['nomortelepon']))
    
    def __repr__(self):
        return "Phonebook({},{})".format(self.nama,self.nomortelepon)

Phonebook.instansiCsv()

print("Selamat datang dalam prototype dari Phonebook kelompok 8")

def pilihan1():
    ulang = "iya"
    while ulang == "iya":
        nama  = input("Nama orang yang anda cari : ").title()
        if nama in Phonebook.kumpulan.keys():
            print("{} memiliki nomor telepon {}".format(nama,Phonebook.kumpulan[nama]))
            ulang = input("apakah anda ingin mencari nama orang lagi ?(iya/tidak):").lower()
        else:
            print("Maaf, nama tersebut tidak ada !")
            ulang = input("apakah anda ingin mencari nama orang lagi ?(iya/tidak):").lower()
        print("Terima kasih sudah menggunakan program 'mencari orang' ini")

def pilihan2():
    ulang = "iya"
    while ulang == "iya":
        nama  = input("Ketik nama orang yang anda ingin tambahkan ke phonebook : ").title()
        if nama in Phonebook.kumpulan.keys():
            print("Maaf, orang dengan nama '{}' sudah ada di phonebook ini".format(nama))
        else:
            telepon = int(input("Ketik nomor telepon orang tersebut : "))
            if telepon in Phonebook.kumpulan.values():
                index_sama = list(Phonebook.kumpulan.values()).index(telepon)
                print("maaf, nomor telopon tersebut sudah ada, orang dengan nama '{}' memiliki nomor telepon tersebut ".format(list(Phonebook.kumpulan.keys())[index_sama]   ))
            else:
                with open(r'phonebook.csv',"a",newline="") as file:
                    tambahan = (nama,telepon)
                    writer = csv.writer(file)
                    writer.writerow(tambahan)
        ulang = input("Apakah anda ingin menulis nama orang dan nomor telepon lagi ?(iya/tidak):")  
    print("Terima kasih sudah menggunakkan program menulis nomor telepon !")

# ========================= Tkinter

term = "Sebelum main, Silahkan masukkan password dan username anda \n Kondisi :\n Saya berjanji username dan password ini merupakan username dan password punya saya ! \n cobaan ==> Username : marvel , password : 12345\n Kalo udah selesai, tolong close window tkinter nya"

x = term.replace(".","\n")
count = 3

username_passwords = {
    "marvel":"12345"
}


def check_user_pass():
    global count
    if User_name.get() in username_passwords.keys():
        if password.get() == username_passwords[User_name.get()]:
            print("Selamat datang {} !".format(User_name.get()))
            ans = "iya"
            while ans == "iya":
                print("Apa yang anda ingin lakukan ?")
                print("Pilihan-pilihan :")
                print("1.Mencari nomor telepon \n2.Menulis nomor telepon orang")
                pilihan = input("pilihan anda (type angka saja): ")

                if pilihan == "1":
                    pilihan1()
                elif pilihan == "2":
                    pilihan2()
                else:
                    print("maaf, pilihan anda tidak ada di program ini !")
                ans = input("apakah anda ingin menggunakan program lagi ?(iya/tidak): ").lower()
            print("terima kasih sudah menggunakan progam prototype ini")
                
        else:
            print("Password anda salah !!")
            count = count-1
            print("Anda memiliki {} cobaan lagi !".format(count))
    else:
        print("Username Anda salah !")
        count = count - 1
        print("Anda memiliki {} cobaan lagi !".format(count))

    if count == 0:
        print("Cobaan Anda sudah habis !!")
        User_name.config(state=DISABLED)
        password.config(state=DISABLED)
        submit.config(state=DISABLED)
        reset.config(state=DISABLED)
        terms_and_conditions.config(state=DISABLED)

def res():
    User_name.delete(0,END)
    password.delete(0,END)

def permission():
    per = tac.get()
    if per == 0 :
        User_name.config(state=DISABLED)
        password.config(state=DISABLED)
        submit.config(state=DISABLED)
        reset.config(state=DISABLED)
    elif per == 1:
        User_name.config(state=NORMAL)
        password.config(state=NORMAL)
        submit.config(state=NORMAL)
        reset.config(state=NORMAL)
    
web = Tk()
web.geometry("700x500")
web.config(background="#00f2ff")
web.title("Prototype2 phonebook")
tac = IntVar()

User_name = Entry(web,font=("aria",30))
User_name.insert(0,"USERNAME")
User_name.config(state=DISABLED) ##this is so that the User_name entry be disabled first before checking the Terms and condition checkbutton
    ##put state=DISABLED below .insert so that even though disabled, the insert text will still be shown
password = Entry(web,font=("aria",30))
password.insert(0,"PASSWORD")
password.config(state=DISABLED) 
password.config(show="*")

submit = Button(web,text="SUBMIT",font=("aria",10),command = check_user_pass)
submit.config(state=DISABLED)

reset = Button(web,text="RESET",font=("aria",10),command=res)
reset.config(state=DISABLED)


terms_and_conditions = Checkbutton(web,text="I accept the terms and conditions !",font=("aria",10),variable=tac,onvalue=1,offvalue=0,command=permission)

termconditiontext = Label(web,text=x)

User_name.place(x=0,y=100)
password.place(x=0 , y=160)
submit.place(x=0,y=220)
reset.place(x=70,y=220)
terms_and_conditions.place(x=0,y=250)
termconditiontext.place(x=0,y=300)


web.mainloop()
