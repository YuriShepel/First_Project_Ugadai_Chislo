from random import *

pop = 0
n = randint(1, 101)
print('Добро пожаловать в числовую угадайку')


def is_valid():
    if x.isdigit() and 1 <= int(x) <= 100:
        return True
    else:
        return False


while True:
    x = input()
    if is_valid() is True:
        x = int(x)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
    if x < n:
        pop = pop + 1
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif x > n:
        pop = pop + 1
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif x == n:
        print('Вы угадали, поздравляем!')
        print('Вы угададли за', pop + 1, 'попыток')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break


