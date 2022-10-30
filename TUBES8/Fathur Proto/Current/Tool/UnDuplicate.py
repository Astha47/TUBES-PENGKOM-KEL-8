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

# debugging line
#A = [1,3,2,5,3,4,2,5,7,3,5,4,2,7,2,1,6,3,4,1,6,8]
#print(UnDuplicate(A))