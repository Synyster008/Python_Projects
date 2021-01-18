from art import logo
import random
def play(lives, num):
    c = random.randint(1,100)
    d = lives
    lives_left = True
    while lives_left:
        if num != c:
            lives -=1
            if lives == 0:
                print(f"You ran out of lives. Psst the number is {c}")
                lives_left = False
            else :
                print("Wrong Guess!")
                if num<c:
                    print("Too low")
                else:
                    print("Too high")
                prompt_3: int = int(input(f"No. of attempts remaining: {lives}\nGuess again\n"))
                num = prompt_3
        else:
            print(f"You guessed it!. The number is {c}")
            break



print(logo)
print("Welcome to 'Guess the Number!'")
prompt_1 = input ("There are two modes to play this game. Type 'easy' or 'hard': ")
print("I'm thinking of a number between 1 to 100")
prompt_2 = int(input("Can you guess the number?"))

if prompt_1 == 'easy':
    play(10, prompt_2)
else:
    play(5, prompt_2)