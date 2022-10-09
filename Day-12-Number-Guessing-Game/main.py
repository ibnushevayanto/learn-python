import random

print("Welcome to the thenumber guessing game!")
print("I'm thinking of a number between 1 and 100.")

theNumber = random.randint(1, 100)
attempt = 0
difficulity = input("Choose a diffuculty. Type 'easy' or 'hard': ").lower()

def guessing(number):
    if theNumber == number:
        print("Correct!")
        return True
    elif number > theNumber:
        print("Too High")
        print("Guess again")
        return False
    else:
        print("Too Low")
        print("Guess again")
        return False

if difficulity == "easy":
    attempt = 10
elif difficulity == "hard":
    attempt = 5

while True:
    print(f"You have a {attempt} attempt remaining to guess the number")
    userGuess = int(input("Make a guess: "))
    if(attempt == 0):
        print("Game Over")
        break
    else:
        if guessing(userGuess):
            break

    attempt -= 1
    
