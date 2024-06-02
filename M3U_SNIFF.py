import os
import re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
import random
import time
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "visit t.me/VikingTERMINAL to try other tools")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

def find_m3u(domain):
    if not domain.startswith("http"):
        domain = "http://" + domain
    
    try:
        response = requests.get(domain)
        response.raise_for_status()  
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        
        links = soup.find_all('a', href=True)
        m3u_links = [urljoin(domain, link['href']) for link in links if link['href'].endswith('.m3u')]

        if m3u_links:
            print("\nHere are the m3u playlists found:")
            for link in m3u_links:
                color = random.choice([Fore.CYAN, Fore.MAGENTA, Fore.RED, Fore.GREEN])
                print(color, end='')
                type_effect(link, speed=0.02)
                print(Fore.RESET)
            save = input("\nDo you want to save these links to a txt file? (y/n): ")
            if save.lower() == 'y':
                with open("playlist_m3u.txt", "w") as file:
                    for link in m3u_links:
                        file.write(link + "\n")
                print("File saved as playlist_m3u.txt")
            else:
                print("Ok, not saving anything!")
        else:
            print("\nNo m3u playlists found on this domain. Try another domain!")

    except Exception as e:
        print(f"Error connecting to {domain}: {e}")

def type_effect(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

init()  
clear_screen()
domain = input("\nEnter the domain to scan (with or without 'https://'): ")
find_m3u(domain)
