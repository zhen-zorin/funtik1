def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if int(str_number[-1]) == 0:
        return first * get_multiplied_digits(int(str_number[1:-1]))
    elif int(len(str_number)) <= 1 :
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

   

result = get_multiplied_digits(40203)
print(result)
result1 = get_multiplied_digits(402030)
print(result1)
