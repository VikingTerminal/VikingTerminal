import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
import time

# Initialize colorama
init(autoreset=True)

# Print the image only once at the beginning of the program
print(Fore.MAGENTA + """
 
| | |<_>| |<_>._ _  _ 
| '   / /| || ' |/ . |
|__/ |__\_\|__|_|\_. |
                     <___'
  t.me/Rapid85
""")

while True:
    # Ask the user to input the domain or "exit" to quit
    print(Fore.GREEN + "Enter the domain (without http/https) or type 'exit' to quit: ", end="")
    domain = input().strip()

    if domain.lower() == 'exit':
        print(Fore.LIGHTYELLOW_EX + "Thank you for trying the tool.t.me/Rapid85")
        break

    url = f"http://{domain}"

    try:
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Find all links on the page
        links = soup.find_all('a')

        # Ask the user if they want to save the results to a file
        print(Fore.GREEN + "Do you want to save the results to a file? (yes/no): ", end="")
        save_results = input().strip().lower()

        if save_results == 'yes':
            print(Fore.GREEN + "Enter the output file name (without extension): ", end="")
            output_file_name = input().strip() + '.txt'

            with open(output_file_name, 'w', encoding='utf-8') as output_file:
                for link in links:
                    href = link.get('href')
                    if href:
                        output_file.write(href + '\n')
                        print(Fore.CYAN + href)
                        time.sleep(0.1)  # Add a delay for typewriter effect

            print(Fore.LIGHTYELLOW_EX + f"Results saved to file: {output_file_name}")
        elif save_results == 'no':
            for link in links:
                href = link.get('href')
                if href:
                    print(Fore.CYAN + href)
                    time.sleep(0.1)  # Add a delay for typewriter effect
        else:
            print(Fore.RED + "Invalid response. Results will not be saved.")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error requesting domain {domain}: {e}. The domain may not exist.")