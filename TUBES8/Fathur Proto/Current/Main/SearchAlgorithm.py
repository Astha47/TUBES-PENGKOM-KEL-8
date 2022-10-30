from unittest import result


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
    Result = SearchResult(matrix,ReArrangeIntIndex(UnDuplicate(SearchEngine(matrix,keyword))))



# debugging line
A = ["klovinki stei", "daniela stei", "fathur zelta", "lorem ipsum", "steve", "awikwok geming","kocak kali aku ini", "nethalie stei"]
search = input("Yang akan dicari: ")
print(SearchResult(A,ReArrangeIntIndex(UnDuplicate(SearchEngine(A,search)))))
#print(SearchEngine(A,"l"))