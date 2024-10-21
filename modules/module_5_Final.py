# Дополнительное практическое задание по модулю*
from time import sleep as wait_sec


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    """
    it means the title is the same
    """
    def __ge__(self, other):
        if isinstance(other, Video):
            return self.title.upper() == other.title.upper()
        elif isinstance(other, str):
            return self.title.upper() == other.upper()
        return False

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"'{self.title}'"

    def __iadd__(self, value: int):
        if isinstance(value, int):
            self.time_now += value
        return self

    def matched(self, item: str):
        if isinstance(item, str):
            return self.title.upper().find(item.upper()) >= 0


class User:
    def __init__(self, nickname: str, password: str, age: int = 0):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    """
    it means the nickname is the same
    """
    def __ge__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        return False

    """
    it means the nickname and its password are the same
    """
    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname and self.password == other.password
        else:
            return False

    def __contains__(self, item):
        return item == self

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return self.nickname


class UrTube:
    def __init__(self, users: list = None, videos: list = None):
        if users is None:
            users = []
        self.users = users
        if videos is None:
            videos = []
        self.users = users
        self.videos = videos
        self.current_user = None

    def clone(self):
        return UrTube(self.users, self.videos)

    """
    finding by nickname in users list, returns None if requested user is not found   
    """
    def find_user_by_name(self, user: User) -> User or None:
        for _user in self.users:
            if user >= _user:
                return _user
        return None

    def find_video_by_name(self, video: Video or str) -> Video or None:
        for _video in self.videos:
            if _video >= video:
                return _video
        return None

    def log_in(self, nickname: str, password: str):
        user = User(nickname, password)
        _user = self.find_user_by_name(user)
        if user == _user:
            self.current_user = _user
        elif _user is None:
            print(f"Пользователь {{{nickname}}} не найден")
        else:
            print(f"Пароль для пользователя {{{nickname}}} введён неверный")

    def log_out(self):
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        user = User(nickname, password, age)
        _user = self.find_user_by_name(user)
        if _user is None:
            self.users.append(user)
            self.log_in(user.nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")

    def add(self, *args):
        for arg in args:
            if (isinstance(arg, Video)) and (self.find_video_by_name(arg) is None):
                self.videos.append(arg)

    def get_videos(self, content: str):
        result = []
        for _video in self.videos:
            if _video.matched(content):
                result.append(_video)
        return result

    def watch_video(self, title: str):
        if self.current_user is not None:
            video = self.find_video_by_name(title)
            if video is not None:
                if video.adult_mode and not self.current_user.is_adult():
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    video.time_now = 0
                    while video.time_now < video.duration:
                        wait_sec(1)
                        video += 1
                        print(video.time_now, end=" ")
                    print("Конец видео")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
