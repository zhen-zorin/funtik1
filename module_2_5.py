def get_matrix (n,m,value):
    matrix = []
    a = []
    for i in range(0, n) :
        for j in range(0,m) :
            a.append(value)
        matrix.append(a)
        a = []
    return matrix
win1 = get_matrix(2,2,10)
win2 = get_matrix(3,5,42)
win3 = get_matrix(4,2,13)
print(*win1)
print(*win2)
print(*win3)
