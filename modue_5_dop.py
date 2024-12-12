from time import sleep

class User:
    def __init__(self, name, password, age):
        self.nickname = name  # Данные пользователя логин, пароль, возраст
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title  # Заголовок
        self.duration = duration  # Продолжительность
        self.time_now = time_now  # Секунда остановки
        self.adult_mode = adult_mode  # Ограничение по возрасту

class UrTube:
    def __init__(self):
        self.users = []  # Список объектов User
        self.videos = []  # Список объектов видео
        self.current_user = None  # Текуший пользователь

    def log_in(self, nickname, password):
        for user in self.users:
            if self.nickname == user.nickname and self.password == user.password:
                self.current_user = user
                return print(f'Ползователь {nickname} совепшил успешный вход.')
            else:
                return print(f'Данные {nickname} и пароль не совподают. \n Попробуйте ещё раз.')

    def register(self, nickname, password, age):
        new_user = []
        for i in self.users:
            if nickname == i.nickname:
                if hash(password) == i.password:
                    return print(f'Пользователь {nickname} успешно вошел в систему')
                    continue
                else:
                    return print(f'Неверная пара логин {nickname} пароль')
                    break
        new_user = User(nickname, hash(password), age)
        self.users.append(new_user)
        self.current_user = new_user
        return self.current_user, print(f'Регистрация "{new_user.nickname}" прошла успешно')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if not any(v.title == i.title for v in self.videos):
                self.videos.append(i)
                return print(f'Видео "{i.title}" успешно добавилось ')
            else:
                return print("Такое видео уже существует")

    def get_videos(self, move):
        new_list = []
        for i in self.videos:
            if move.lower() in i.title.lower():
                if i.title not in new_list:
                    new_list.append(i.title)
                else:
                    return print('Названий с заданным фрагментом не найдено.')
        return new_list

    def watch_video(self, move):
        if self.current_user == None:
            return print('Войдите в аккаунт, что бы смотреть видео')
        else:
            for i in self.videos:
                if move == i.title:
                    if i.adult_mode == True and self.current_user.age < 18:
                        return print('Вам нет 18 лет покинте страницу')
                    else:
                        for j in range(1, 11):
                            print(j, end=' ')
                            sleep(1)
                        return print(" Конец видео")
            return print("Нет такого видео")

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык програмирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень програмист?', 10, adult_mode=True)
    
    # добавление видео
    ur.add(v1)
    ur.add(v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    
    # Проверка на вход пользователя и ворастное ограничение
    ur.watch_video('Для чего девушкам парень програмист?')
    ur.register('vasya_pupkin','lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень програмист?')
    ur.register('urban_pythonist','iScX4vLCLb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень програмист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi',55)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык прогамирования 2024 года!')

    # проверка повторного входа
    ur.register('urban_pythonist','iScX4vLCLb9YQavjAgF', 25)
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)