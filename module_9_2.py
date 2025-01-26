
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(st) for st in first_strings if len(st) >= 5]
print(first_result) # Список из списка first_strings с длинной строки не мение 5 символов

second_result = [(x, y) for x in first_strings for y in second_strings if len(y) == len(x)]
print(second_result) # Сборка пар слов (кортежей) одной длинны из  first_strings и second_strings

combined_string = first_strings + second_strings
third_result = {s: len(s)for s in combined_string if len(s) % 2 == 0 }
print(third_result) # Словарь (значение строки: длинна строки)
# из  first_strings и second_strings с четной длинной строки