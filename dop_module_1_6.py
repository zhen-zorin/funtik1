grades_ = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
grades_new =[]
grades_1 = [sum(grades_[0]) / len(grades_[0])]
grades_new.append(grades_1[0])
grades_2 = [sum(grades_[1]) / len(grades_[1])]
grades_new.append(grades_2[0])
grades_3 = [sum(grades_[2]) / len(grades_[2])]
grades_new.append(grades_3[0])
grades_4 = [sum(grades_[3]) / len(grades_[3])]
grades_new.append(grades_4[0])
grades_5 = [sum(grades_[4]) / len(grades_[4])]
grades_new.append(grades_5[0])
students = {'Jonny','Bilbo','Steve','Khendrik','Aaron'}
students_1 = list(students)
students_1.sort()# сортируем список учеников по алфавиту
delta_ = dict(zip(students_1, grades_new))

print(delta_)
