# Author: Colin
# Python text-based blackjack game

import random
from art import logo
import os

def clear_console(): 
    return os.system('clear')

# Randomly select cards from a standard deck of cards to add to a hand
def addACard(list1):
    draw = random.randint(0, len(deck) - 1)
    list1.append(deck[draw])
    # .pop allows removes the card from the "deck" to allow draws to be more realistic
    deck.pop(draw)

# Check if the list has any face cards
def hasLetters(list1):
    for x in list1:
        if x == "J":
            return True
        elif x == "Q":
            return True
        elif x == "K":
            return True
        elif x == "A":
            return True
    return False

# Take in a hand of cards and determine their sum
def findSum(list1, letters):
    sum = 0
    newList = []
    for x in list1:
        newList.append(x)
    if letters:
        # Convert face cards to their numerical values
        for x in range(0, len(newList)):
            if newList[x] == 'J':
                newList[x] = 10
            elif newList[x] == 'Q':
                newList[x] = 10
            elif newList[x] == 'K':
                newList[x] = 10
            elif newList[x] == 'A' and 11 not in newList:
                newList[x] = 11
        # Aces count as 1 if the sum exceeds 21 or if there are other Aces
        if sum > 21 and 11 in newList:
            newList.remove(11)
            newList.append(1)
            sum = 0
        for x in newList:
            sum += x
    if not letters:
        for x in newList:
            sum += x
    return sum

# Determine the outcome of the round based on player and computer hands
def whoWon(pScore, cScore):
    if pScore == cScore:
        print("\n<<<Draw>>>")
    elif pScore  == 21:
        print("\n<<<Player Blackjack! You win.>>>")
    elif cScore == 21:
        print("\n<<<Computer Blackjack! You lose.>>>")
    elif pScore > 21:
        print("\n<<<Player Bust. You lose.>>>")
    elif cScore > 21:
        print("\n<<<Computer Bust. You win.>>>")
    elif pScore > cScore:
        print("\n<<<Player hand was greater. You win.>>>")
    elif cScore > pScore:
        print("\n<<<Computer hand was greater. You lose.>>>")

recordList = []

# Keep track of the number of wins, losses and draws
def record(pScore, cScore, recordList):
    draw = 0
    playerWin = 0
    computerWin = 0
    if pScore == cScore:
        recordList.append(0)
    elif pScore  == 21:
        recordList.append(1)
    elif cScore == 21:
        recordList.append(2)
    elif pScore > 21:
        recordList.append(2)
    elif cScore > 21:
        recordList.append(1)
    elif pScore > cScore:
        recordList.append(1)
    elif cScore > pScore:
        recordList.append(2)
    for x in recordList:
        if x == 0:
            draw += 1
        if x == 1:
            playerWin += 1
        if x == 2:
            computerWin += 1
    # Display the record to the player
    print("There have been" +
    " {} player wins, {} computer wins, and {} draws.".format(playerWin, 
    computerWin, draw))

playAgain = True  
while playAgain:
    print(logo)
    # Standard deck of cards (excluding Jokers)
    deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 
    7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 
    'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']
    playerHand = []
    computerHand = []
    winner = 0
    # Create player hand
    for x in range(2):
        addACard(playerHand)
    # Create computer hand 
    for x in range(2):
        addACard(computerHand)
    # Continuous loop until the player busts, wins, or chooses to stand
    while winner == 0:
        playerScore = findSum(playerHand, hasLetters(playerHand))
        computerScore = findSum(computerHand, hasLetters(computerHand))
        print("\nYour hand: {}\n Current score: {}".format(playerHand, 
        playerScore))
        print("\nThe computer's" +
        " hand: {}, ?\n Current score: ?".format(computerHand[0]))
        # Player wins
        if playerScore == 21:
            winner = 1
        # Computer wins
        elif computerScore == 21:
            winner = 1
        # Player busts; computer wins
        elif playerScore > 21:
            winner = 1
        else:
            playerMove = 'A'
            while playerMove.upper() != "H" and playerMove.upper() != "S":
                playerMove = input("Would you like to [H]it or" +
                " [S]tand?: ")
            if playerMove.upper() == 'H':
                addACard(playerHand)
            elif playerMove.upper() == 'S':
                winner = 1
    # Computer adds cards to its hand as long as its sum is less than 17
    while findSum(computerHand, hasLetters(computerHand)) < 17:
        addACard(computerHand)
    print('\n.............................................')
    # Display Player hand and score
    print("Your hand: {}\n Your score: {}".format(playerHand, 
    findSum(playerHand, hasLetters(playerHand))))
    # Display Computer hand and score
    print("\nComputer's hand: {}\n Computer's score: {}".format(computerHand, 
    findSum(computerHand, hasLetters(computerHand))))
    # Determine the outcome
    whoWon(findSum(playerHand, hasLetters(playerHand)), findSum(computerHand, 
    hasLetters(computerHand)))
    # Display results 
    record(findSum(playerHand, hasLetters(playerHand)), findSum(computerHand, 
    hasLetters(computerHand)), recordList)
    keepPlaying = 'A'
    # Prompt the user to either quit or continue playing
    while keepPlaying.upper() != "Y" and keepPlaying.upper() != "N":
        keepPlaying = input("Would you like to play again?" +
        " [Y]es or [N]o?: ")
    if keepPlaying.upper() == 'Y':
        playAgain = True
        for x in range(12):
            print('........\n')
    elif keepPlaying.upper() == 'N':
        playAgain = False
        recordList = []
        draw = 0
        playerWin = 0
        computerWin = 0
    clear_console()