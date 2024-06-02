import os
import re
import requests
from bs4 import BeautifulSoup

# ANSI color codes for terminal output
Black, Red, Green, Yellow, Blue, Purple, Cyan, White = (
    '\033[1;90m', '\033[1;91m', '\033[1;92m', '\033[1;93m',
    '\033[1;94m', '\033[1;95m', '\033[1;96m', '\033[1;97m'
)

def banner():
    print(f"{Green}Rapid85")
    print(f"\n\e[1;77m     A web scraping tool designed to extract email addresses and phone numbers from websites.      \e[0m\n\n")
    print(f"\e[0;96m                Developed by: {Red}Rapid85 (t.me/VikingTerminal)\n\n\n")

    # Add a disappearing message
    os.system('sleep 3 && clear')

def internet():
    print(f"{White}[{Red}!{White}] {Red}Checking your internet connection")
    try:
        response = requests.get("http://www.google.com", timeout=5)
        response.raise_for_status()
        print(f"{White}[{Yellow}*{White}] {Yellow}Connected")
    except requests.ConnectionError:
        print(f"{White}[{Red}!{White}] {Red}No internet connection. Please try again.")
        exit()

def email_scraping(html):
    print(f"{White}[{Yellow}*{White}] {Yellow}Scraping emails...{White}")
    email_pattern = re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}', re.IGNORECASE)
    emails = sorted(set(re.findall(email_pattern, html)))
    
    if emails:
        print(f"{White}[{Yellow}*{White}] {Yellow}Emails scraped successfully{White}")
        for email in emails:
            print(email)
    else:
        print(f"{White}[{Red}!{White}] {Red}No emails found")

def phone_scraping(html):
    print(f"{White}[{Yellow}*{White}] {Yellow}Scraping phone numbers...{White}")
    phone_pattern = re.compile(r'(\d{3}-\d{3}-\d{4})|(\(\d{3}\)\d{3}-\d{4})|(\d{10})|(\d{3}\s\d{3}\s\d{4})')
    phones = sorted(set(re.findall(phone_pattern, html)))
    
    if phones:
        print(f"{White}[{Yellow}*{White}] {Yellow}Phone numbers scraped successfully{White}")
        for phone in phones:
            print("".join(filter(None, phone)))
    else:
        print(f"{White}[{Red}!{White}] {Red}No phone numbers found")

def scraper(url, email_choice, phone_choice):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text

        if email_choice.lower() == 'y':
            email_scraping(html)

        if phone_choice.lower() == 'y':
            phone_scraping(html)

        if os.path.exists("email.txt") or os.path.exists("phone.txt"):
            save_output = input(f"{White}[{Yellow}*{White}] Do you want to save the file (y/n): ")
            if save_output.lower() == 'y':
                output()
    except requests.RequestException as e:
        print(f"{White}[{Red}!{White}] {Red}Error fetching URL: {e}")
    finally:
        exit_program()

def output():
    custom_output = input(f"{White}[{Yellow}*{White}] Enter output file name (default: output.txt): ")
    output_file = custom_output or "output.txt"

    if os.path.exists(output_file):
        print(f"{White}[{Red}!{White}] {Red}File already exists")
        output()

    os.rename("email.txt", output_file)
    os.rename("phone.txt", output_file)

    print(f"{White}[{Green}*{White}] {Cyan}Output saved to {output_file}")
    exit_program()

def scanner():
    url = input(f"{White}[{Yellow}*{White}] Enter URL to begin: ")
    url_validity = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]')

    if url_validity.match(url):
        email_choice = input(f"{White}[{Yellow}*{White}] Scrape emails from website (y/n): ")
        phone_choice = input(f"{White}[{Yellow}*{White}] Scrape phone numbers from website (y/n): ")

        if email_choice.lower() == 'y' or phone_choice.lower() == 'y':
            print(f"{White}[{Red}!{White}] {Red}Scraping started")
            scraper(url, email_choice, phone_choice)

        print(f"{White}[{Red}!{White}] {Red}Exiting....\n")
        print("Thank you for using this tool. Visit t.me/VikingTerminal to try other utilities.")
        exit_program()
    else:
        print(f"{White}[{Red}!{White}] {Red}Check your URL (invalid)")
        scanner()

def exit_program():
    if os.path.exists("email.txt"):
        os.remove("email.txt")
    if os.path.exists("phone.txt"):
        os.remove("phone.txt")
    exit()

if __name__ == "__main__":
    banner()
    internet()
    scanner()
