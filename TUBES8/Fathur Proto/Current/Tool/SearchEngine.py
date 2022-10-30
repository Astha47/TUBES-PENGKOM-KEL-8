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
    
# debugging line      
A = ["awikwok","babi","bangsad","aihihihihi","booyaaah"]
print(SearchEngine(A,"A"))