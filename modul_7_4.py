team1_num = 5 # число участников, команда 1 Мастера кода, команда 2 Волшебники данных
team2_num = 6
score_1 = 40
score_2 = 42 # Количество решенных задач
team1_time = 18015.2 # Время за которое команда 2 решила задачи
team2_time = 1552.512
tasks_total = score_1 + score_2
time_age = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'победа команды Мастера кода !'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'победа команды Волшебники данных !'
else:
    challenge_result = 'ничья'
print('"В команде Мастера кода участников: %d !"' % team1_num)
print('"Итого сегодня в командах участников: %d и %d !"' % (team1_num, team2_num))

print('"Команда Волшебники данных решила задач: {} !"'.format(score_2))
print('"Волшебники данных решили задачи за {} c !"'.format(team1_time))

print(f'"Команды решили {score_1} и {score_2} задач."')
print(f'"Результат битвы: {challenge_result} !"')
print(f'"Сегодня было решено {tasks_total} задач, в среднм по {time_age} секунды на задачу!"')