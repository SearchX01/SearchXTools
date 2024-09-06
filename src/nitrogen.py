import random
import string
from colorama import init, Fore
import fade
import os
import sys

# Initialisation de colorama
init(autoreset=True)

def clear_screen():
    """Fonction pour effacer l'écran."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Affichage du texte avec couleurs
    text = fade.greenblue("""
       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄
                                              NITRO GEN""")
    print(text)

    text2 = fade.greenblue("Press enter if you agree to this, program will start")
    print(text2)
    input()  # Attente de l'accord de l'utilisateur

    num_text = fade.greenblue("How Many Codes do you want to Generate ?")
    print(num_text)

    # Demander combien de codes générer
    num = input("Please enter the number of codes to generate: ").strip()

    # Assurer que l'entrée utilisateur est un nombre entier
    try:
        num = int(num)
    except ValueError:
        print(Fore.RED + "Invalid number provided. Please enter a valid integer.")
        input("Press Enter to exit.")
        return

    charSet = f"{string.ascii_uppercase}{string.digits}{string.ascii_lowercase}"
    bigStr = ""

    # Génération des codes
    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
        print(Fore.BLUE + 'Wait, Generating for you!')

        for i in range(num):
            bigStr += f'https://discord.gift/{"".join(random.choices(charSet, k=16))}\n'
            if i % 100_000 == 0:
                file.write(bigStr)
                bigStr = ""

        # Write remaining data
        if bigStr:
            file.write(bigStr)

        print(Fore.CYAN + 'Successfully generated. The codes are in Nitro Codes.txt')

    # Attendre que l'utilisateur appuie sur "Enter" pour fermer
    input("Press Enter to return to the main menu...")

    # Effacer l'écran et retourner au menu principal
    clear_screen()
    return

if __name__ == "__main__":
    main()
