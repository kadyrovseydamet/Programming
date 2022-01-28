number = int(input('Введите число: '))
if number % 10 == 0:
    print('У меня ' + str(number),'пирожков')
elif number % 10 == 1:
    print('У меня ' + str(number),'пирожок')
elif number % 10 >= 2 and number % 10 <= 4:
    print('У меня ' + str(number),'пирожка')
elif number % 10 >= 5 and number % 10 <= 20:
    print('У меня ' + str(number),'пирожов')
