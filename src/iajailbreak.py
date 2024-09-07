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


menu = fade.greenblue("""CODE GPT : https://github.com/friuns2/BlackFriday-GPTs-Prompts/blob/main/Jailbreaks.md""")
print(menu)

def main():
   
    input(Fore.GREEN + "\nAppuyez sur Entrée pour quitter...")

    
    clear_screen()

if __name__ == "__main__":
    main()
