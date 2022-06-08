from abc import ABC
import datetime

class User(ABC):

    __id = 0
    lst_of_users = {}

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
        else:
            raise ValueError('Имя уже занято')

    def find_user_by_id(self, id: int) -> str:

        """ Возвращает имя пользователя """

        if id in User.lst_of_users.keys():
            return User.lst_of_users[id]
        else:
            raise KeyError('Нет такого id')

    def __str__(self):
        return f'{self.user_name}'