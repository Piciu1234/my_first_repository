# importing the random module
import random
# and the time module
import time

# welcoming the player
name = input('Please enter your name: ')

print('Hello,', name + '. Welcome in our game.')

# drawing a one random number from 1 to 25
number = random.randint(1, 25)

# creating variable to save player number
guess = 0

# creating variable with number of tries to guess the number
tries = 6

# creating a while loop
while guess != number:

    # in this place the player is entering the guessing number
    guess = int(input('Guess the number (1 - 25): '))

    # waiting for one second
    time.sleep(1)

    # if the number is correct, print: 'You won!'
    if guess == number:
        print('You won!')

    # if the guessing number is too few, print: 'Too few'
    elif guess < number:
        print('Too few')
        # inform the player about the number of tries
        print('You have got', tries, 'tries.')

    # if the guessing number is too much, print: 'Too much'
    elif guess > number:
        print('Too much')
        # inform the player about the number of tries
        print('You have got', tries, 'tries.')

    # reduce by one the number of tries
    tries -= 1

    # waiting for one second
    time.sleep(1)

    # print it to make the code more readable
    print(20*'=')
