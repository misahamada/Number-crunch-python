from random import randint
from random import choice
from time import sleep

def confirm(option):
    confirmed=False
    while confirmed==False:
        confirm_option=input('\nYou have chosen '+option+' mode - continue? ')
        if confirm_option in ['Yes','yes','Y','y']:
            confirmed=True
            return True
        elif confirm_option in ['No','no','N','n']:
            confirmed=True
            return False
        else:
            print('Invalid option, please select difficulty')
            confirmed=False

print('Welcome to Number crunch!')

mode_chosen=False

while mode_chosen==False:
    difficulty_select = input('''\nPlease choose your difficulty: \n1. Easy\n2. Medium\n3. Hard\n''')

    if difficulty_select in ['1','Easy','easy']:
        difficulty = 'Easy'
        mode_chosen=confirm(difficulty)
        upper_add=50
        upper_sub=50
        upper_mult=5
    elif difficulty_select in ['2','Medium','medium']:
        difficulty = 'Medium'
        mode_chosen=confirm(difficulty)
        upper_add=100
        upper_sub=100
        upper_mult=9
    elif difficulty_select in ['3','Hard','hard']:
        difficulty = 'Hard'
        mode_chosen=confirm(difficulty)
        upper_add=500
        upper_sub=500
        upper_mult=50
    else:
        print('Invalid option, please select difficulty')

tasks=int(input('\nHow many tasks do you want? '))

repeat=True
count=1

while repeat==True:

    print('\nRound',count,'-',difficulty,'mode')

    print(difficulty,'mode.',tasks,'tasks. Let the game begin...\n')
    starting_number=randint(1,500)
    operations=['+','-','*']
    integer=True
    print(starting_number,'\n')

    for i in range(tasks):
        operation_choice=choice(operations)
        if operation_choice=='+':
            number=randint(1,upper_add)
            starting_number+=number
            print('Add',number)
            sleep(0.5)
        elif operation_choice=='-':
            number=randint(1,upper_sub)
            starting_number-=number
            print('Subtract',number)
            sleep(0.5)
        elif operation_choice=='*':
            number=randint(1,upper_mult)
            current_number=number*starting_number
            print('Multiply by',number)
            starting_number=current_number
            sleep(0.5)

    print('')
    guess=int(input("What's the answer? "))
    if guess==starting_number:
        print('\nCorrect! Answer is:',starting_number)
        end=input('')
    else:
        print('\nClose! Answer is:',starting_number)
        end=input('')

    repeat=input('\nGo again? ')
    if repeat in ['Yes','yes','y','Y']:
        repeat=True
        count+=1
        print('-------------------------------------------------')
    else:
        repeat=False
        print('\nThanks for playing!')
        input('Press enter to exit')
