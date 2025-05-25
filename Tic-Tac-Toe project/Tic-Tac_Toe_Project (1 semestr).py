import sys
import turtle
x_list = []
o_list = []

names = []
wins = []
losses = []
ties = []
all_games = []

player_1 = 'Player_1'
player_2 = 'Player_2'

count_1 = 0
count_2 = 0
tie_count_1 = 0
tie_count_2 = 0

def x():
    a.pendown()
    a.rt(45)
    a.fd(26)
    a.bk(52)
    a.fd(26)
    a.lt(90)
    a.fd(26)
    a.bk(52)
    a.fd(26)
    a.rt(45)

def o():
    a.fd(18)
    a.lt(90)
    a.pendown()
    a.circle(18)
    a.penup()
    a.rt(90)
    a.bk(18)

def board():
    a.fillcolor('light green')
    a.begin_fill()
    for i in range(4):
        a.fd(150)
        a.lt(90)
    a.end_fill()
    a.fd(50)
    a.lt(90)
    a.fd(150)
    a.rt(90)
    a.fd(50)
    a.rt(90)
    a.fd(150)
    for i in range(2):
        a.lt(90)
        a.fd(50)
    a.lt(90)
    a.fd(150)
    a.rt(90)
    a.fd(50)
    a.rt(90)
    a.fd(150)

def Vline(x):
    a.pensize(4)
    a.penup()
    a.setposition(x, 150)
    a.pendown()
    a.rt(90)
    a.fd(150)
    a.lt(90)
    a.pensize(2)

def Hline(x):
    a.pensize(4)
    a.penup()
    a.setposition(0, x)
    a.pendown()
    a.fd(150)
    a.pensize(2)

def give_name():
    global player_1
    global player_2
    give = input("Will you change nicknames of Players? (yes/no): ").lower()
    if give == 'yes':
        player_1 = input('Give nickname to Player_1: ')
        player_2 = input('Give nickname to Player_2: ')
    elif give != 'no':
        print("Please write yes or no!")
        give_name()

def win_horizontal():
    global count_1
    global count_2
    if 1 in x_list and 2 in x_list and 3 in x_list:
        print(f'{player_1.upper()} is winner!')
        count_1 = 1
        Hline(125)
        one_more()
    elif 4 in x_list and 5 in x_list and 6 in x_list:
        print(f'{player_1.upper()} is winner!')
        count_1 = 1
        Hline(75)
        one_more()
    elif 7 in x_list and 8 in x_list and 9 in x_list:
        print(f'{player_1.upper()} is winner!')
        count_1 = 1
        Hline(25)
        one_more()
    if 1 in o_list and 2 in o_list and 3 in o_list:
        print(f'{player_2.upper()} is winner!')
        count_2 = 1
        Hline(125)
        one_more()
    elif 4 in o_list and 5 in o_list and 6 in o_list:
        print(f'{player_2.upper()} is winner!')
        count_2 = 1
        Hline(75)
        one_more()
    elif 7 in o_list and 8 in o_list and 9 in o_list:
        print(f'{player_2.upper()} is winner!')
        count_2 = 1
        Hline(25)
        one_more()

def win_vertical():
    global count_1
    global count_2
    if 1 in x_list and 4 in x_list and 7 in x_list:
        print(f'{player_1.upper()} is winner!')
        count_1 = 1
        Vline(25)
        one_more()
    elif 2 in x_list and 5 in x_list and 8 in x_list:
        print(f'{player_1.upper()} is winner!')
        count_1 = 1
        Vline(75)
        one_more()
    elif 3 in x_list and 6 in x_list and 9 in x_list:
        print(f'{player_1.upper()} is winner!')
        count_1 = 1
        Vline(125)
        one_more()
    if 1 in o_list and 4 in o_list and 7 in o_list:
        print(f'{player_2.upper()} is winner!')
        count_2 = 1
        Vline(25)
        one_more()
    elif 2 in o_list and 5 in o_list and 8 in o_list:
        print(f'{player_2.upper()} is winner!')
        count_2 = 1
        Vline(75)
        one_more()
    elif 3 in o_list and 6 in o_list and 9 in o_list:
        print(f'{player_2.upper()} is winner!')
        count_2 = 1
        Vline(125)
        one_more()

def win_diagonal():
    global count_1
    global count_2
    if 1 in x_list and 5 in x_list and 9 in x_list:
        print(f'{player_1.upper()} is winner!')
        count_1 = 1
        a.pendown()
        a.pensize(4)
        a.setposition(-10, 160)
        a.rt(45)
        a.fd(240)
        a.penup()
        a.lt(45)
        a.pensize(2)
        one_more()
    elif 3 in x_list and 5 in x_list and 7 in x_list:
        print(f'{player_1.upper()} is winner!')
        count_1 = 1
        a.pendown()
        a.pensize(4)
        a.setposition(160, 160)
        a.rt(135)
        a.fd(240)
        a.penup()
        a.lt(135)
        a.pensize(2)
        one_more()
    if 1 in o_list and 5 in o_list and 9 in o_list:
        print(f'{player_2.upper()} is winner!')
        count_2 = 1
        a.pendown()
        a.pensize(4)
        a.setposition(-10, 160)
        a.rt(45)
        a.fd(240)
        a.penup()
        a.lt(45)
        a.pensize(2)
        one_more()
    elif 3 in o_list and 5 in o_list and 7 in o_list:
        print(f'{player_2.upper()} is winner!')
        count_2 = 1
        a.pendown()
        a.pensize(4)
        a.setposition(160, 160)
        a.rt(135)
        a.fd(240)
        a.penup()
        a.lt(135)
        a.pensize(2)
        one_more()

