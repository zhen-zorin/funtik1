from math import inf

def divide(first,second):
    if second == 0 :
         rez = inf
    else:
        rez = first / second
    return rez


exit_  = divide(15 ,0)

print(exit_)