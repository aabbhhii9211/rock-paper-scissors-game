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

#print(scissors)
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

random_computer_choice = random.randint(0,2)

#for computer
if random_computer_choice == 0:
  print(f"{rock}\nComputer chose:")
elif random_computer_choice == 1:
  print(f"{paper}\nComputer chose:")
elif random_computer_choice == 2:
  print(f"{scissors}\nComputer chose:")

#for player
if your_choice == 0:
  print(rock)
elif your_choice == 1:
  print(paper)
elif your_choice == 2:
  print(scissors)

# logic of game
if your_choice == random_computer_choice:
  print('game tied')
elif your_choice == 0 and random_computer_choice == 1:
  print("You lose")
elif your_choice == 0 and random_computer_choice == 2:
  print('You win')
elif your_choice == 1 and random_computer_choice == 0:
  print('You win')
elif your_choice == 1 and random_computer_choice == 2:
  print('You lose')
elif your_choice == 2 and random_computer_choice == 0:
  print("You lose")
elif your_choice == 2 and random_computer_choice == 1:
  print("You win")
else:
  print('You typed a invalid number!\nYou lose')