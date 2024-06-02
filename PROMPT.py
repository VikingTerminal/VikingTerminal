import requests
from colorama import Fore, Style
import subprocess

print(Fore.GREEN + """
       /|   | |
     _/_\_  >_<
    .-\-/.   |
   /  | | \_ |
   \ \| |\__(/
   /(`---')  |
  / /     \  |
._.'  \'-'  /  |
`----'`=-='   '    t.me/VikingTERMINAL
""" + Style.RESET_ALL)

url = "https://api.github.com/repos/VikingTerminal/VikingTerminal/contents"

response = requests.get(url)

files = [file['name'] for file in response.json()]

tool_mapping = {
    "AirCrack_NG.py": "AirCrack NG",
    "CDN_detector.py": "CDN Detector",
    "CHAT_GPT.py": "Chat GPT",
    "DATABASE_SCANN.py": "Database Scanner",
    "DB_DATA_HUNTER.py": "Database Data Hunter",
    "DBname_scanner.py": "Database Name Scanner",
    "DNS_hijacking-py": "DNS Hijacking",
    "DNS_spoofing.py": "DNS Spoofing",
    "EMAIL_BOMBER.py": "Email Bomber",
    "EnumScanner.py": "Enumeration Scanner",
    "FAKER.py": "Faker",
    "FTPconn.py": "FTP Connection",
    "IP_associated_LINKS.py": "IP Associated Links",
    "JSON_GEN.py": "JSON Generator",
    "M3U_SNIFF.py": "M3U Sniffer",
    "NTPAMPLIFICATION.py": "NTP Amplification",
    "NetWork Scanner.py": "Network Scanner",
    "NetWork_ToolKit.py": "Network Toolkit",
    "OSINT_BOT_telegram.py": "OSINT Telegram Bot",
    "PASSWORD _GEN.py": "Password Generator",
    "PHANTOM_DOMAIN.py": "Phantom Domain",
    "README.md": "Readme",
    "REVERSE_SHELL.py": "Reverse Shell",
    "SCRAPER.py": "Scraper",
    "SHORTLINK_RESOLVER.py": "Shortlink Resolver",
    "SPY_USER.py": "User Spy",
    "sQL_query_injection.py": "SQL Query Injection",
    "SuperCat.py": "SuperCat",
    "Tracker.py": "Tracker",
    "Translator.py": "Translator",
    "URL_PASSWORDLIST_GEN.py": "URL Password List Generator",
    "URL_READER.py": "URL Reader",
    "XSS_Scanner.py": "XSS Scanner",
    "metadati_sniff.py": "Metadata Sniffer",
    "scandrir.py": "Scandrir"
}

for i, file in enumerate(files, start=1):
    print(f"{Fore.CYAN}{i}. {file}{Style.RESET_ALL}")

selection = int(input("Scegli il numero del file da eseguire: "))

if 1 <= selection <= len(files):
    selected_file = files[selection - 1]
    
    if selected_file in tool_mapping:
        tool_name = tool_mapping[selected_file]
        print(f"Hai selezionato '{selected_file}'. Ora eseguiamo '{tool_name}'.")
        
        
        subprocess.run(["python", selected_file])
    else:
        print("Non c'è alcuno strumento associato a questo file.")
else:
    print("Selezione non valida. Per favore, seleziona un numero valido.")