def check_tie():
    global tie_count_1
    global tie_count_2
    if len(x_list) >= 5:
        print('No one wins, this is TIE!')
        tie_count_1 = 1
        tie_count_2 = 1
        one_more()

def results():
    global count_1
    global count_2
    global tie_count_1
    global tie_count_2
    if player_1.lower() not in names:
        names.append(player_1.lower())
        wins.append(0)
        losses.append(0)
        all_games.append(0)
        ties.append(0)
    if player_2.lower() not in names:
        names.append(player_2.lower())
        wins.append(0)
        losses.append(0)
        all_games.append(0)
        ties.append(0)
    wins[names.index(player_1.lower())] += count_1
    wins[names.index(player_2.lower())] += count_2
    ties[names.index(player_1.lower())] += tie_count_1
    ties[names.index(player_2.lower())] += tie_count_2
    tie_count_1 = 0
    tie_count_2 = 0
    count_1 = 0
    count_2 = 0
    all_games[names.index(player_1.lower())] = all_games[names.index(player_1.lower())] + 1
    losses[names.index(player_1.lower())] = all_games[names.index(player_1.lower())] - wins[names.index(player_1.lower())] - ties[names.index(player_1.lower())]
    all_games[names.index(player_2.lower())] = all_games[names.index(player_2.lower())] + 1
    losses[names.index(player_2.lower())] = all_games[names.index(player_2.lower())] - wins[names.index(player_2.lower())] - ties[names.index(player_2.lower())]
    for i in range(len(names)):
        print(f"{names[i].upper()}: all games -> {all_games[names.index(names[i].lower())]}   wins -> {wins[names.index(names[i].lower())]}   losses -> {losses[names.index(names[i].lower())]}   ties -> {ties[names.index(names[i].lower())]}")

def one_more():
    results()
    oneMore = input('One more game? (yes/no): ').lower()
    if oneMore == 'yes':
        a.clear()
        a.penup()
        a.setposition(0, 0)
        a.pendown()
        board()
        give_name()
        for i in range(len(x_list)):
            x_list.pop(0)
        for i in range(len(o_list)):
            o_list.pop(0)
        while True:
            player_1_input()
            win_vertical()
            win_horizontal()
            win_diagonal()
            check_tie()
            player_2_input()
            win_vertical()
            win_horizontal()
            win_diagonal()
            check_tie()
    elif oneMore == 'no':
        print('So, game has finished! 😎 ')
        sys.exit()
    else:
        print('Can you please answer correctly!')
        one_more()

def player_1_input():
    try:
        inp_1 = int(input(f"{player_1}'s turn to put x (1-9): "))
        if 1 <= inp_1 and inp_1 <= 9 and inp_1 not in x_list and inp_1 not in o_list:
            x_list.append(inp_1)
            if inp_1 == 1:
                a.penup()
                a.setposition(25, 125)
                x()
            elif inp_1 == 2:
                a.penup()
                a.setposition(75, 125)
                x()
            elif inp_1 == 3:
                a.penup()
                a.setposition(125, 125)
                x()
            elif inp_1 == 4:
                a.penup()
                a.setposition(25, 75)
                x()
            elif inp_1 == 5:
                a.penup()
                a.setposition(75, 75)
                x()
            elif inp_1 == 6:
                a.penup()
                a.setposition(125, 75)
                x()
            elif inp_1 == 7:
                a.penup()
                a.setposition(25, 25)
                x()
            elif inp_1 == 8:
                a.penup()
                a.setposition(75, 25)
                x()
            elif inp_1 == 9:
                a.penup()
                a.setposition(125, 25)
                x()
        elif inp_1 in x_list or inp_1 in o_list:
            print('This spot is NOT EMPTY!')
            player_1_input()
        else:
            print('Please write the number (1-9)!')
            player_1_input()
    except ValueError:
        print("Please write the number (1-9)!")
        player_1_input()

def player_2_input():
    try:
        inp_2 = int(input(f"{player_2}'s turn to put O (1-9): "))
        if 1 <= inp_2 and inp_2 <= 9 and inp_2 not in x_list and inp_2 not in o_list:
            o_list.append(inp_2)
            if inp_2 == 1:
                a.penup()
                a.setposition(25, 125)
                o()
            elif inp_2 == 2:
                a.penup()
                a.setposition(75, 125)
                o()
            elif inp_2 == 3:
                a.penup()
                a.setposition(125, 125)
                o()
            elif inp_2 == 4:
                a.penup()
                a.setposition(25, 75)
                o()
            elif inp_2 == 5:
                a.penup()
                a.setposition(75, 75)
                o()
            elif inp_2 == 6:
                a.penup()
                a.setposition(125, 75)
                o()
            elif inp_2 == 7:
                a.penup()
                a.setposition(25, 25)
                o()
            elif inp_2 == 8:
                a.penup()
                a.setposition(75, 25)
                o()
            elif inp_2 == 9:
                a.penup()
                a.setposition(125, 25)
                o()
        elif inp_2 in x_list or inp_2 in o_list:
            print('This spot is NOT EMPTY!')
            player_2_input()
        else:
            print('Please write the number (1-9)!')
            player_2_input()
    except ValueError:
        print("Please write the number (1-9)!")
        player_2_input()

print("Hello, this is TIC-TAC-TOE game :) ")
print("So, game will be started after giving the nicknames to Players!")
give_name()
a = turtle.Turtle()
a.pensize(2)
a.speed(0)
print(a)
board()
while True:
    player_1_input()
    win_vertical()
    win_horizontal()
    win_diagonal()
    check_tie()
    player_2_input()
    win_vertical()
    win_horizontal()
    win_diagonal()
    check_tie()
turtle.mainloop()