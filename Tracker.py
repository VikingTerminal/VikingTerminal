import os
import re
import requests
import time
from colorama import Fore, Style
from googlesearch import search

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)  
    print()

def search_information(name, surname, city, phone_number):
    query_parts = []
    if name:
        query_parts.append(name)
    if surname:
        query_parts.append(surname)
    if city:
        query_parts.append(city)
    if phone_number:
        query_parts.append(phone_number)
    
    query = " ".join(query_parts) + " -site:linkedin.com -site:facebook.com -site:twitter.com"
    results = []

    try:
        for j in search(query, num=10, stop=10, pause=2):
            results.append(j)
    except Exception as e:
        pass

    return results

def get_links(results):
    return results

def print_introduction():
    clear_screen()
    type_writer_effect(f"{Fore.CYAN}Welcome to the search program! This tool is part of the collection at t.me/VikingTERMINAL\n{Style.RESET_ALL}")

def save_results(links):
    file_name = input(f"{Fore.YELLOW}Enter the file name to save the results (without extension): {Style.RESET_ALL}")
    file_name += ".txt"
    with open(file_name, "w") as file:
        for link in links:
            file.write(link + "\n")
    print(f"{Fore.GREEN}The results have been saved in the file {file_name}.{Style.RESET_ALL}")

def main():
    print_introduction()

    name = input(f"{Fore.YELLOW}Enter the name (optional): {Style.RESET_ALL}")
    surname = input(f"{Fore.YELLOW}Enter the surname (optional): {Style.RESET_ALL}")
    city = input(f"{Fore.YELLOW}Enter the city (optional): {Style.RESET_ALL}")
    phone_number = input(f"{Fore.YELLOW}Enter the phone number (optional): {Style.RESET_ALL}")

    results = search_information(name, surname, city, phone_number)
    links = get_links(results)

    clear_screen()
    if links:
        type_writer_effect(f"{Fore.CYAN}Links found:{Style.RESET_ALL}")
        for link in links:
            print(link)
        
        response = input(f"\n{Fore.YELLOW}Do you want to save the results in a text file? (yes/no): {Style.RESET_ALL}").lower()
        if response == "yes":
            save_results(links)
        elif response != "no":
            print(f"{Fore.RED}Invalid response. The results will not be saved.{Style.RESET_ALL}")
    else:
        type_writer_effect(f"{Fore.GREEN}No links found.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()