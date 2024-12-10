# This is The Main File where I will write my programs
# And Import my SHITS

# from your Folder named my_modules, import module1.py --(You can just remove .py)
from my_modules import module1

def main():
    while True:
        # This Receives input from the user
        usr = input("ENTER SHTS: ")
        # this is a condition when the user enters 1
        if usr == "1":
            module1.code_challange1() 
            #this module1 is the one you imported from the file my_modules
            # This code_challange1() is the name of the function inside module1.py
        elif usr == "2":
            module1.code_challange2()
main()