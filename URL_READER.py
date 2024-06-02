import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import random
import time

def read_web_content(domain):
    try:
        url = f'http://{domain}'
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            formatted_text = ' '.join(soup.stripped_strings)
            
            print(f"\n{Fore.CYAN}Content of the page {url}:{Style.RESET_ALL}\n")
            
            for char in formatted_text:
                time.sleep(0.01)  # Delay between characters for "typewriter" effect
                text_color = Fore.LIGHTGREEN_EX
                print(f"{text_color}{char}{Style.RESET_ALL}", end='', flush=True)

            print("\n")
        else:
            print(f"\nError {response.status_code}: Unable to access the page {url}")
    except Exception as e:
        print(f"\nError during HTTP request: {e}")

def main():
    while True:
        domain = input(f"{Fore.LIGHTYELLOW_EX}Enter the domain (e.g., www.example.com), or type 'exit' to quit: {Style.RESET_ALL}")
        
        if domain.lower() == 'exit':
            print(f"\nThank you for using the script! Best regards: {Fore.YELLOW}t.me/VikingTerminal{Style.RESET_ALL}")
            break
        elif domain:
            read_web_content(domain)
        else:
            print("The entered domain is not valid.")

if __name__ == "__main__":
    main()