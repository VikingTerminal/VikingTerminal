import os
import re
import requests
import time
from bs4 import BeautifulSoup
from colorama import Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def search_information(phone_number, api_key=None):
    results = []

    try:
        if api_key:
            response = requests.get(f"https://www.google.com/search?q={phone_number}&key={api_key}")
        else:
            response = requests.get(f"https://www.google.com/search?q={phone_number}")
            
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='BNeawe deIvCb AP7Wnd')
        for result in search_results:
            info = result.get_text(strip=True)
            results.append(info)
    except requests.RequestException as e:
        print(f"{Fore.RED}HTTP request error: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")

    return results

def print_introduction():
    clear_screen()
    type_writer_effect(f"{Fore.CYAN}Welcome to the search program! This tool is part of the t.me/VikingTERMINAL collection\n{Style.RESET_ALL}")

def print_results(results):
    clear_screen()
    if results:
        type_writer_effect(f"{Fore.GREEN}Details found:{Style.RESET_ALL}")
        for result in results:
            print(result)
    else:
        type_writer_effect(f"{Fore.GREEN}No details found.{Style.RESET_ALL}")

def main():
    print_introduction()

    choice = input(f"{Fore.YELLOW}Do you want to use your own API Key for the search? (yes/no): {Style.RESET_ALL}").lower()
    if choice == 'yes':
        api_key = input(f"{Fore.YELLOW}Enter your API key: {Style.RESET_ALL}")
        phone_number = input(f"{Fore.YELLOW}Enter the phone number: {Style.RESET_ALL}")
        if not re.match(r'^\d{10}$', phone_number):  
            print(f"{Fore.RED}The entered phone number is not valid. Please enter a 10-digit number.{Style.RESET_ALL}")
            return

        results = search_information(phone_number, api_key)
        print_results(results)
    elif choice == 'no':
        phone_number = input(f"{Fore.YELLOW}Enter the phone number: {Style.RESET_ALL}")
        if not re.match(r'^\d{10}$', phone_number):  
            print(f"{Fore.RED}The entered phone number is not valid. Please enter a 10-digit number.{Style.RESET_ALL}")
            return

        results = search_information(phone_number)
        print_results(results)
    else:
        print(f"{Fore.RED}Invalid choice. Please enter 'yes' or 'no'.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()