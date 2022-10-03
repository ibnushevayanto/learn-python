import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gameImage = [rock, paper, scissors]

userChoice = int(
  input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if userChoice == 0 or userChoice == 1 or userChoice == 2:
  print(gameImage[userChoice])

opponentChoice = random.randint(0, 2)
print("Computer choice:\n")
if opponentChoice == 0 or opponentChoice == 1 or opponentChoice == 2:
  print(gameImage[opponentChoice])

if userChoice == 0:
  if opponentChoice == 2:
    print("You Won")
  elif opponentChoice == 0:
    print("Draw")
  else:
    print("You Lose")
elif userChoice == 1:
  if opponentChoice == 0:
    print("You Won")
  elif opponentChoice == 1:
    print("Draw")
  else:
    print("You Lose")
elif userChoice == 2:
  if opponentChoice == 1:
    print("You Won")
  elif opponentChoice == 2:
    print("Draw")
  else:
    print("You Lose")
else:
  print("Not valid command. You Lose")