import datetime
from datetime import timedelta

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

    def set_date(self, year: int, month: int, day: int) -> None:

        self.beginning_date = datetime.date(year, month, day)
        self.ending_date = self.beginning_date + timedelta(days=365)

    def del_course(self) -> None:

        print(f'Курс {self.course_name} удалён')
        Course.list_of_diciplines.remove(self.course_name)
        self.course_name = None
        self.course_id = None
        self.beginning_date = None
        self.ending_date = None

    def __str__(self):
        return f'{self.course_name}'