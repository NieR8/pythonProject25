UML - диаграмма проекта: https://lucid.app/lucidchart/4893458f-4516-4f8a-8c37-403d17e675a2/edit?viewport_loc=304%2C51%2C2303%2C1191%2CMY5jE6GVud2_&invitationId=inv_acf37ec1-f3fe-46c7-be34-258231a1833c#

Ссылка на скриншот: http://screenshot.ru/upload/images/2022/06/08/LMS4f532e400d1fc1c0.png


Мини - проект MegaLMS: Приложение для управления процессом обучения в школе или на курсах. Задача этой системы хранить в себе всех учащихся, преподавателей, изучаемые дисциплины, учебные группы и оценки, выставляемые на занятиях.

Структура проекта: 
- Базовый класс User, от которого наследуются классы Student и Teacher. Хранит в себе, как атрибут класса, словарь lst_of_users, с ключом - id пользователя, и в качестве значения - имя пользователя ( Пример: {1: 'Mr. Smith'}). Методы: find_user_by_id - ищет пользователя по id.

- Класс Student, наследуется от User. Методы: set_profile - устанавливает значения полей для атрибутов экземпляра класса, которые по умолчанию имеют значение None

- Класс Teacher, наследуется от User. Методы: set_email - валидатор для электронной почты; get_info - выводит информации о преподавателе; для всех полей прописаны сэтеры

- Класс Course. Хранит атрибут класса list_of_disciplines, в котором хранятся названия дисциплин. Методы: set_date - установить дату для начала и окончания курса; del_course - удалить курс

- Класс Education. Связан агрегацией с классами Course, Teacher, Student и хранит в себе их сущности в качестве полей.
Атрибуты класса:
1) dict_of_marks - Словарь с именем студента и его списком всех оценок по всем курсам
2) dict_of_average_score - Словарь с именем студента и его средней оценкой
3) dict_of_teachers - Словарь с именем преподавателя и его количеством проставленных оценок
4) list_of_students - Множество с id студентов, которые обучаются
5) teacher_marks - Словарь с именем преподавателя и списком оценок, которые он поставил
6) course_students - Словарь с именем курса и списком студентов, которые на нём обучаются
7) teacher_students - Словарь с именем преподавателя и списком учеников, которых он обучает
8) teacher_students_count - Словарь с именем преподователя и количеством студентов, которые он обучает

Методы класса:
1) point_student_mark - поставить оценку студенту
2) get_average_score - посчитать среднюю оценку студента по всем имеющимся 
3) get_dict_with_students_average_score - формирует словарь из имени студента и его средней оценки
4) get_id_list_of_students - получить множество с id студентов, которые обучаются
5) change_teacher - поменять учителя на курсе
6) generator - сортирует список по убыванию
7) generator_reverse - сортирует список по возрастанию
8) get_best_students -  получить трех первых лучших студентов на основании их среднего балла
9) get_worst_students - получить трех первых худших студентов
10) get_active_teachers - получить трех первых преподавателя, которые ставят больше всего оценок
11) get_passive_teachers - получить трех первых преподавателя, которые ставят меньше всего оценок
12) get_teacher_with_major_students - получить первых трех преподавателей, которые обучают больше всего студентов
13) get_teacher_with_minor_students - получить первых трех преподавателей, которые обучают меньше всего студентов
14) del_student - отчислить студента с курса

Для запуска проекта создайте нужные сущности и совершайте с ними перечисленные операции.
