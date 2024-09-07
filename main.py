import os
import colorama
from colorama import Fore
import fade
import sys
import pystyle

colorama.init(autoreset=True) 

def display_menu():
    """Affiche le menu principal avec des options."""
    text = fade.greenblue("""
       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄  v 2.0
                                             ███    ███                                          
                                               VenzOT X Purple""")
    print(Fore.GREEN + text)
    
    menu = fade.greenblue("""
   ╔═══                     ═══╗ ╔═══                     ═══╗ ╔═══                   ═══╗╔═══                     ═══╗
   ║  {1} SearchX Obfuscator   ║ ║  {5} SearchX Deface       ║ ║  {9}  SearchX Deobfusc  ║║  {13} SearchX DarkGPT     ║
   ║  {2} SearchX Lookup       ║ ║  {6} SearchX Web to Ip    ║ ║  {10} SearchX Token Inf ║║  {14} SearchX IA CRACKED  ║
   ║  {3} SearchX Nitro Gen    ║ ║  {7} SearchX Dump Lookup  ║ ║  {11} SearchX DMALL     ║║  {15} SearchX CODE GPT    ║
   ║  {4} SearchX Database     ║ ║  {8} SearchX Web Stealer  ║ ║  {12} SearchX KeyLogs   ║║  {16} SearchX Webcam grab ║
   ╚═══                     ═══╝ ╚═══                     ═══╝ ╚═══                   ═══╝╚═══                     ═══╝
   ╔═══                     ═══╗ ╔═══                     ═══╗ ╔═══                   ═══╗╔═══                     ═══╗
   ║  {17} SearchX Website     ║ ║  {21} SearchX Phone Info  ║ ║  {25} SearchX Tokn brute║║  {29} SearchX TECHS       ║
   ║  {18} SearchX Tiktok boost║ ║  {22} SearchX DDOS        ║ ║  {26} SearchX Hypesquad ║║  {30} SearchX VPN         ║
   ║  {19} SearchX Cookie Steal║ ║  {23} SearchX Name Track  ║ ║  {27} SearchX API       ║║  {31} SearchX PROXIES     ║
   ║  {20} SearchX Roblox Info ║ ║  {24} SearchX Token Steal ║ ║  {28} SearchX Socials   ║║  {32} SearchX UPDATER     ║
   ╚═══                     ═══╝ ╚═══                     ═══╝ ╚═══                   ═══╝╚═══                     ═══╝""")
    print(Fore.GREEN + menu)

def main_menu():
    try:
        username = os.getlogin() 
    except OSError:
        username = os.environ.get('USER') 

    while True:
        display_menu()
        choice_prompt = fade.greenblue(f"┌───{{{username}}}-(@SearchX)-(.gg/searchx)\n└─> ")

        sys.stdout.write(choice_prompt)  
        sys.stdout.flush()  
        choice = input()  

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/obfuscator.py')
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/lookup.py')
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/nitrogen.py')
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/database.py')
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/deface.py')
        elif choice == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/webtoip.py')
        elif choice == '7':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/dumplookup.py')
        elif choice == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/webgrabber.py')
        elif choice == '9':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/deobfuscator.py')
        elif choice == '10':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/tokeninfo.py')       
        elif choice == '11':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/dmall.py')              
        elif choice == '12':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/keylogger.py')        
        elif choice == '16':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/webcam.py')             
            os.system('python src/keylogger.py')        
        elif choice == '32':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/update.py')           
        
        elif choice == '33':
            print(Fore.GREEN + "Sortie du programme...")
            break
        else:
            print(Fore.RED + "Choix non valide. Veuillez réessayer.")
            input(Fore.GREEN + "Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main_menu()
