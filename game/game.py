import random
import sys
while True:
    try:
        user_input= int(input("Level: "))
        if user_input > 0:
            break
    except ValueError:
        pass
random_number = random.randint(1, user_input)
while True:
    try:
        user_input2= int(input("Guess: "))
        if user_input2 >0:
            if user_input2 < random_number:
                print("Too small!")
            elif user_input2 > random_number:
                print("Too large!")
            else:
                print("Just Right!")
                break
    except ValueError:
        pass




