from replit import clear
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
  clear()
  print(logo)
  my_hand = []
  pc_hand = []
  deal_1 = True
  deal_2 = True
  my_hand.append(random.choice(cards))
  my_hand.append(random.choice(cards))
  while deal_1:
    if sum(pc_hand)<15:
      pc_hand.append(random.choice(cards))
    elif sum(pc_hand)<21:
      if random.randint(0,1)==1:
        c = random.choice(cards)
        if c == 11:
          c = 1
        pc_hand.append(c)
      else :
        deal_1 = False
    elif sum(pc_hand)>21:
      deal_1 = False

  while deal_2:
    print(f"Your cards: {my_hand}, Current score = {sum(my_hand)}")
    print(f"Dealer's first card: {pc_hand[0]}")
    prompt_3 = input("Type 'y' to get another card. Type 'n' to pass: ")
    if prompt_3 == 'y':
      d = random.choice(cards)
      if sum(my_hand)>11:
        if d==11:
          d = 1
      my_hand.append(d)
      if sum(my_hand)>21:
        print(f"Bust! You Lose. Your cards: {my_hand}, current_score: {sum(my_hand)}\n")
        deal_2 = False

    else:
      if sum(my_hand)>sum(pc_hand):
        print(f"You Won! Your cards: {my_hand}, current_score: {sum(my_hand)}\n Dealer's cards{pc_hand} Dealer's score: {sum(pc_hand)} ")
      elif sum(my_hand)<sum(pc_hand) and sum(pc_hand)<=21:
        print(f"You Lost! Your cards: {my_hand}, current_score: {sum(my_hand)}\n Dealer's cards{pc_hand} Dealer's score: {sum(pc_hand)}")
      elif sum(my_hand)==sum(pc_hand):
        print(f"Draw! Your cards: {my_hand}, current_score: {sum(my_hand)}\n Dealer's cards{pc_hand} Dealer's score: {sum(pc_hand)}")
      elif sum(my_hand)<sum(pc_hand) and sum(pc_hand)>21:
        print(f"Dealer bust! Your cards: {my_hand}, current_score: {sum(my_hand)}\n Dealer's cards{pc_hand} Dealer's score: {sum(pc_hand)}")
      deal_2 = False
  prompt_2 = input("Do you want to play another game? Type 'y' or 'n': ")
  if prompt_2 == 'y':
    blackjack()
  else:
    exit()


prompt = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if prompt == 'y':
  blackjack()