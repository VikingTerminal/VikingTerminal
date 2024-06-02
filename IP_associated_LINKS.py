import requests
from colorama import Fore, Style, init
import sys
import random

init(autoreset=True)

def random_color():
    return random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])

def print_error(message):
    color = Fore.RED
    formatted_message = color + message + Style.RESET_ALL
    print(formatted_message)

def get_user_input():
    user_ip_address = input(Fore.GREEN + "Enter the IP address for the search: ")
    user_api_key = input(Fore.GREEN + "Enter your API key (e.g., for ipstack): ")

    return user_ip_address.strip(), user_api_key.strip()

def find_associated_links(ip_address, api_key):
    api_url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()
        links = data.get('links', [])

        color = random_color()
        print(Fore.YELLOW + f"Links associated with the IP address {ip_address}:\n")
        for link in links:
            print(color + link)

    except requests.exceptions.HTTPError as errh:
        print_error(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print_error(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print_error(f"Timeout: {errt}")
    except requests.exceptions.RequestException as err:
        print_error(f"Error: {err}")

def main():
    # Display ASCII banner with random color
    banner = """ _ _  _  _    _           
| | |<_>| |__<_>._ _  ___ 
| ' || || / /| || ' |/ . |
|__/ |_||_\_\|_||_|_|\_. |
t.me/VikingTerminal  <___
"""
    print(random_color() + banner)

    user_ip_address, user_api_key = get_user_input()
    
    if not user_ip_address:
        print_error("IP address is required.")
        return
    
    if not user_api_key:
        print_error("API key is required.")
        return
    
    find_associated_links(user_ip_address, user_api_key)

if __name__ == "__main__":
    main()
