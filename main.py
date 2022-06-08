from Education import *


discipline1 = Course('Julia')
discipline2 = Course('Python')
discipline3 = Course('C++')
student1 = Student('Jonh')
student2 = Student('Max')
student3 = Student('Oleg')
teacher1 = Teacher('Mr.Smith', 'master', '9234837123', 'abc@mail.ru', 'IT')
teacher2 = Teacher('Mrs.Lith', 'PhD', '9134935621', 'abc@mail.com', 'DevOps')



# Примеры проставления оценок
education = Education(discipline1, student1, teacher1)
education.point_student_mark(3)
#
# print(Education.dict_of_marks)

education1 = Education(discipline2, student1, teacher1)
education1.point_student_mark(3)

# print(Education.dict_of_marks)

education2 = Education(discipline3, student1, teacher1)
education2.point_student_mark(3)
# print(Education.dict_of_marks)

education3 = Education(discipline1, student2, teacher2)
education3.point_student_mark(2)
# print(Education.dict_of_marks)

education4 = Education(discipline2, student2, teacher2)
education4.point_student_mark(5)
# print(Education.dict_of_marks)


education5 = Education(discipline3, student2, teacher2)
education5.point_student_mark(5)

education6 = Education(discipline2, student3, teacher1)
education6.point_student_mark(5)

print(Education.dict_of_marks)
# print(education.dict_of_teachers)

print(Education.dict_of_teachers)


# print(education3.get_average_score())
#
# discipline1.set_date(2022, 5, 17)
# print(discipline1.beginning_date)
# print(discipline1.ending_date)

# print(Course.list_of_diciplines)
#
# discipline1.del_course()
# print(Course.list_of_diciplines)

# student1.set_profile()
# print(student1._age)




# print(education.get_average_score())
# print(education)


print(student1.lst_of_users)
print(education.student.find_user_by_id(2))

print(education.get_dict_with_students_average_score())
print(education3.get_dict_with_students_average_score())
print(education6.get_dict_with_students_average_score())

# print(Education.dict_of_average_score)

#
# print(Education.dict_of_average_score)

print(Education.dict_of_teachers)

print(Education.teacher_marks)

print(education.get_id_list_of_students())


teacher1.get_info()




(education5.get_students_courses())

print(Education.course_students)
print(Education.teacher_students)


# education5.del_student()
#
# print(education5.get_id_list_of_students())
# print(Education.course_students)
# print(Education.teacher_students)
#
# print(education5.student)

print(education6.dict_of_teachers)
print(education6.get_active_teachers())
print(education6.get_passive_teachers())

print(education6.get_teacher_with_minor_students())

print(education5.get_best_students())
print(Education.dict_of_average_score)
print(education6.get_worst_students())