calls = 0
def count_calls():
    global calls
    calls +=  1
    return calls

def string_info(string):
    count_calls()
    string_1 = string.upper()
    string_2 = string.lower()
    return len(string), string_1, string_2

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() in string.lower() or string.lower() in i.lower():
            return True
        else:
            return False



rez1 = string_info('CAPYBARA')
rez2 = string_info('Armageddon')
is_rez1 = is_contains('Urban',['ban','BaNaN','urBAN'])
is_rez2 = is_contains('cycle',['recycling','cyclic'])

print(rez1)
print(rez2)
print(is_rez1)
print(is_rez2)
print(calls)



