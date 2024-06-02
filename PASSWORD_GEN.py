import time
import random
import string
from termcolor import colored  

def print_with_typing_effect_green(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_with_typing_effect(text, color='white', delay=0.01):
    color_code = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }
    
    for char in text:
        print(f"{color_code.get(color, color)}{char}\033[0m", end='', flush=True)
        time.sleep(delay)
    print()

def generate_password(length, use_numbers=True, use_symbols=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_special_chars:
        characters += "!@#$%^&*()_-+=<>?"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def animated_progress_bar(iterations, delay=0.1):
    for _ in range(iterations):
        print("[", end='')
        for i in range(10):
            time.sleep(delay)
            print("■", end='', flush=True)
        print("]", end='\r')
    print()

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).lower()
        if response == 'y' or response == 'yes':
            return True
        elif response == 'n' or response == 'no':
            return False
        else:
            print(colored("Please enter 'y' or 'n'. Try again.", 'red'))

try:
    num_passwords = int(input(colored("Enter the number of passwords to generate: ", random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']))))
    password_length = int(input(colored("Enter the desired length of passwords: ", random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']))))
except ValueError:
    print(colored("Please enter a valid number.", 'red'))
    exit()

use_numbers = get_yes_no_input(colored("Do you want to include numbers in passwords? (y/n): ", random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])))
use_symbols = get_yes_no_input(colored("Do you want to include symbols in passwords? (y/n): ", random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])))
use_special_chars = get_yes_no_input(colored("Do you want to include special characters in passwords? (y/n): ", random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])))

print_with_typing_effect_green(colored("\nGenerating passwords...", random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])))

for _ in range(num_passwords):
    password = generate_password(password_length, use_numbers, use_symbols, use_special_chars)
    print_with_typing_effect(f"Generated password: {password}", 'cyan')

save_to_file = get_yes_no_input(colored("\nDo you want to save these passwords to a file? (y/n): ", random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])))

if save_to_file:
    
    filename = input("Enter the file name (with .txt extension): ")
    
    
    if not filename.lower().endswith('.txt'):
        print(colored("Error: File must have .txt extension", 'red'))
    else:
        try:
            with open(filename, 'a') as file:
                for _ in range(num_passwords):
                    file.write(f"{generate_password(password_length, use_numbers, use_symbols, use_special_chars)}\n")
        except (FileNotFoundError, PermissionError, IsADirectoryError, OSError) as e:
            print(colored(f"Error saving file: {e}", 'red'))
        except Exception as e:
            print(colored(f"Unknown error saving file: {e}", 'red'))

animated_progress_bar(3)

print_with_typing_effect("Thank you for trying out this tool. Visit t.me/VikingTerminal to try out other utilities!!!", color='cyan')