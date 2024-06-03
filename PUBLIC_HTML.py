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
from urllib.parse import urljoin
import time
import threading
from queue import Queue
import logging
from urllib.robotparser import RobotFileParser

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

TIMEOUT = 10  

def get_links(url, domain):
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = set()
            for link in soup.find_all('a', href=True):
                href = link['href']
                if 'html_public' in href:
                    full_url = urljoin(url, href)
                    links.add(full_url)
            return links
    except requests.RequestException as e:
        logging.error(f"Error in request to {url}: {e}")
    return set()

def can_fetch(url, robots_parser):
    return robots_parser.can_fetch(HEADERS['User-Agent'], url)

def get_robots_parser(domain):
    robots_url = urljoin(f"http://{domain}", '/robots.txt')
    robots_parser = RobotFileParser()
    robots_parser.set_url(robots_url)
    try:
        robots_parser.read()
    except Exception as e:
        logging.error(f"Error reading robots.txt: {e}")
    return robots_parser

def search_html_public(domain, max_depth=3, delay=1):
    robots_parser = get_robots_parser(domain)
    visited = set()
    to_visit = Queue()
    to_visit.put((f"http://{domain}", 0))
    to_visit.put((f"https://{domain}", 0))
    contains_html_public = False  

    while not to_visit.empty():
        url, depth = to_visit.get()
        if url not in visited and depth <= max_depth and can_fetch(url, robots_parser):
            visited.add(url)
            links = get_links(url, domain)
            
            for link in links:
                if link not in visited:
                    to_visit.put((link, depth + 1))
                    if 'html_public' in link:
                        contains_html_public = True
            
            time.sleep(delay)
    
    if contains_html_public:
        print(f"The domain {domain} contains links with 'html_public' in their URL.")
    else:
        print(f"The domain {domain} does not contain links with 'html_public' in their URL.")

def main():
    while True:
        while True:
            domain = input("\033[1;33mEnter the domain (without http:// or https://), or type 'exit' to quit:\033[0m ")
            if domain.lower() == 'exit':
                return

            if domain.strip():
                break
            else:
                print("\033[1;31mPlease enter a valid domain.\033[0m")

        max_depth = int(input("\033[1;33mEnter the maximum depth:\033[0m "))
        delay = float(input("\033[1;33mEnter the delay between requests (in seconds):\033[0m "))
        num_threads = int(input("\033[1;33mEnter the number of threads:\033[0m "))

        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=search_html_public, args=(domain, max_depth, delay))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()