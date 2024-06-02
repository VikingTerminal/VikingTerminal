import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_databases(url, depth=0):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            database_links = set()
            text_content = soup.get_text().lower()
            keywords = ['database', 'db', 'data', 'dataset', 'repository']
            for keyword in keywords:
                if keyword in text_content:
                    database_links.add(url)
                    break

            internal_links = [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True) if not link.get('href').startswith('http')]
            print(f"Scanning level {depth}: {len(internal_links)} internal links")
            for internal_link in internal_links:
                database_links.update(find_databases(internal_link, depth + 1))

            return database_links
        else:
            print(f"Error retrieving page {url}: {response.status_code}")
            return set()
    except Exception as e:
        print(f"An error occurred while scanning the site {url}: {e}")
        return set()

if __name__ == "__main__":
    domain = input("Enter the domain to scan (e.g., https://example.com): ")
    databases = find_databases(domain)
    if databases:
        print("Databases found:")
        for db in databases:
            print(db)
    else:
        print("No databases found.")