import string

class WordsFinder:
    def __init__(self, *file_name):
        self.file_list = file_name

    def get_all_words(self):
        all_words ={} #Конечный словарь вида <имя файла>:<перебранная строка>
        list_string =[] # Список строк содержащихся в файле
        for fili in self.file_list:# Перебираем список названий файлов и по очереди их открывааем
            with open(fili,'r', encoding='utf-8') as file1:
                rem1 = ''
                for rem in file1: # перебираем строки в файле
                    rem1 = rem1 + rem.strip().lower()  # Удаляем знаки припинания, Удаляем перенос строки.
                list_string.append(rem1.translate(str.maketrans('', '', string.punctuation)))
            for listr in list_string:
                qiwi = listr.split()
                all_words.update({ fili: qiwi})
        return all_words

    def find(self,word):# word искомое слово в значениях.
        global dict_word, list_keys
        dict_word = self.get_all_words()# словарь вида <имя файла>:<перебранная строка>
        list_keys = dict_word.keys() # Список ключей
        self.word = word.lower()

        rezult = [] # список словарей
        for key in list_keys:
            if self.word not in dict_word.get(key):
                continue
            else:
                rezult.append({key : dict_word.get(key).index(self.word ) +1})
        return rezult

    def count(self,word):
        self.word = word.lower()
        rezult1 =[]
        for key in list_keys:
            if self.word not in dict_word.get(key):
                continue
            else:
                rezult1.append({key : dict_word.get(key).count(self.word )})
        return rezult1

if __name__ =='__main__':
    finder1 =WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
    print(finder1.get_all_words())
    print(finder1.find('TEXT'))
    print(finder1.count('teXT'))
