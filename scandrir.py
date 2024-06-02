import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
import time

# Inizializza colorama
init(autoreset=True)

# Stampa l'immagine solo una volta all'inizio del programma
print(Fore.MAGENTA + """
 
| | |<_>| |<_>._ _  _ 
| '   / /| || ' |/ . |
|__/ |__\_\|__|_|\_. |
                     <___'
  t.me/Rapid85
""")

while True:
    # Chiedi all'utente di inserire il dominio o "exit" per uscire
    print(Fore.GREEN + "Inserisci il dominio (senza http/https) o scrivi 'exit' per uscire: ", end="")
    domain = input().strip()

    if domain.lower() == 'exit':
        print(Fore.LIGHTYELLOW_EX + "Grazie per aver provato il tool.t.me/Rapid85")
        break

    url = f"http://{domain}"

    try:
        response = requests.get(url)

        # Verifica se la richiesta ha avuto successo
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Esempio: Trova tutti i link nella pagina
        links = soup.find_all('a')

        # Chiedi all'utente il nome del file di output
        print(Fore.GREEN + "Desideri salvare i risultati in un file? (yes/no): ", end="")
        save_results = input().strip().lower()

        if save_results == 'yes':
            print(Fore.GREEN + "Inserisci il nome del file di output (senza estensione): ", end="")
            output_file_name = input().strip() + '.txt'

            with open(output_file_name, 'w', encoding='utf-8') as output_file:
                for link in links:
                    href = link.get('href')
                    if href:
                        output_file.write(href + '\n')
                        print(Fore.CYAN + href)
                        time.sleep(0.1)  # Aggiungi un ritardo per l'effetto macchina da scrivere

            print(Fore.LIGHTYELLOW_EX + f"Risultati salvati nel file: {output_file_name}")
        elif save_results == 'no':
            for link in links:
                href = link.get('href')
                if href:
                    print(Fore.CYAN + href)
                    time.sleep(0.1)  # Aggiungi un ritardo per l'effetto macchina da scrivere
        else:
            print(Fore.RED + "Risposta non valida. I risultati non saranno salvati.")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Errore nella richiesta per il dominio {domain}: {e}. Il dominio potrebbe non esistere.")
