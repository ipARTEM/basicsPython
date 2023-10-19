
year_of_birth=input('Какой год рождения Пушкина А.С.: ')

while True:
    if year_of_birth=='1799':
        print('Отлично! Вы угадали 1799')
        break
    else:
        print('Вы не угадали. Попробуйте ещё раз: ')
        year_of_birth=input('Какой год рождения Пушкина А.С.: ')