from random import randint

number = randint(0, 10)
print('У вас три попытки отгадать число')
for i in range (3):
    c = int(input('Введите число: '))
    if number < c:
        print('Загаданное число меньше')
    elif number > c:
        print('Загаданное число больше')
    elif c == number:
        print('Вы выиграли')
        break
else:
    print('Вы проиграли')
