import random


def game():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return 'It is a tie'

    if win(user, computer):
        return 'You won!'

    return 'You lost!'


def win(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') \
            or (player == 'paper' and opponent == 'rock'):
        return True


print(game())
