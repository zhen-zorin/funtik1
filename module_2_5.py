def get_matrix ():
    matrix = []
    a = []
    n = int(input('строки: '))
    m = int(input('столбцы: '))
    value = int(input('Число: '))
    for i in range(0, n) :
        for j in range(0,m) :
            a.append(value)
        matrix.append(a)
        a = []
    return matrix
win = get_matrix()
print(*win)
