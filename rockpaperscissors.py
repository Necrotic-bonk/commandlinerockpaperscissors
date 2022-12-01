import random

rps = ['rock', 'paper', 'scissors']

def game():

    print("TYPE ROCK, PAPER OR SCISSORS IN LOWERCASE!!!")
    userinput = input(print("Rock, paper, scissors?             "))
    answer = random.choice(rps)
    str.lower(userinput)
    print(answer)
    if answer == userinput:
        print("It's a tie!")
    elif userinput == 'rock':
        if answer == 'scissors':
            print("You won!")
        else:
            print("You lost!")
    elif userinput == 'scissors':
        if answer == 'paper':
            print("You won!")
        else:
            print("You lost!")
    elif userinput == 'paper':
        if answer == 'rock':
            print("You won!")
        else:
            print("You lost!")
    else:
        print('Type either rock, paper or scissors!')

game()