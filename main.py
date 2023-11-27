import random
import string
import time
from os import system
from colorama import init, Fore, Style
from pyfiglet import Figlet
from termcolor import colored

system("title " + "INT LIST 9000")

init()  # Initialize colorama

def generate_code():
    section1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    section2 = "".join(random.choices(string.digits, k=4))
    section3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    code = "-".join([section1, section2, section3])
    return code

# Generate ASCII art for "INT LIST 9000"
f = Figlet(font='slant')
ascii_text = f.renderText('INT LIST 9000')

# Generate rainbow-colored ASCII art
rainbow_ascii_text = ""
colors = ['red', 'yellow', 'green', 'blue', 'magenta', 'cyan']
for char in ascii_text[:-1]:
    color = random.choice(colors)
    rainbow_ascii_text += colored(char, color)
rainbow_ascii_text += colored(ascii_text[-1], 'white')  # Set the last character color to white

login = True
logged = False

# Read existing data from the file
with open('int_list.txt', 'r') as file:
    int_list = [line.strip() for line in file]

while login:
    print(rainbow_ascii_text)
    print("")
    print("")

    username = input("USERNAME: ")
    pw = input("PASSWORD: ")


    # replace these with ur username/password.
    if username == "your username" and pw == "your password":
        print("ACCESS ACCEPTED!")
        time.sleep(0.5)
        login = False
        system("cls")
        logged = True
    else:
        print("ACCESS DENIED!")
        time.sleep(0.5)
        print("TRY AGAIN")
        login = True
        system("cls")

while logged:
    print(rainbow_ascii_text)
    print("")
    print("")

    new_player = input("Enter a new player (or type 'read' to review INT LIST or 'exit' to leave): ")

    if new_player.lower() == 'exit':
        logged = False
    elif new_player.lower() == "read":
        system('cls')

        print(rainbow_ascii_text)
        print("")
        print("")

        print("Updated INT List:")
        print("")
        for item in int_list:
            print(item)

        input()
        system('cls')
    else:
        int_list.append(new_player)
        system('cls')

        # Write the updated list to the file
        with open('int_list.txt', 'w') as file:
            for item in int_list:
                file.write(item + '\n')

# The file is now closed and contains the updated list
print("Goodbye!")


    