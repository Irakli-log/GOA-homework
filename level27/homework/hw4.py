import random


numbers = list(range(1, 31))

number = random.choice(numbers)

while True:
    user = input("Guess the number (from 1 to 30): ")

    
    if not user.isdigit():
        print("Incorrect, You must enter a number from 1 to 30")
        continue
    
    guess = int(user)

    if guess < 1 or guess > 30:
        print("Incorrect, You must enter a number from 1 to 30")
    elif  guess == number :
        print("You guessed the number!")
        break
    else:
        print("Incorrect, Please try again")
