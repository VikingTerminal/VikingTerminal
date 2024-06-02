import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import init, Fore, Style


init(autoreset=True)

def trova_database(url, depth=0):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            database_links = set()
            text_content = soup.get_text().lower()
            keywords = ['database', 'db', 'data', 'dataset', 'repository', 
            'scientific', 'research', 'study', 
            'finance', 'stock', 'market', 
            'health', 'medical', 'education', 
            'government', 'public', 'policy', 
            'geospatial', 'environment', 'climate',
            'social', 'demographic', 'economic',
            'business', 'industry', 'technology',
            'energy', 'transportation', 'agriculture']
            for keyword in keywords:
                if keyword in text_content:
                    database_links.add(url)
                    break
            
            internal_links = [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True) if not link.get('href').startswith('http')]
            print(f"{Fore.GREEN}Scansione livello {depth}: {len(internal_links)} link interni{Style.RESET_ALL}")
            for internal_link in internal_links:
                database_links.update(trova_database(internal_link, depth + 1))
            
            return database_links
        else:
            print(f"{Fore.RED}Errore durante il recupero della pagina {url}: {response.status_code}{Style.RESET_ALL}")
            return set()
    except Exception as e:
        print(f"{Fore.RED}Si è verificato un errore durante la scansione del sito {url}: {e}{Style.RESET_ALL}")
        return set()

if __name__ == "__main__":
    dominio = input(f"{Fore.CYAN}Inserisci il dominio da scansionare (es. https://example.com): {Style.RESET_ALL}")
    databases = trova_database(dominio)
    if databases:
        print(f"{Fore.GREEN}Database trovati:{Style.RESET_ALL}")
        for db in databases:
            print(db)
    else:
        print(f"{Fore.YELLOW}Nessun database trovato.{Style.RESET_ALL}")
