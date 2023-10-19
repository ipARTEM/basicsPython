
print('Добрый день!')
print('Давайте поиграем в викторину, вам надо угадать год рождения известных людей! ')
input('Готовы?')
while True:
    counter=0
    year=input('Введите год рождения Майкла Блумберга: ')
    if year=='1942':
        counter +=1

    year=input('Введите год рождения Илона Маска: ')
    if year=='1971':
        counter +=1

    year=input('Введите год рождения Джеффа Безоса: ')
    if year=='1964':
        counter +=1

    year=input('Введите год рождения Ларри Эллисона: ')
    if year=='1944':
        counter +=1

    year=input('Введите год рождения Уоррена Баффета: ')
    if year=='1930':
        counter +=1


    print('У вас', counter, 'правильных ответа')

    mistake=5-counter
    print('Вы ошиблись', mistake, 'раз')

    percentage=counter*100/5
    print('Процент правильных ответов: ', percentage, '%',sep='')

    one=input('Хотите сыграть ещё раз? Если да то нажмите "1", если нет любую клавишу: ')
    if one!='1':
        break





