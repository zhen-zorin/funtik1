def print_params(a= 1,b= 'строка',c = True):
    print(a,b,c)
print_params(3, 5, False)
print_params(b=25, c =4)
print_params(2, c=[1,2,3,])
print_params()
values_list = (2, True, 'Пирожок')
values_dict = { 'a' : 7, 'b' : 'Метель', 'c': True}

print_params(*values_list)
print_params(**values_dict)
values_list_2 = [3,'hello']
print_params(*values_list_2,42)