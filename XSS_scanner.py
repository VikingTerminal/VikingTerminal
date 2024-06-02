import sys
import time
from bs4 import BeautifulSoup
import requests
from colorama import init, Fore

init(autoreset=True)

def print_magenta_with_typing_effect(text):
    for char in text:
        sys.stdout.write(Fore.MAGENTA + char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def print_cyan_with_typing_effect(text):
    for char in text:
        sys.stdout.write(Fore.CYAN + char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def find_xss_vulnerabilities(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        vulnerable_tags = soup.find_all(['script', 'iframe', 'input', 'a', 'img', 'form', 'textarea', 'div', 'span', 'button', 'select', 'label', 'link', 'style', 'table', 'tr', 'td', 'th', 'nav', 'header', 'footer', 'article'])
        found_vulnerabilities = False
        for tag in vulnerable_tags:
            if tag.string and any(xss_keyword in tag.string for xss_keyword in ['<script>', 'javascript:', 'onerror=', 'eval(', 'document.cookie']):
                print_magenta_with_typing_effect("Potential XSS vulnerability found in tag: " + tag.name)
                print_magenta_with_typing_effect("Tag content: " + tag.string.strip())
                print_magenta_with_typing_effect("Position in document: " + str(soup.get_text().find(tag.string.strip())))
                print_magenta_with_typing_effect("Line in document: " + str(soup.get_text().count('\n', 0, soup.get_text().find(tag.string.strip())) + 1))
                print_magenta_with_typing_effect("---------------")
                found_vulnerabilities = True

        if not found_vulnerabilities:
            print_cyan_with_typing_effect("No potential XSS vulnerabilities found.")
    except requests.RequestException as e:
        print(Fore.RED + "Error during HTTP request:", e)

print(Fore.RED + "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print(Fore.RED + "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█")
print(Fore.RED + "█░░║║║╠─║─║─║║║║║╠─░░█")
print(Fore.RED + "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
print(Fore.RED + "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

def main():
    print_cyan_with_typing_effect("Thank you for trying out this tool. Visit t.me/VikingTERMINAL to try out other utilities.\n")

    while True:
        url = input(Fore.YELLOW + "Enter the link to analyze (type 'exit' to quit): ")
        if url.lower() == 'exit':
            print_cyan_with_typing_effect("Thank you for trying out this tool. Visit t.me/VikingTERMINAL to try out other utilities.\n")
            break
        find_xss_vulnerabilities(url)

if __name__ == "__main__":
    main()