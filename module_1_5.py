immutable_var = (1,2,3,4,True,'module')
print(immutable_var) #
#mmimmutable_var[0] = 50# ошибка оъект "кортеж" не поддерживает назначение элементов
mutable_list = ['banana','string',False,72]
mutable_list[1] ='peach'
mutable_list.append('coconut')
mutable_list.remove(72)
print(mutable_list)