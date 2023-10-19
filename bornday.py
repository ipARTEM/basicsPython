year_of_birth = input('Какой год рождения Пушкина А.С.: ')

while True:
    if year_of_birth == '1799':
        print('Отлично! Вы угадали 1799')
        birthday = input('А какой день рождения: ')

        while True:
            if birthday == '6':
                print('Ура, вы удагадали! Пушкин А.С. родился 6 июня 1799')
                break

            else:
                print('Вы не угадали. Попробуйте ещё раз: ')
                birthday = input('Какой день рождения: ')
        break

    else:
        print('Вы не угадали. Попробуйте ещё раз: ')
        year_of_birth = input('Какой год рождения Пушкина А.С.: ')
