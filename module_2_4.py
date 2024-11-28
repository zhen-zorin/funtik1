nambers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes =[]
not_primes =[]
for k in nambers:
    if k == 1:
        continue
    is_prime = True
    for j in range (2 , k ):
        if  k % j == 0 :
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        primes.append(k)
    else:
        not_primes.append(k)
print ('Primers: ', primes)
print('Not Primers: ',not_primes)

