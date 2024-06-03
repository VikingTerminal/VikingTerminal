print("\033[91m⠀⠀⠀⠀⠀⣀⣀⣀⣀⣠⣤⣤⣄⣀⣀⣀⣀⠀⠀⠀⠀⠀")
print("⢀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀")
print("⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷")
print("⣿⣿⣿⡿⠛⠉⠉⠙⠿⣿⣿⣿⣿⠿⠋⠉⠉⠛⢿⣿⣿⣿")
print("⣿⣿⣿⣶⣿⣿⣿⣦⠀⢘⣿⣿⡃⠀⣴⣿⣿⣿⣶⣿⣿⣿")
print("⣿⣿⣿⣏⠉⠀⠈⣙⣿⣿⣿⣿⣿⣿⣋⠁⠀⠉⣹⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⢸⣿⣿⣎⠻⣿⣿⣿⣿⡿⠋⠙⢿⣿⣿⣿⣿⠟⣱⣿⣿⡇")
print("⠀⢿⣿⣿⣧⠀⠉⠉⠉⠀⢀⡀⠀⠉⠉⠉⠀⣼⣿⣿⡿⠀")
print("⠀⠈⢻⣿⣿⣷⣶⣶⣶⣶⣿⣿⣶⣶⣶⣶⣾⣿⣿⡟⠁⠀")
print("⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⠉⠉⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀")
print("⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣦⣴⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀\033[0m")

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def check_error_php_editable(domain):
    url = f"http://{domain}/error.php"
    try:
        print_slow(f"\n{Fore.YELLOW}Scanning {url}...{Style.RESET_ALL}")
        time.sleep(1)
        
        response = requests.get(url)
        
        if response.status_code == 200:
            print_slow(f"{Fore.GREEN}Response received. Analyzing...{Style.RESET_ALL}")
            time.sleep(1)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            forms = soup.find_all('form')
            textareas = soup.find_all('textarea')

            if forms or textareas:
                print_slow(f"{Fore.RED}The file {url} exists and may be editable.{Style.RESET_ALL}")
            else:
                print_slow(f"{Fore.BLUE}The file {url} exists but doesn't seem to be editable.{Style.RESET_ALL}")
        else:
            print_slow(f"{Fore.RED}The file {url} doesn't exist (status code: {response.status_code}).{Style.RESET_ALL}")
    except requests.RequestException as e:
        print_slow(f"{Fore.RED}Error requesting {url}: {e}{Style.RESET_ALL}")

def save_results_to_file(results, filename):
    with open(filename, 'w') as file:
        for result in results:
            file.write(result + '\n')

if __name__ == "__main__":
    while True:
        domain = input("\nEnter the domain (without http:// or https://) or 'exit' to quit: ")
        if domain.lower() == 'exit':
            break  
        check_error_php_editable(domain)
        
        while True:
            save_option = input("\nDo you want to save the results to a file? (y/n): ")
            if save_option.lower() == 'y':
                filename = input("Enter the TXT file name to save the results: ")
                try:
                    save_results_to_file(['Result 1', 'Result 2'], filename + '.txt')  
                    print(f"The results have been saved to {filename}.txt")
                    break
                except Exception as e:
                    print(f"An error occurred while saving the results: {e}")
            elif save_option.lower() == 'n':
                break
            else:
                print("Invalid option. Please enter 'y' to save or 'n' to not save the results.")