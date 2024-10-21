my_dict = {'Sergey': 1999,'Victor': 2007,'Kamila': 2004}
print('Словарь: ',my_dict)
print('Существующая стоимость',my_dict.get('Victor'))
print('Несуществующее значение: ', my_dict.get('Max','Отсутствует'))
my_dict.update({'Vasiliy':1986,'Petr':1993})
print('Удаленное значение', my_dict.pop('Victor'))
print('Измененный словарь',my_dict)
my_set = {'string',4,7,3,7,3,True,'string'}
print('Набор',my_set)
my_set.add('Face')
my_set.add(14)
my_set .discard(True)
print('Модифицированный набор',my_set)