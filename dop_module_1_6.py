grades_ = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
grades_sum = [sum(grades_[0]),sum(grades_[1]),sum(grades_[2]),sum(grades_[3]),sum(grades_[4])]
grades_1 = [ grades_sum[0] / len(grades_[0])]
grades_2 = [grades_sum[1] / len(grades_[1])]
grades_3 = [grades_sum[2] / len(grades_[2])]
grades_4 = [grades_sum[3] / len(grades_[3])]
grades_5 = [grades_sum[4] / len(grades_[4])]
students = {'Jonny','Bilbo','Steve','khendrik','Aaron'}
students_1 = list({'Jonny','Bilbo','Steve','khendrik','Aaron'})
students_1.sort()# сортируем список учеников по алфавиту
delta_ = {students_1[0]: grades_1, students_1[1] :grades_2, students_1[2]: grades_3, students_1[3]:grades_4, students_1[4]:grades_5}
print(delta_)