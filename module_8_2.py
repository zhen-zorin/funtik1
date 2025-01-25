

def personal_sum(numbers):
    incorrect_date = 0 # количество некорректных данных
    result = 0 # сумма чисел
    for nam in numbers:
        try:
            result += nam
        except(TypeError):
            incorrect_date += 1
            print(f'Некорректный тип данных для подсчёта суммы - {nam}')
    return result, incorrect_date

def calculate_average(numbers):
    count = 0
    try:
        for i in numbers:
            if type(i) is int:
                count += 1
            else:
                continue
        return (personal_sum(numbers)[0]) / count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Резльтат 2 : {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4 : {calculate_average([42, 15, 36, 13])}')


        

