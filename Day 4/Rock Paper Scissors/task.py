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

user_choice =(input('What do you choose?Type 0 for Rock, 1 for Paper, 2 for Scissors'))
computer_choice = random.randint(0,2)
print(f"Computer choose{computer_choice}")
if user_choice == computer_choice:
    print("its a tie")
elif user_choice == 0:
    print("you win")
else:
    print("you lose")
