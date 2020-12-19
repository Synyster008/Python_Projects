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

prompt = input("What do you choose? Type 'rock' 'paper' 'scissors' for the required roll\n")

c = random.randint(1,3)

if c==1:
  c=rock
elif c==2:
  c=paper
else:
  c=scissors

if prompt=='rock':
  print(rock)
  print(f"Computer chose\n{c}")
  if c==rock:
    print("Draw")
  elif c==paper:
    print("You lose")
  else:
    print("You win")
elif prompt=='paper':
  print(paper)
  print(f"Computer chose\n{c}")
  if c==rock:
    print("You win")
  elif c==paper:
    print("Draw")
  else:
    print("You lose")
else:
  print(scissors)
  print(f"Computer chose\n{c}")
  if c==rock:
    print("You lose")
  elif c==paper:
    print("You win")
  else:
    print("Draw")


