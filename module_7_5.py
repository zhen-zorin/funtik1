from os import walk
from os.path import join, getmtime, getsize, dirname, abspath
from time import strftime, localtime


directory = '.'

for root, dirs, files in walk(directory):  # для просмотра вложенных директорий ( '.' означает текущая директория)
    for file in files:
        filepath = join(root, file)
        filetime = getmtime(filepath)
        formatted_time = strftime("%d.%m.%Y %H:%M", localtime())
        file_size = getsize(filepath)
        parent_dir = dirname(filepath)
        abs_path = abspath(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}, Абсолютный путь: {abs_path}')
