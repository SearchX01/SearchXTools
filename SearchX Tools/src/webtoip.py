import socket
import fade
import os
import platform

def get_ip_and_port(domain):
    """Obtient l'adresse IP et le port d'un domaine donné."""
    try:
        # Résolution DNS pour obtenir l'adresse IP
        ip_address = socket.gethostbyname(domain)
        
        # Affichage de l'adresse IP et du port
        print(f"{fade.greenblue('Domain:')} {fade.greenblue(domain)}")
        print(f"{fade.greenblue('IP Address:')} {fade.greenblue(ip_address)}")
        print(f"{fade.greenblue('Port:')} {fade.greenblue('HTTP (80) or HTTPS (443)')}")
    except socket.gaierror:
        print(f"{fade.red('Error: Invalid domain or unable to resolve IP.')}")
    except Exception as e:
        print(f"{fade.red(f'An unexpected error occurred: {e}')}")
    
def clear_screen():
    """Efface l'écran du terminal pour différentes plateformes."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def display_main_menu():
    """Affiche le menu principal."""
    clear_screen()
    text = fade.greenblue("""
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
    print(text)
    print(f"{fade.greenblue('1. Saisir un site web pour obtenir son IP et port')}")
    print(f"{fade.greenblue('2. Quitter')}")
    
def main():
    while True:
        display_main_menu()
        choice = input(f"{fade.greenblue('Choisissez une option (1 ou 2): ')}").strip()

        if choice == '1':
            clear_screen()
            domain = input(f"{fade.greenblue('Entrez le site que vous voulez : ')}").strip()
            clear_screen()
            get_ip_and_port(domain)
            input(f"{fade.greenblue('Appuyez sur Entrée pour revenir au menu principal...')}")
        elif choice == '2':
            clear_screen()
            # Efface l'écran avant de quitter
            clear_screen()
            break
        else:
            print(f"{fade.red('Option invalide. Veuillez choisir 1 ou 2.')}")
            input(f"{fade.greenblue('Appuyez sur Entrée pour essayer à nouveau...')}")

if __name__ == "__main__":
    main()
