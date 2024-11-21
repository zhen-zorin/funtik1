
list_ = []
n = int(input('Введите число: '))
del_ = []
c = 3
b = 1
a = 1
i = 1
j = 1
while c < n:
    if n % c == 0 :
        del_.append(c)
    c += 1
for i in del_:
    for j in range (1, i):
        for k in range(1, i // 2 + 1):
            if k + j == i and k != j:
                list_.append([k, j])
for b in range(1, n):
    for a in range(1, n // 2+1):
        if b + a == n and a != b:
            list_.append([ a, b])
            continue
result = sorted(list_)
rezult1 = []
for i in result:
    for j in i:
        rezult1.append(j)

print(*rezult1, sep='')
