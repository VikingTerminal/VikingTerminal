import requests
from colorama import Fore, Style
import time

def print_with_effect(text, color=Fore.WHITE, speed=0.03):
    for character in text:
        print(f"{color}{character}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(speed)
    print()

def get_original_link(shortlink):
    try:
        response = requests.head(shortlink, allow_redirects=True)
        return response.url
    except requests.RequestException as e:
        return f"Error: {e}"

def print_thank_you_message():
    message = "\nThank you for using this tool. Created by t.me/VikingTerminal"
    print_with_effect(message, color=Fore.GREEN)

def main():
    welcome = "Welcome! This tool will help you get the original link from a short link."
    print_with_effect(welcome, color=Fore.CYAN)

    while True:
        input_prompt = "Enter the short link (or type 'exit' to quit):\n"
        shortlink = input(f"{Fore.YELLOW}{input_prompt}{Style.RESET_ALL}")

        if shortlink.lower() == 'exit':
            print_thank_you_message()
            break

        original_link = get_original_link(shortlink)
        output = f"Original link:\n{original_link}\n"
        print_with_effect(output, color=Fore.GREEN)

if __name__ == "__main__":
    main()