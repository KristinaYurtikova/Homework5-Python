#Создайте программу для игры с конфетами человек против бота.
#Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
#Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
#Победитель - тот, кто оставил на столе 0 конфет.
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

from random import randint as ri

total_sweet = int(input('Enter number of sweets on the table: '))
take_sweet = 0
pleer_sweet = 0
bot_sweet = 0


def whe_is_first():
        random_number = ri(1,2)
        if random_number == 1:
            pleer_turn()
        else:
            bot_turn()

def pleer_turn():
        global total_sweet
        global take_sweet
        global pleer_sweet
        print(f'Your turn, now on the table {total_sweet} sweets')
        take_sweet = int(input('How many sweets do you want to take? '))
        while take_sweet > 28 or take_sweet < 0  or take_sweet > total_sweet:
            take_sweet = int(input('You take too many sweets!Try again '))
        total_sweet -= take_sweet
        pleer_sweet += take_sweet
        if total_sweet > 0:
            bot_turn()
        else:
            print('You won!')

def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1, 28)
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    print(f'Bot took {take_sweet} sweets! Now on the table {total_sweet} sweets!')
    if total_sweet > 0:
        pleer_turn()
    else:
        print('Bot won!')

whe_is_first()
