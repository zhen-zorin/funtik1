def send_email(massage, recipient=[], sender = 'university.help@gmail.com'):
    list_ = ('.com','.ru','.net')
    if sender.endswith(list_) and sender.find('@') and recipient.endswith(list_) and recipient.find('@'):
        if  sender == recipient:
            print('Нельзя отправить письмо самому себе! ')
        elif sender != 'university.help@gmail.com':
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ ! Письмо отправленно с адреса: {sender} на адрес: {recipient}')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса: {sender} на адрес: {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return send_email

send_email('Это сообщение для проверки связи','vasyok1337@gmail.com' )
send_email('Вы видите это сообщениекак лучший студент курса!','urban.fan@mail.ru','urban.info@gmail.com')
send_email('Пожалуйста исправте задание','urban.student@mail.ru','urban.teacher@mail.uk')
send_email('Напоминаю сам себе о семинаре','urban.teacher@mail.ru','urban.teacher@mail.ru')
