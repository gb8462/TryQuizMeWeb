import os
import base64
import random

# Guessing Game Made by yours Truly.
# my name is Encoded run the code and play to know :3
# para masaya wag ka mang daya~

def clean():
    os.system("cls")

def game():
    attempt = 0
    chances = 10
    
    print("Hallooooo :3")
    print("\nGuessing Name Game")

    number_to_guess = random.randrange(30)
    
    while attempt < chances:

        attempt += 1
        usr = int(input('Please Enter your Guess (0-30) : '))
        clean()
        if usr == number_to_guess:
            print(f'The number is {number_to_guess} and you found it right !! in the {attempt} attempt')
            decode()
            break
        elif attempt >= chances and usr != number_to_guess:
            print(f'Oops sorry, The number is {number_to_guess} better luck next time')
        elif usr > number_to_guess:
            print('Your Number is High ')
        elif usr < number_to_guess:
            print('Your Number is Less')
        else:
            print("Invalid Input~!")

def decode():
    decoding = "Q29uZ3JhdHMhIEdhbGluZyBOYW1hbn4sIENhcmxvcyBuZ2EgcGFsYSBIQUhBSEFIQUhB"
    clean()
    decoded_data = base64.b64decode(decoding.encode('utf-8')).decode('utf-8')
    print(f"Congratulations!: \n{decoded_data}")

game()
