from abc import ABC
import datetime
import logging

log = logging.getLogger(__name__)
log2 = logging.getLogger('warn')
log.setLevel(logging.INFO)
handler = logging.FileHandler('logs.txt')
handler2 = logging.FileHandler('warnings.txt')
handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
handler2.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
log.addHandler(handler)
log2.addHandler(handler2)

class User(ABC):

    __id = 0
    lst_of_users = {} #Словарь с id пользователя и его именем

    def __init__(self, user_name: str):

        User.__id += 1
        self.user_name = user_name
        self.user_id = User.__id
        self.register_date = datetime.datetime.now()
        User.lst_of_users[self.user_id] = self.user_name

    @property
    def user_name(self) -> str:
        return self.__user_name

    @user_name.setter
    def user_name(self, val: str) -> None:
        if val not in User.lst_of_users.values():
            self.__user_name = val
            log.info(f'Пользователь задал имя {val}')
        else:
            log2.warning('Пользователь попытался ввести имя, которое уже занято')
            raise ValueError('Имя уже занято')



    def find_user_by_id(self, id: int) -> str:

        """ Поиск имя пользователя по id """

        if id in User.lst_of_users.keys():
            log.info(f'Пользователь {self.user_name} попытался найти имя другого пользователя по id:{id} ')
            return User.lst_of_users[id]
        else:
            log.info(f'Пытаясь найти пользователя, пользователь {self.user_name} ввел несуществующий id')
            raise KeyError('Нет такого id')

    def __str__(self):
        return f'{self.user_name}'