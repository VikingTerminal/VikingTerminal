import time
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from typing import Iterator

def type_effect(text: str) -> Iterator[str]:
    for char in text:
        yield char
        time.sleep(0.05)  

def print_random_color(text: str) -> None:
    for char in text:
        print(Fore.CYAN if char.isalpha() else Fore.GREEN, end="")
        print(char, end="")
        time.sleep(0.02)  
    print(Style.RESET_ALL)  

def check_database_visibility(domain, keywords=None):
    url = f"http://{domain}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print_random_color("The program is searching the database on: ")
            print_random_color(domain)
            time.sleep(1)  
            
            print_random_color("\nSearching for the database name...\n")
            time.sleep(1)  

            print(Fore.YELLOW + "Search Result:\n" + Style.RESET_ALL)  
            
            soup = BeautifulSoup(response.text, 'html.parser')

            database_keywords = keywords.split(',') if keywords else ["database", "SQL", "MySQL", "PostgreSQL", "MongoDB", "NoSQL", "SQLite"]

            potential_tags = soup.find_all(["meta", "title", "div", "span", "a"])
            database_name = None
            for tag in potential_tags:
                for keyword in database_keywords:
                    if keyword.strip().lower() in str(tag).lower():
                        database_name = tag.text.strip()
                        break
                
                if not database_name:
                    for key, value in tag.attrs.items():
                        for keyword in database_keywords:
                            if keyword.strip().lower() in value.lower():
                                database_name = value.strip()
                                break
                        if database_name:
                            break
                
                if database_name:
                    break

            if database_name:
                print_random_color(f"Database Name Found: {database_name}\n")
            else:
                print_random_color("Unable to retrieve the database name.\n")
        else:
            print_random_color("The database does not seem to be visible.\n")
    except requests.ConnectionError:
        print_random_color("Unable to connect to the domain.\n")

def main():
    print(Fore.RED + '''
┈┈┈╲┈┈┈┈╱
┈┈┈╱▔▔▔▔╲
┈┈┃┈▇┈┈▇┈┃
╭╮┣━━━━━━┫╭╮
┃┃┃┈┈┈┈┈┈┃┃┃
╰╯┃┈┈┈┈┈┈┃╰╯
┈┈╰┓┏━━┓┏╯
┈┈┈╰╯┈┈╰╯
__        
\  / | |__/ | |\ | / _`       
 \/  | |  \ | | \| \__>
     
powered by t.me/RAPID85
''' + Style.RESET_ALL)
    print_random_color("Welcome to the database visibility verification program. Visit t.me/VikingTERMINAL to discover all my tools!\n")
    domain = input("[#] Enter the database domain:\n\n ")
    custom_keywords = input("\n\nEnter keywords separated by commas (leave blank to use default ones):\n\n ")
    print_random_color("\nSearching for the database name...\n")
    time.sleep(2)  
    check_database_visibility(domain, custom_keywords)

if __name__ == "__main__":
    main()