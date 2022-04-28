"""Guess Game you can guess number or computer can guess your number"""
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    TURNS = 5
    while guess != random_number and TURNS != 0:
        guess = int(input(f'Guess a number between 1 and {x} :  '))
        if guess > random_number:
            print("Sorry, guess again. Too high")
            TURNS -= 1
            print(f"You have {TURNS} attempts remaining to guess the number")
        elif guess < random_number:
            print("Sorry, guess again. Too low")
            TURNS -= 1
            print(f"You have {TURNS} attempts remaining to guess the number")

    if guess == random_number:   
        print(f'Yay, Congrats.You have guessed the number {random_number} correctly')
    else:
        print("Game Over!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high :
            guess = random.randint(low, high)
        else :
            guess = low 
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (c)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess} correctly!')


guess(100)
