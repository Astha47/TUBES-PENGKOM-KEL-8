def ReArrangeIntIndex(index):
    NewIndex = []
    CacheIndex = 0

    while len(NewIndex)<len(index):
        for i in range(len(index)):
            if index[i] == CacheIndex:
                NewIndex += [index[i]]
        
        CacheIndex += 1
    
    return NewIndex

# debugging line
#A = [1,4,6,3,2,5,9,7,8]
#print(ReArrangeIndex(A))