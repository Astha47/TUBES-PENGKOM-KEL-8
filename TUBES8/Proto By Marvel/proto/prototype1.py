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
    
            




    