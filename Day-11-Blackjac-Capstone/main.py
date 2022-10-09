import art
import random
from replit import clear

print(art.logo)

def calculateCard(cards):
    if sum(cards) == 2 and len(cards) == 2:
        return 0
        
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(totalUser, totalComputer):
    if totalUser > totalComputer and totalUser <= 21:
        return "You Win"
    elif totalComputer > 21 and totalUser <= 21:
        return "You Win"
    elif totalUser == totalComputer:
        return "Draw"
    else:
        return "You Lose"

while True:
    user_cards = []
    computer_cards = []

    for idx in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"Your Cards: {user_cards}")
    print(f"Computer First Card: {computer_cards[0]}")
    

    totalUserOverall = calculateCard(user_cards)
    totalComputerOverall = calculateCard(computer_cards)

    if(totalUserOverall == 0):
        print("You got blackjack, you won")
        break
    elif totalComputerOverall == 0:
        print("Computer got blackjack, you lose")
        break

    if totalUserOverall > 0 and totalComputerOverall > 0:
        isGetAnotherCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        if isGetAnotherCard == "y":
            user_cards.append(deal_card())
            totalUserOverall = calculateCard(user_cards)
        if totalComputerOverall < 17:
            computer_cards.append(deal_card())
            totalComputerOverall = calculateCard(computer_cards)
    
        print(f"Your Final Hand: {user_cards}")
        print(f"Computer Final Hand: {computer_cards}")
        print(compare(totalUserOverall, totalComputerOverall))
    
    wannaPlayAgain = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if wannaPlayAgain != "y":
        break
    else:
        clear()
