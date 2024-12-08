from time import sleep

class User:
    def __init__(self, name, password, age):
        self.nickname = name  # Данные пользователя логин, пароль, возраст
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)  # Хеширование пароля


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
        self.new_list = []

    def log_in(self, login='', password=''):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        for i in self.users:
            if nickname == i.nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        new_user =User (nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if not any(v.title == i.title for v in self.videos):
                self.videos.append(i)

    def get_videos(self,move):
        for i in self.videos:
            if move.lower() in i.title.lower():
                ur.new_list.append(i.title)
                return ur.new_list

    def watch_video(self, move):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет покинте страницу')
        elif self.current_user:
            for i in self.videos:
                if move in i.title:
                    for j in range(1,11):
                        print(j, end=' ')
                        sleep(2)
                    print(" Конец видео")

        else:
            print('Войдите в аккаунт, что бы смотреть видео')

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык програмирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень програмист?', 10, adult_mode=True)
    
    # добавление видео
    ur.add(v1, v2)


    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('Для'))
    
    # Проверка на вход пользователя и ворастное ограничение
    ur.watch_video('Для чего девушкам парень програмист?')
    ur.register('vasya_pupkin','lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень програмист?')
    ur.register('urban_pythonist','iScX4vLCLb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень програмист')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi',55)
    print(ur.current_user.nickname)
    
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык прогамирования 2024 года!')

