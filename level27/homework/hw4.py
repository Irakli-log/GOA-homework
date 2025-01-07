import random


numbers = list(range(1, 31))


chosen_index = random.randint(0, 29)

while True:
    user_input = input("შეიყვანეთ რიცხვი 1-დან 30-მდე: ")

 
    if user_input.isdigit():
        user_input = int(user_input)

        
        if user_input < 1 or user_input > 30:
            print("Incorrect You must enter a number from 1 to 30")
        
      
        elif user_input == numbers[chosen_index]:
            print("You guessed the number")
            break
        else:
            print("Incorrect Please try again")
    else:
        print("Incorrect You must enter a number from 1 to 30")
