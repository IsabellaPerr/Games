import random
# y is number of guesses
y = 0
def guess_function(x, y):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess a number between 1 and {}: '.format(x)))
        if guess < random_number:
            y = y + 1
            print('Sorry, guess again. Too low.')
            print('Total guesses: {}'.format(y))
        elif guess > random_number:
            y = y + 1
            print('Sorry, guess again. Too high.')
            print('Total guesses: {}'.format(y))

    print('Yay, congrats. You have guessed the number {} correctly!!'.format(random_number))


y = 0
guess_function(1000, 0)
