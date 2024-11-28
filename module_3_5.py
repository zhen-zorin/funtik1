def get_multiplied_digits(number):
    str_number = str(number)
    str_number1 = str_number.replace('0', '')
    first = int(str_number[0])
    if int(len(str_number1)) > 1:
        return  first * get_multiplied_digits(int(str_number1[1:]))
    else:
         return first

result = get_multiplied_digits(40203)
print(result)
result1 = get_multiplied_digits(402030)
print(result1)
