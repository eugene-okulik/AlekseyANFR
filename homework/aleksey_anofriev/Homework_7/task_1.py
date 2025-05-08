a = 6

while True:
    user_input = int(input('Enter count: '))
    if user_input == a:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
        