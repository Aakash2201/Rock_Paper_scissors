# Read about lists, nested lists, read abour list[+index] and list[-index]
# we can import any code of python into any other code by using import function

import temp

print(temp.Aakash)

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
import random

random_num = random.randint(1,3)

user_choice = input("What do you choose? Type 1 for Rock, Type 2 for Paper and Type 3 for Scissors")

if user_choice == 1:
    print(rock)
elif user_choice == 2:
    print(paper)
else:
    print(scissors)

print("Computer chooses =")

if random_num == 1:
    print(rock)
elif random_num == 2:
    print(paper)
else:
    print(scissors)

if random_num == user_choice:
    print("Draw")

elif random_num == 1:
    if user_choice == 2:
        print("You win")
    else:
        print("You Loose")

elif random_num == 2:
    if user_choice == 1:
        print("You Loose")
    else:
        print("You Win")

else:
    if user_choice == 1:
        print("You Win")
    else:
        print("You Loose")



# import random
# import numpy as np

# print("Welcome to Game !!!!!")
# UserInput = int(input("Choose one \n1.Rock \n2.Paper \n3.Sizor"))
# RanOutput = random.randint(0,3)
# print(f"{UserInput} {RanOutput}")

