"""Финкция принимает название файла - file_name, список строк для записи - strings
Функция записывает в файл 'strings' с новой строки
возвращает словарь с ключём кортежем (<номер строки>, <байт начала строки>)
 и значением <записываемая строка>"""
def custom_write(file_name, strings):
    dict_strings = {}
    strings_positions = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        strings_positions += 1
        cursor = file.tell()
        dict_strings[(strings_positions, cursor)] = string
        file.write(string +'\n')
    file.close()
    return dict_strings
if __name__ =='__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages',
        'Спасибо'
    ]
    rezult = custom_write('write_file.txt', info)
    for wali in rezult.items():
        print(wali)