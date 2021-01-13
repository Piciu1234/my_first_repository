# importing the random module
import random
# importing the time module
import time

# creating variables to save player and computer results
player = 0
computer = 0

# welcoming the player
name = input('Please enter your name: ')
print("Hello", name + ". Let's play \"Paper, rock, scissors\"!")

# in this place player decide how many points needs to win
how_long = int(input('Points needed to win: '))

# creating three variables with messages to make our work easier
tie = 'It is a tie'
lose = 'You lose :('
win = 'You win!'

# creating a while loop (do it as long as player and computer result will not be equal how_long)
while player != how_long and computer != how_long:

    # creating a variable to save result of the game
    result = ()

    # now player is making a choice (paper/rock/scissors)
    print('Make your choice:')
    choice = input()
    # making player choice to lower case
    choice = choice.lower()

    # printing player's choice
    print('Your choice is', choice)

    # waiting for one second
    time.sleep(1)

    # creating list with elements to draw computer_choice
    choices = ['rock', 'paper', 'scissors']

    # drawing a one random element from choices list
    computer_choice = choices[random.randint(0, len(choices) - 1)]

    # printing drawing element (computer_choice)
    print('Computer choice is:', computer_choice)

    # waiting for one second
    time.sleep(1)

    # if player choice there is in choices (list) - make:
    if choice in choices:

        # if player choice is 'rock' - make:
        if choice == 'rock':
            # if computer_choice is 'rock' - make:
            if computer_choice == 'rock':
                # result is tie
                result = tie
            # if computer_choice is 'paper' - make:
            elif computer_choice == 'paper':
                # result is lose
                result = lose
            # if computer_choice is 'scissors' - make:
            elif computer_choice == 'scissors':
                # result is win
                result = win

        # if player choice is 'paper' - make:
        if choice == 'paper':
            # if computer_choice is 'paper' - make:
            if computer_choice == 'paper':
                # result is tie
                result = tie
            # if computer_choice is 'scissors' - make:
            elif computer_choice == 'scissors':
                # result is lose
                result = lose
            # if computer_choice is 'rock' - make:
            elif computer_choice == 'rock':
                # result is win
                result = win

        # if player choice is 'scissors' - make:
        if choice == 'scissors':
            # if computer_choice is 'scissors' - make:
            if computer_choice == 'scissors':
                # result is tie
                result = tie
            # if computer_choice is 'rock' - make:
            elif computer_choice == 'rock':
                # result is lose
                result = lose
            # if computer_choice is 'paper' - make:
            elif computer_choice == 'paper':
                # result is win
                result = win

        # waiting for one second
        time.sleep(1)

        # if result is tie - make:
        if result == tie:
            # print tie ('It is a tie')
            print(tie)

        # if result is win - make:
        if result == win:
            # player points +1
            player += 1
            # print win ('You win!')
            print(win)

        # if result is lose - make:
        if result == lose:
            # computer points +1
            computer += 1
            # print lose ('You lose :(')
            print(lose)

        # waiting for one second
        time.sleep(1)

        # creating a variable score to save the result
        score = f"Result: Player {player} vs. Computer {computer}"
        # printing the score
        print(score)

    # if player choice there is not in choices (list), print:
    else:
        print('Invalid choice, try again.')

    # print it to make the code more readable
    print('='*25)

# if player result is bigger than computer result - make:
if player > computer:
    # print ('You win this game :) \nNice!!!')
    print('You win this game :) \nNice!!!')

# if computer result is bigger than player result - make:
else:
    # paint ('You lose the game :( \nSorry...')
    print('You lose the game :( \nSorry...')
