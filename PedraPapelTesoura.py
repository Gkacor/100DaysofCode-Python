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

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

cpu = random.randint(0, 2)

if choice == "0":
    print(rock)
    if cpu == 0:
        print("Cpu chose: " + rock + "It's a tie!")
    elif cpu == 1:
        print("Cpu chose: " + paper + "You Lose!")
    elif cpu == 2:
        print("Cpu chose: " + scissors + "You Win!")
elif choice == "1":
    print(paper)
    if cpu == 0:
        print("Cpu chose: " + rock + "You Win!")
    elif cpu == 1:
        print("Cpu chose: " + paper + "It's a tie!")
    elif cpu == 2:
        print("Cpu chose: " + scissors + "You Lose!")
elif choice == "2":
    print(scissors)
    if cpu == 0:
        print("Cpu chose: " + rock + "You Lose!")
    elif cpu == 1:
        print("Cpu chose: " + paper + "You Win!")
    elif cpu == 2:
        print("Cpu chose: " + scissors + "It's a tie!")
else:
    print("error")





