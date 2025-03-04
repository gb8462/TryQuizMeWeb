import os
import base64
import random

def clean():
    os.system("cls")

def game():
    attempt = 0
    chances = 10
    
    print("Hallooooo :3")
    print("\nGuessing Game")

    number_to_guess = random.randrange(20)
    
    while attempt < chances:

        attempt += 1
        usr = int(input('Please Enter your Guess (0-20) : '))
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

def decode():
    decoding = "Q29uZ3JhdHMhIEdhbGluZyBOYW1hbn4sIENhcmxvcyBuZ2EgcGFsYSBIQUhBSEFIQUhB"
    clean()
    decoded_data = base64.b64decode(decoding.encode('utf-8')).decode('utf-8')
    print(f"Congratulations!: \n{decoded_data}")

game()
