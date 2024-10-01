import os
import base64
import colorama
from colorama import Fore
import fade

colorama.init(autoreset=True)

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def deobfuscate_code(obfuscated_code):
    
    try:
       
        encoded_code = obfuscated_code.split("base64.urlsafe_b64decode('")[1].split("').decode()")[0]
      
        decoded_code = base64.urlsafe_b64decode(encoded_code.encode()).decode()
        return decoded_code
    except (IndexError, base64.binascii.Error) as e:
        return f"Erreur lors de la déobfuscation : {e}"

def main():
    while True:
       
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
                                             DEOBFUSCATOR""")
        print(Fore.GREEN + banner)
        
 
        file_path = input(Fore.GREEN + "Veuillez saisir le chemin complet du fichier .py obfusqué et appuyer sur Entrée.\nChemin du fichier .py : ")

        if file_path.strip() == "":
            clear_screen()
            print(Fore.GREEN + banner)
            print(Fore.RED + "Aucun fichier n'a été fourni. Veuillez glisser-déposer un fichier .py sur ce script et appuyer sur Entrée.")
            input(Fore.GREEN + "Appuyez sur Entrée pour revenir au menu.")
            clear_screen()
            continue
        
        if not file_path.lower().endswith('.py'):
            clear_screen()
            print(Fore.GREEN + banner)
            print(Fore.RED + "Le fichier doit avoir une extension .py")
            input(Fore.GREEN + "Appuyez sur Entrée pour revenir au menu.")
            clear_screen()
            continue

        if not os.path.isfile(file_path):
            clear_screen()
            print(Fore.GREEN + banner)
            print(Fore.RED + "Le fichier spécifié n'existe pas.")
            input(Fore.GREEN + "Appuyez sur Entrée pour revenir au menu.")
            clear_screen()
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                obfuscated_code = file.read()
        except UnicodeDecodeError:
            clear_screen()
            print(Fore.GREEN + banner)
            print(Fore.RED + "Erreur de décodage du fichier. Assurez-vous que le fichier est encodé en UTF-8.")
            input(Fore.GREEN + "Appuyez sur Entrée pour revenir au menu.")
            clear_screen()
            continue

        print(Fore.GREEN + "Déobfuscation en cours...")

        deobfuscated_code = deobfuscate_code(obfuscated_code)


        deobfuscated_file_path = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}_deobfuscated.py")
        with open(deobfuscated_file_path, 'w', encoding='utf-8') as file:
            file.write(deobfuscated_code)

        clear_screen()
        print(Fore.GREEN + banner)
        print(Fore.GREEN + f"Code déobfusqué sauvegardé sous {deobfuscated_file_path}")


        input(Fore.GREEN + "Appuyez sur Entrée pour revenir au menu principal...")
        clear_screen()
        break   

if __name__ == "__main__":
    main()
