def SearchResult(matrix,index):
    hasil = []
    for i in range (len(index)):
        hasil += [matrix[index[i]]]
    return hasil