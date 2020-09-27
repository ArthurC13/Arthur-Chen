import random                                                                                                   #import random

options = ['R', 'P', 'S']                                                                                       #define a list of possible options
                                                                                                                #print an introduction
print("""
Welcome to Rock, Paper, Scissors!
Please enter 'R' for Rock, 'P' for Paper and 'S' for Scissors
""")

def player_input():                                                                                             #define a function that validates input
    option = input('Please enter your option: ')                                                                #ask for input
    if option in options:                                                                                       #return option if it is one of the options
        return option
    else:                                                                                                       #if option is not one of the options
        print('invlaid input, please try again')
        return player_input()                                                                                   #recall the function to ask for the input again

player = player_input()                                                                                         #call the player_input function
computer = options[random.randint(0,2)]                                                                         #use random to give computer a random option
print('Player:',player,'\nComputer:',computer)                                                                  #print the options of player and computer

wincondition = (player=='R' and computer=='S')or(player=='S' and computer=='P')or(player=='P' and computer=='R')#define win conditions

if player == computer:                                                                                          #print draw if the choices are the same
    print('draw')
elif wincondition:                                                                                              #print player won if the win condition is satisfied
    print('Player won')
else:                                                                                                           #print computer won if it is neither a draw or a win for the player
    print('Computer won')
