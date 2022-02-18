# choose your own adventure (CYOA) CSP project
# -*- coding: utf-8 -*-
HP = 5
Ammo = 10


def HP_check(x):
    if x <= 0:
        print(name, 'died')


def S2(x, y):
    print('You open the red door and find a goblin, you fight valiantly and barely make it out alive, \
in the process you lose 3 health, you lose 1 Ammo')
    y = y - 1
    x = x - 3
    HP_check(HP)
    ans = input('There are two more doors in front of you, a black and a \
blue door, the question is which one do you choose')

    if ans == 'black':
        S5(HP, Ammo)
    else:
        S6(HP)


def S5(x, y):
    print('You enter the next room where you find a dragon guarding its treasure, the \
dragon is alerted by your footsteps, you shoot all of your Ammo but the dragon promptly deals 5 damage')
    y = y - 10
    x = x - 5
    HP_check(x)


def S6(x):
    print('you enter through the blue door and find a health potion which you drink and heal to full health')
    x = 5
    ans = input('There is a single door in front of you, do you go through it, type "y for yes and "n" for no')
    if ans == 'y':
        S5(HP, Ammo)
    else:
        print('What are you doing, this is called a choose your own adventure game \
not a sit on the ground game, your character goes through anyway')
        S5(HP, Ammo)


def S9():
    print('There is a single door in front of you and you open it to finally see the daylight of the sun', name,
          'wins!')


def S3(x, y):
    swo = input(
        'After entering the blue door you discover a sword on the ground do you pick it up, "y" for yes or "n" for "no"')
    if swo == 'n':
        print('what are you doing? Theres a sword you can use instead of a sling, your character \
        picks it up anyway because they are not trying to lose')
    y = 0
    ans = input('You drop your Ammo after you pick up the sword and make your way through the room, at the end of the dark hallway \
there is an undead skeleton \n you can strike it on the helmet or attack the arm with your new found sword \
    \n type "helmet" to attack the hemet or "arm" to attack the arms')
    if ans == 'helmet':
        print('you take your sword out and it breaks on hit, you lose 5 health')
        x = x - 5
        HP_check(x)
    else:
        print('You battle with the skeleton and achieve victory but lose 3 health in the process')
        S9()


def S1():
    door1 = input('You see three identical doors in front of you \
one red one blue and one green which one do you go through')
    if door1 == 'red':
        S2(HP, Ammo)
    elif door1 == 'blue':
        S3(HP, Ammo)
    else:
        S4(HP)


def S4(x):
    ans = input(
        'Out of nowhere a skeleton shoots you with an arrow and you lose 1 health, do you attack the head or the arm with your weapon')
    x = x - 1
    HP_check(x)
    if ans == 'head':
        print('You use your weapon to attack the head of the skeleton, you get the jump on the enemy and emerge victorious, \
you then go through the only door in front of you')
        S9()
    else:
        print('You break your weapon with your attack and lose 5 health')
        x = x - 5
        HP_check(HP)


name = input('You awaken dizzy and in a dark room with a slingshoot in one hand and a torch in the other \
what is this character\'s name')
S1()
