import time
import random
import os
from colorama import init, Fore, Style

init(autoreset=True)

def print_typewriter_colored(text):
    for char in text:
        print(Fore.CYAN + Style.BRIGHT + char, end='', flush=True)
        time.sleep(0.03)  

while True:
  
    file_path = input(Fore.GREEN + "Enter the file path ('exit' to quit): ")

    if file_path.lower() == 'exit':
        print(Fore.MAGENTA + "Thanks for using the script! Follow me on t.me/VikingTerminal. Goodbye!")
        break

    try:
        
        full_path = file_path if "." in file_path else file_path + ".txt"

        if not os.path.isfile(full_path):
            raise FileNotFoundError

        with open(full_path, 'r') as file:
           
            content = file.read()

            
            print_typewriter_colored(content)

    except FileNotFoundError:
        print(Fore.RED + "File not found. Make sure to enter a valid path.")
    except Exception as e:
        print(Fore.RED + "An error occurred:", e)