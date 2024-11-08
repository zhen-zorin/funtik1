

calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
print(calls)
def string_info():
    string = input('Введите текст: ')
    string_1 = string.upper()
    string_2 = string.lower()
    age = string + string_1 + string_2
    count_calls()
    print(age)
    return age
def is_contains():
    string = input ('Введите строку: ')
    list_to_search = input("Введите список через запятую: ")
    first = string in list_to_search
    count_calls()
    print(first)
    return first
string_info()
is_contains()
print(calls)

