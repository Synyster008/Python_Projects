from art import logo, vs
#from replit import clear
from game_data import data
import random

info_a = {}
info_b = {}
score = 0

info_a = random.choice(data)
info_b = random.choice(data)
play = True
print(logo)

while play:
  if info_a == info_b:
    info_b = random.choice(data)
  else:
    print(f"Compare A: {info_a['name']}, a {info_a['description']}, from {info_a['country']}")
    print(vs)
    print(f"Against B: {info_b['name']}, a {info_b['description']}, from {info_b['country']}")
    prompt = input("Who has more followers? Type 'A' or 'B': ")
    #clear()
    print(logo)
    if prompt == 'A':
      if info_a['follower_count']>info_b['follower_count']:
        score +=1
        info_a = info_b
        info_b = random.choice(data)
        print(f"You're right. Current score: {score}")
      else:
        play = False
        print(f"Wrong! Final score: {score}")
    else:
      if info_b['follower_count']>info_a['follower_count']:
        score +=1
        info_a = info_b
        info_b = random.choice(data)
        print(f"You're right. Current score: {score}")
      else:
        play = False
        print(f"Wrong! Final score: {score}")