import random

randomnumber = random.randrange(1, 1001)

userguess = 0

for guess in range():
    guess = int(input("Please guess a number between 1 and 1000: "))
    userguess += 1
    if guess > randomnumber:
        print("Too High")
    elif guess < randomnumber:
        print("Too Low")
    elif guess == randomnumber:
        print("Correct!")
        print("Guesses: ", userguess)
        break