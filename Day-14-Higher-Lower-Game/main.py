import art
import game_data
import random
from replit import clear

score = 0

def get_text_compare(item):
    return f"{item['name']}, a {item['description']}, from {item['country']}"

def compare(itemA, itemB, answer):
    if answer == 'a':
        return itemA['follower_count'] > itemB['follower_count']
    elif answer == 'b':
        return itemB['follower_count'] > itemA['follower_count']
    else: 
        print("Invalid answer")
        return False

def game_play():
    itemA = game_data.data[random.randint(0, len(game_data.data) - 1)]
    itemB = game_data.data[random.randint(0, len(game_data.data) - 1)]
    print(f"Compare A: {get_text_compare(itemA)}")
    print(art.vs)
    print(f"Against B: {get_text_compare(itemB)}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    return compare(itemA, itemB, answer)
    
while True:
    if(game_play()):
        score += 1
        clear()
        print(f"You're right! current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break