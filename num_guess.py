# Author: Justin Huang
# GitHub username: huangjus
# Date: 1/25/23
# Description: Has the user guess a given number until they are correct, then tells them the number of tries it took

number = int(input('Enter the integer for the player to guess.'))
tries = 0
while True:
    guess = int(input('Enter your guess.'))
    tries += 1
    if guess == number:
        break
    elif guess > number:
        print('Too high - try again:')
    else:
        print('Too low - try again:')

if tries == 1:
    print('You guessed it in 1 try')
else:
    print('You guessed it in', tries, 'tries.')
