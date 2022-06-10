from datetime import timedelta
from User import *

class Course(object):

    list_of_diciplines = set()
    __id = 0

    def __init__(self, course_name: str):

        self.course_name = course_name
        Course.list_of_diciplines.add(self.course_name)
        Course.__id += 1
        self.course_id = Course.__id
        self.beginning_date = None
        self.ending_date = None
        log.info(f'Был создан курс под названием {self.course_name} с id: {self.course_id}')

    def set_date(self, year: int, month: int, day: int) -> None:

        self.beginning_date = datetime.date(year, month, day)
        self.ending_date = self.beginning_date + timedelta(days=365)
        log.info(f'Для курса {self.course_name} была установлена дата начала и окончания')

    def del_course(self) -> None:

        print(f'Курс {self.course_name} удалён')
        Course.list_of_diciplines.remove(self.course_name)
        self.course_name = None
        self.course_id = None
        self.beginning_date = None
        self.ending_date = None
        log.info(f'Курс {self.course_name} был удалён')

    def __str__(self):
        return f'{self.course_name}'