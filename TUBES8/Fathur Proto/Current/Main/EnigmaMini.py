from array import array
import random

#pass = 8 kode
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

"""
Test = ["A","B","C","D"]
Key = [1,2]

print(LibraryRandomizerTest(Test,Key))
"""


"""
ulang = True
while ulang:
    text = input("Yang akan dienkripsi : ")
    matrix = [text]
    enkrip = EnigmaMiniEncrypt(matrix)
    print("Hasil enkrip : ",enkrip)
    print("")
"""
"""

"""
"""
for j in range (3):
    text = input("Yang akan dienkripsi : ")
    matrix = [text]
    enkrip = EnigmaMiniEncrypt(matrix)
    print("Hasil enkrip : ",enkrip)
    print("")
for a in range (3):
    x = []
    a = str(input("Masukkan kode :"))
    x = x + [a]
    for i in range (8):
        a = int(input("Masukkan password ke-"+str(i+1)+" :"))
        x = x + [a]
    print("Terjemahan : ",EnigmaMiniDeEncrypt(x))
    print("")

"""
"""
ulang = True
while ulang:
    text = input("Yang akan dienkripsi : ")
    matrix = [text]
    enkrip = EnigmaMiniEncrypt(matrix)
    print("Hasil enkrip : ",enkrip)
    deenkrip = EnigmaMiniDeEncrypt(enkrip)
    print("Hasil deenkrip : ",deenkrip)
    print()
"""
