from collections import defaultdict
from Course import *
from Student import *
from Teacher import *

class Education(object):

    dict_of_marks = defaultdict(list) #Словарь с именем студента и его списком всех оценок по всем курсам
    dict_of_average_score = {} #Словарь с именем студента и его средней оценкой
    dict_of_teachers = {} #Словарь с именем преподавателя и его количеством проставленных оценок
    __list_of_students = set() #Множество с id студентов, которые обучаются
    teacher_marks = defaultdict(list) #Словарь с именем преподавателя и списком оценок, которые он поставил
    course_students = defaultdict(list) #Словарь с именем курса и списком студентов, которые на нём обучаются
    teacher_students = defaultdict(set) #Словарь с именем преподавателя и списком учеников, которых он обучает
    teacher_students_count = {} #Словарь с именем преподователя и количеством студентов, которые он обучает

    def __init__(self, course: Course, student: Student, teacher: Teacher):
        self.course = course
        self.student = student
        self.teacher = teacher
        Education.course_students[self.course.course_name].append(self.student.user_name)
        Education.teacher_students[self.teacher.user_name].add(self.student.user_name)
        Education.teacher_students_count[self.teacher.user_name] = len(Education.teacher_students[self.teacher.user_name])
        print(f'Студент {self.student.user_name} зачислен на курс по {self.course}')
        Education.__list_of_students.add(self.student.user_id)
        log.info(f'На образовательную программу {self.course.course_name} был зачислен студент {self.student.user_name}'
                 f'и его учителем становится {self.teacher.user_name} ')

    def point_student_mark(self, value: int) -> None:

        """ Для словаря dict_of_marks функция создает ключ с именем  студента и в качестве значения создает список оценок,
        которые у него есть по всем курсам, на которых он обучается. Аналогично для словаря teacher_marks создает ключ
         с именем преподавателя и в качестве значения создает список оценок, которые он проставил """

        if value in range(1, 6) and isinstance(value, int):
            Education.dict_of_marks[self.student.user_name].append(value)
            Education.teacher_marks[self.teacher.user_name].append(value)
            log.info(f'Для студента {self.student.user_name} была поставлена оценка {value} преподавателем {self.teacher.user_name}'
                     f'по курсу {self.course.course_name}')
        else:
            log.warning(f'Преподавтель {self.teacher.user_name} попытался поставить невалидную оценку {value}')
            print('Оценка должна быть в интервале от 1 до 5')

        # Считает количество оценок, которые поставил конкретный преподаватель
        Education.dict_of_teachers[self.teacher.user_name] = len(Education.teacher_marks[self.teacher.user_name])
        self.get_average_score()
        log.info(f'Для студента {self.student.user_name} автоматически была посчитана средняя оценка')
        self.get_dict_with_students_average_score()

    def get_average_score(self) -> float:

        """ Считает среднюю оценку студента как среднее арифметическое """

        try:
            list_of_marks = Education.dict_of_marks[self.student.user_name]
            average_mark = sum(list_of_marks) / len(list_of_marks)
            return average_mark
        except ZeroDivisionError:
            log.warning(f'Для студента {self.student.user_name}, пытаясь посчитать среднюю оценку получилось деление '
                        f'на 0, то есть еще не заполнили оценки')
            print('Список оценок еще пуст')


    def get_dict_with_students_average_score(self) -> dict:

        """ Для словаря dict_of_average_score функция создает ключ с именем  студента и в качестве значения берёт
        оцеку, которую высчитывает функция get_average_score(), если оценки не проставлены, то функция вернет
        сообщение об этом """

        try:
            Education.dict_of_average_score[self.student.user_name] = self.get_average_score()
            return Education.dict_of_average_score
        except Exception:
            log.warning('Пытаясь получить словарь со студентами и их средней оценкой, предварительно не заполнили '
                        'оценки')
            print('Список оценок еще пуст')

    def get_id_list_of_students(self) -> set:
        return Education.__list_of_students

    def change_teacher(self, val: Teacher) -> None:
        if isinstance(val, Teacher):
            self.teacher = val
        else:
            log.warning(f'Пытаясь поменять учителя {self.teacher.user_name}, в его поле ввели невалидное значение {val}')
            print('Данный объект не является преподавателем')

    @staticmethod
    def generator(dict: dict) -> list:
        l = [i for i in dict.items()]
        l.sort()
        return l[:3]

    @staticmethod
    def generator_reverse(dict: dict) -> list:
        l = [i for i in dict.items()]
        l.sort(reverse=True)
        return l[:3]

    def get_best_students(self) -> list:

        """ Функция возвращает список из первых трех лучших студентов """

        return self.generator_reverse(Education.dict_of_average_score)

    def get_worst_students(self) -> list:

        """ Функция возвращает список из первых трех худших студентов """

        return self.generator(Education.dict_of_average_score)

    def get_active_teachers(self) -> list:

        """ Функция возвращает список из первых трех преподавателей, которые ставят больше всего оценок """

        return self.generator(Education.dict_of_teachers)

    def get_passive_teachers(self) -> list:

        """ Функция возвращает список из первых трех преподавателей, которые ставят меньше всего оценок """

        return self.generator_reverse(Education.dict_of_teachers)

    def get_teacher_with_major_students(self) -> list:

        """ Функция возвращает список из первых трех преподавателей, которые обучают больше всего студентов """

        return self.generator(Education.teacher_students_count)

    def get_teacher_with_minor_students(self) -> list:

        """ Функция возвращает список из первых трех преподавателей, которые обучают меньше всего студентов """

        return self.generator_reverse(Education.teacher_students_count)

    def get_students_courses(self) -> dict:
        return Education.course_students

    def del_student(self) -> None:
        Education.__list_of_students.remove(self.student.user_id)
        Education.course_students[self.course.course_name].remove(self.student.user_name)
        Education.teacher_students[self.teacher.user_name].remove(self.student.user_name)
        log.info(f'Студент {self.student.user_name} был отчислен с курса {self.course.course_name}')
        print(f'Студент {self.student.user_name} отчислен с курса {self.course.course_name}')
        self.student = None


    def __str__(self):
        return f'Студент: {self.student.user_name}; Учитель: {self.teacher.user_name}, Курс: {self.course.course_name}'