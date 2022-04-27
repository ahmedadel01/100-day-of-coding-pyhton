# The Blackjack Capstone Project

import random
from replit import clear

def dealCard():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculateScore(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # the user or the computer has got a score of Blackjack
    
    #if score is already over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(userScore, computerScore):
    if userScore == computerScore:
        return "Draw!"
    elif computerScore == 0:
        return "Lose, opponent has Blackjack"
    elif userScore == 0:
        return "You Win with a Blackjack"
    elif userScore > 21:
        return "You went over. You loss"
    elif computerScore > 21:
        return "Opponent went over. You win"
    elif userScore > computerScore:
        return "You win!"
    else:
        return 'You lose'

def playGame():
    userCards = []
    computerCards = []
    isGameOver = False

    for _ in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())

    while not isGameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        print(f"  Your card:{userCards}, currnet score: {userScore}")
        print(f"   Computer's first card: {computerCards[0]}")

        # If the computer of the user has a blackjack (0) or 
        # if the user's score is over 21, than the game ends.
        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else:
            userShouldDeal = input("Type 'y' to get another card, type 'n' to pass: ")
            if userShouldDeal == "y":
                userCards.append(dealCard())
            else:
                isGameOver = True

    while computerScore != 0 and computerScore < 17:
        computerCards.append(dealCard())
        computerScore = calculateScore(computerCards)
    print(f"    Your final hand: {userCards}, final score: {userScore}")
    print(f"    Computer's final hand: {computerCards}, final score: {computerScore}")
    print(compare(userScore, computerScore))

# Ask the user if want to restart the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n'?") == "y":
    clear()
    playGame()
