import math
#Задание возможно решено правильно

number1 = int(input('Введите 1 координату: '))
number2 = int(input('Введите 2 координату: '))
number3 = int(input('Введите 3 координату: '))
number4 = int(input('Введите 4 координату: '))

otvet = int(number1 ** 2) + int(number2 ** 2)
otvet1 = int(number3 ** 2) + int(number4 ** 2)
print(math.sqrt(otvet + otvet1))
