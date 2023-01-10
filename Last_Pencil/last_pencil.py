import random


def check_amount_pen():
    global calc
    while True:
        calc = input()
        if not(calc.isdigit()):
            print('The number of pencils should be numeric')
        elif calc == '0':
            print('The number of pencils should be positive')
        else:
            calc = int(calc)
            break


def bot_Jack(lot):
    global pencil
    if lot == 3:
        pencil = '2'
    elif lot == 2 or lot == 1:
        pencil = '1'
    else:
        if lot % 4 == 0:
            pencil = '3'
        elif lot % 4 == 3:
            pencil = '2'
        elif lot % 4 == 2:
            pencil = '1'
        else:
            pencil = random.choice('123')
    print(pencil)


def who_first():
    global NAME
    while True:
        NAME = input()
        if NAME == NAME1 or NAME == NAME2:
            break
        else:
            print("Choose between 'John' and 'Jack'")


def poss_value(NAME):
    global lot
    while True:
        if NAME == NAME1:
            print(f'{NAME}\'s turn!')
            NAME = NAME2
            while True:
                calc = input()
                if calc == '1' or calc == '2' or calc == '3':
                    lot -= int(calc)
                    if lot < 0:
                        print('Too many pencils were taken')
                        lot += int(calc)
                        continue

                    if lot == 0:
                        print(f'{NAME} won!')
                        exit()
                    break
                else:
                    print("Possible values: '1', '2' or '3'")
                    continue
        else:
            print(f'{NAME}\'s turn:')
            bot_Jack(lot)
            lot -= int(pencil)
            NAME = NAME1
            if lot == 0:
                print(f'{NAME} won!')
                exit()
        print('|' * lot)


print('How many pencils would you like to use:')
check_amount_pen()
NAME1 = 'John'
NAME2 = 'Jack'
print(f'Who will be the first ({NAME1},{NAME2}):')
who_first()
amount = print('|' * calc)
lot = calc
poss_value(NAME)
