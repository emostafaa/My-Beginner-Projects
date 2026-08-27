import pyfiglet
from termcolor import colored
import secrets
letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=[]|;':,./<>?~"
numbers = "0123456789"

def cool_font_print(Characters, color, font="slant"):
     ascii_art = pyfiglet.figlet_format(Characters, font)
     print(colored(ascii_art, color))




print("********************************************")
cool_font_print("Pass_Gen", "green")
print("********************************************")
while True:
    try:
        length = int(input("Enter password length (in characters): "))
        break
    except ValueError:
        print("Please enter a number ")

print("********************************************")


characters = ""

if input("include upper-case letters: ").lower() == "y":
    characters += letters_upper
if input("include lower-case letters: ").lower() == "y":
    characters += letters_lower
if input("include symbols: ").lower() == "y":
    characters += symbols
if input("include numbers: ").lower() == "y":
    characters += numbers
if characters == "":
    print("You have to choose at least one option from above")    
else:
    print("********************************************")
    password = ""
    for i in range(length):
        password += secrets.choice(characters)
    print(f"The Generated Password Is: {password}")    

    
