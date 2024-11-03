import random

rps = ['rock', 'paper', 'scissors']

def game():
    userinput = input("Type rock, paper or scissors: ").lower()
    answer = random.choice(rps)
    
    print("Computer chose:", answer)
    
    if answer == userinput:
        print("It's a tie!")
        return False
    
    elif (userinput == 'rock' and answer == 'scissors') or \
         (userinput == 'scissors' and answer == 'paper') or \
         (userinput == 'paper' and answer == 'rock'):
        print("You won!")
        return False
    
    elif userinput in rps:
        print("You lost!")
        return False
    
    else:
        print("Invalid input. Please try again.")
        return True

# Loop until a valid game result
while game():
    pass
