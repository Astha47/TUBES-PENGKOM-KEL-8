from operator import mod
import random


matrix = ["1","2","3","4","5","6","7","8","9","0","-","=","q","w","e","r","t","y","u","i","o","p","[","]","a","s","d","f","g","h","j","k","l",";","'","z","x","c","v","b","n","m",",",".","~","/","!","@","#","$","%","^","&","*","(",")","_","+","Q","W","E","R","T","Y","U","I","O","P","{","}","|","A","S","D","F","G","H","J","K","L",":","Z","X","C","V","B","N","M","<",">","?"," "]
print(len(matrix))


def RandomizeArray(matrix):
    NewMatrix = []
    IndexWR = []
    while len(NewMatrix)<len(matrix):

        x = random.randint(0,91)

        #print("didapat x :", x)

        repeated = 0
        for j in range (len(IndexWR)):
            #print("perulangan ke",j)
            #print("Index terpakai :",IndexWR)
            #print("panjang IndexWR : ",len(IndexWR))
            if len(IndexWR)>0:
                if IndexWR[j] == x:
                    #print("perulangan terdeteksi")
                    repeated = 1
    
        if repeated == 0:
            NewMatrix = NewMatrix + [matrix[x]]
            IndexWR = IndexWR + [x]
    


    return NewMatrix
"""
newmatrix = RandomizeArray(RandomizeArray(RandomizeArray(RandomizeArray(RandomizeArray(RandomizeArray(RandomizeArray(RandomizeArray(matrix))))))))
#print(matrix)
print(newmatrix)
print(len(newmatrix))
"""
NewMatrix = RandomizeArray(matrix)
print(NewMatrix)
print(len(NewMatrix))
print(len(matrix))