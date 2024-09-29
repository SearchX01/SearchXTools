import os
import colorama
from colorama import Fore
import fade
import sys
import pystyle

colorama.init(autoreset=True) 

def display_menu():
    text = fade.greenblue("""
       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄  v 4
                                             ███    ███                                          
                                               WalSo'211 X Purple""")
    print(Fore.GREEN + text)
    
    menu = fade.greenblue("""
   ╔═══                     ═══╗ ╔═══                     ═══╗ ╔═══                   ═══╗╔═══                     ═══╗
   ║  {1} SearchX Obfuscator   ║ ║  {5} SearchX Deface       ║ ║  {9}  SearchX Deobfusc  ║║  {13} SearchX DarkGPT     ║
   ║  {2} SearchX Lookup       ║ ║  {6} SearchX Web to Ip    ║ ║  {10} SearchX Token Inf ║║  {14} SearchX IA CRACKED  ║
   ║  {3} SearchX Nitro Gen    ║ ║  {7} SearchX Dump Lookup  ║ ║  {11} SearchX DMALL     ║║  {15} SearchX CODE GPT    ║
   ║  {4} SearchX Database     ║ ║  {8} SearchX Web Stealer  ║ ║  {12} SearchX KeyLogs   ║║  {16} SearchX Webcam grab ║
   ╚═══                     ═══╝ ╚═══                     ═══╝ ╚═══                   ═══╝╚═══                     ═══╝
   ╔═══                     ═══╗ ╔═══                     ═══╗ ╔═══                   ═══╗╔═══                     ═══╗
   ║  {17} SearchX Website     ║ ║  {21} SearchX Phone Info  ║ ║  {25} SearchX Hypesquad ║║  {29} SearchX NazAPI      ║
   ║  {18} SearchX Tiktok boost║ ║  {22} SearchX Git Lookup  ║ ║  {26} SearchX API       ║║  {30} SearchX VPN         ║
   ║  {19} SearchX antilink byp║ ║  {23} SearchX Name Track  ║ ║  {27} SearchX Socials   ║║  {31} SearchX PROXIES     ║
   ║  {20} SearchX Roblox Info ║ ║  {24} SearchX Account Gen ║ ║  {28} SearchX Discord   ║║  {32} SearchX UPDATER     ║
   ╚═══                     ═══╝ ╚═══                     ═══╝ ╚═══                   ═══╝╚═══                     ═══╝
                                                       {33} For Leave !""")
    
    
    print(Fore.GREEN + menu)

def main_menu():
    try:
        username = os.getlogin() 
    except OSError:
        username = os.environ.get('USER') 

    while True:
        display_menu()
        choice_prompt = f"{Fore.GREEN}{username}@searchx:~$ " 
        sys.stdout.write(choice_prompt)  
        sys.stdout.flush()  
        choice = input().strip()  

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
        elif choice == '13':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/darkgpt.py')
        elif choice == '14':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/iajailbreak.py')                       
        elif choice == '15':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/codegpt.py')          
        elif choice == '16':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/webcam.py')          
        elif choice == '17':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/searchxweb.py')                
        elif choice == '18':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/tiktokboost.py')        
        elif choice == '19':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/antilinkbypass.py')         
        elif choice == '20':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/robloxlookup.py')
        elif choice == '21':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/foneinfo.py')      
        elif choice == '22':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/gitlookup.py')         
        elif choice == '23':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/pseudotrack.py')             
        elif choice == '24':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/accgen.py')         
        elif choice == '25':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/hypesquad.py')          
        elif choice == '26':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/api.py')           
        elif choice == '27':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/socials.py')          
        elif choice == '28':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/discord.py')          
        elif choice == '29':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/nazapi.py')           
        elif choice == '30':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/vpn.py')          
        elif choice == '31':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/proxy.py')        
        elif choice == '32':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python src/update.py')           
        elif choice == '33':
            print(Fore.GREEN + "Sortie du programme...")
            break
        elif choice == '':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            print(Fore.RED + "Choix non valide. Veuillez réessayer.")
            input(Fore.GREEN + "Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main_menu()
