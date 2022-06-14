from User import *
import string

class Teacher(User):

    def __init__(self, user_name, science_degree, phone_number, email, scientific_direction):
        super().__init__(user_name)
        self.science_degree = science_degree
        self.phone_number = phone_number
        self.email = email
        self.scientific_direction = scientific_direction

    @property
    def science_degree(self) -> str:
        return self.__science_degree

    @science_degree.setter
    def science_degree(self, value: str) -> None:
        if isinstance(value, str):
            if len(value) < 10:
                s = ''.join(value.split())
                if s.isalpha() == True:
                    self.__science_degree = value
                else:
                    log2.warning(f'Пользователь {self.user_name} в названии научной степени ввел цифры')
                    raise ValueError('В названии научной степени не должно быть цифр')
            else:
                log2.warning(f'Пользователь {self.user_name} в названии научной ввёл слишком много букв')
                raise ValueError('Превышен лимит в 10 букв')
        else:
            raise ValueError('Введите строку')

    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str) -> None:
        if isinstance(value, str) and value.isdigit() == True:
            if len(value) == 10:
                self.__phone_number = value
            else:
                log2.warning(f'Пользователь {self.user_name} ввёл слишком много цифр в номере телефона')
                raise ValueError('Номер телефона должен содержать 10 цифр')
        else:
            log2.warning(f'Пользователь {self.user_name} вместо номера телефона ввёл буквы')
            raise ValueError('В номере телефона должны содержаться только цифры')

    @staticmethod
    def set_email(new_email: str) -> str:

        ''' Данная функция проверяет валидность введеного емэйл адреса по шаблону Abc@mail.com '''

        dog_index = new_email.find('@')
        if isinstance(new_email, str) and new_email.count('@') == 1 and new_email.count('.') == 1 \
                and any(i in string.ascii_letters for i in new_email[dog_index:]) \
                and '.' in new_email[dog_index:] \
                and any(i in string.ascii_letters for i in new_email[:dog_index]):
            return new_email
        else:
            log2.warning(f'Пользователь ввёл невалидный адрес почты ')
            raise ValueError('Невалидный адрес почты')

    @property
    def email(self) -> str:
        return self.__email


    @email.setter
    def email(self, value) -> None:
        self.__email = self.set_email(value)

    @property
    def scientific_direction(self) -> str:
        return self.__scientific_direction

    @scientific_direction.setter
    def scientific_direction(self, value) -> None:

        if isinstance(value, str) and len(value) < 100 and value.isdigit() == False:
            self.__scientific_direction = value
        else:
            log2.warning(f'Пользователь {self.user_name} попытался ввести в поле "Научное направление" из цифр или непонятных символов')
            raise ValueError('Это поле не должно состоять только из цифр')

    def get_info(self) -> None:

        log.info(f'Пользователь {self.user_name} запросил информацию')
        print(f'Имя: {self.user_name}; Научная степень: {self.science_degree}; Рабочий номер телефона: {self.phone_number};'
              f' Адрес почты:  {self.email}; Научное направление: {self.scientific_direction}')