import os
import base64
import fade
import colorama
from colorama import Fore

# Initialisation de colorama
colorama.init(autoreset=True)

def clear_screen():
    """Efface l'écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obfuscate_code(code):
    """Obfusquer le code donné en l'encodant en base64."""
    # Encoder le code en base64
    encoded_code = base64.urlsafe_b64encode(code.encode()).decode()

    # Envelopper le code encodé dans un script simple de décodage
    obfuscated_code = f"""import base64
exec(base64.urlsafe_b64decode('{encoded_code}').decode())
"""
    return obfuscated_code

def display_banner():
    """Affiche la bannière et les informations associées."""
    banner = fade.greenblue("""
       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                          ███    ███                                          
    """)
    print(Fore.GREEN + banner)

    databaes = fade.greenblue("""
                    
        RESTORECORD 2023 : https://gofile.io/d/wAKKaz
       
        CANVA            : https://gofile.io/d/nnPzWx
                           
        INSTAGRAM        : https://gofile.io/d/cpVHO3
                           
        PROXIES          : https://mega.nz/folder/kF4nzAIa#lCNgeeo9IfwwTR6N25AxHw/folder/URR0zara
                           
        FIVEM            : https://mega.nz/folder/gT0R3SzA#kK1GkNUvnEo4XYwRjbdiIg/folder/Mas2wKaK
                           
        APPLE ID         : https://mega.nz/file/lXZGkToL#v36fZuhFv8ugER9nsZWmTmsHmrRrxNDoFddOJbJy8Gs
                           
        GMOD             : https://mega.nz/folder/YH4nkB6b#ghAgMu8SDxj7SgpdHokx4A
                           
        PANDABUY         : https://pixeldrain.com/u/W6EbqW1x
                           
        SPORT 2000       : https://gofile.io/d/PhlTvn
                           
        EPIX GAMES       : https://gofile.io/d/WBSYZB
                           
        SPOTIFY          : https://gofile.io/d/luFjHx""")
    print(databaes)

def main():
    while True:
        clear_screen()
        display_banner()
        
        # Attente de l'entrée de l'utilisateur
        input(Fore.GREEN + "Press Enter to continue...")
        
        # Efface l'écran
        clear_screen()
        
        # Votre logique pour le menu principal ou pour d'autres actions
        # Cela pourrait être le point d'entrée vers d'autres fonctions ou scripts
        print(Fore.GREEN + "Returning to main menu...")
        break  # Sortir de la boucle pour revenir au menu principal ou pour terminer le programme

if __name__ == "__main__":
    main()
