import random

randomnumber = random.randrange(1, 11)

for guess in range(3):
    guess = int(input("Please guess a number between 1 and 10: "))
    if guess > randomnumber:
        print("Too High")
    elif guess < randomnumber:
        print("Too Low")
    elif guess == randomnumber:
        print("Correct!")
        break