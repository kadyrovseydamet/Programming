lista = list(map(int,input('Введите значения цен через пробел ').split()))
lista.sort()
listb = lista[::-1]
print(listb)
