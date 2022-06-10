from User import *

class Student(User):

    def __init__(self, user_name: str):

        super().__init__(user_name)
        self._first_name = None
        self._last_name = None
        self._age = None
        self._phone_number = None

    def set_profile(self) -> None:

        log.info(f'Пользователь {self.user_name} решил заполнить свой профиль')
        self._first_name = input('Введите полное имя: ')
        self._last_name = input('Введите фамилию: ')
        age = int(input('Введите год рождения: '))
        month = int(input('Введите месяц рождения: '))
        day = int(input('Введите день рождения: '))
        self._age = datetime.date(age, month, day)
        self._phone_number = input('Введите номер телефона: ')