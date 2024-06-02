from googletrans import Translator, LANGUAGES
from termcolor import colored
import sys
import random
import time

def colore_random():
    colori_disponibili = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    return random.choice(colori_disponibili)

def effetto_macchina_da_scrivere(testo):
    colore = colore_random()
    for carattere in testo:
        print(colored(carattere, colore), end='', flush=True)
        time.sleep(0.05)  # Aggiungi una pausa di 0.05 secondi tra i caratteri
    print()  # Vai a capo alla fine del testo

def traduci_testo():
    translator = Translator()

    frase_prompt = "Inserisci il testo da tradurre (scrivi 'exit' per uscire): "
    effetto_macchina_da_scrivere(frase_prompt)

    while True:
        testo_da_tradurre = input()

        if testo_da_tradurre.lower() == 'exit':
            print(colored("\nGrazie per aver utilizzato il traduttore! Seguici su t.me/vikingterminal", 'green'))
            sys.exit()

        print(colored("\nTraduzione in corso...", 'yellow'))

        print(colored(f"\nTesto originale:\n", 'cyan'))
        effetto_macchina_da_scrivere(testo_da_tradurre)

        print("Lingue disponibili:")
        for codice, lingua in LANGUAGES.items():
            print(f"{colored(codice, 'yellow')}: {colored(lingua, 'cyan')}")

        lingua_destinazione = input("Inserisci il codice della lingua di destinazione: ")

        if lingua_destinazione not in LANGUAGES:
            print(colored("Errore: Lingua di destinazione non valida.", 'red'))
            continue

        try:
            traduzione = translator.translate(testo_da_tradurre, dest=lingua_destinazione)
            testo_tradotto = traduzione.text
            lingua_origine = LANGUAGES[traduzione.src]
            
            print(colored(f"\nTesto tradotto ({lingua_origine}):", 'cyan'))
            effetto_macchina_da_scrivere(testo_tradotto)
        except Exception as e:
            print(colored(f"Si è verificato un errore durante la traduzione: {e}", 'red'))

        print(colored("\nScrivi 'exit' per uscire oppure continua a scrivere per tradurre altro testo", 'yellow'))

if __name__ == "__main__":
    traduci_testo()
