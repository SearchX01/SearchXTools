import os
import base64
import fade
import colorama
from colorama import Fore


colorama.init(autoreset=True)

def clear_screen():
    """Efface l'écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


text = fade.greenblue("""
       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                                                 DARKGPT""")
print(text)


menu = fade.greenblue("""CODE GPT : https://gptcall.net/chat?data=%7B%22contact%22%3A%7B%22id%22%3A%22N5YPN8z7igKvqL92NCSsT%22%2C%22flow%22%3Atrue%7D%7D#chatID=%222024-09-07T14%3A08%3A55.919Z%22""")
print(menu)

def main():
   
    input(Fore.GREEN + "\nAppuyez sur Entrée pour quitter...")

    
    clear_screen()

if __name__ == "__main__":
    main()
