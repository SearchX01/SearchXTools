import random
import string
from colorama import init, Fore
import fade
import os
import sys


init(autoreset=True)

def clear_screen():
    """Fonction pour effacer l'écran."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
   
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
    input() 

    num_text = fade.greenblue("How Many Codes do you want to Generate ?")
    print(num_text)


    num = input("Please enter the number of codes to generate: ").strip()

  
    try:
        num = int(num)
    except ValueError:
        print(Fore.RED + "Invalid number provided. Please enter a valid integer.")
        input("Press Enter to exit.")
        return

    charSet = f"{string.ascii_uppercase}{string.digits}{string.ascii_lowercase}"
    bigStr = ""

   
    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
        print(Fore.BLUE + 'Wait, Generating for you!')

        for i in range(num):
            bigStr += f'https://discord.gift/{"".join(random.choices(charSet, k=16))}\n'
            if i % 100_000 == 0:
                file.write(bigStr)
                bigStr = ""

 
        if bigStr:
            file.write(bigStr)

        print(Fore.CYAN + 'Successfully generated. The codes are in Nitro Codes.txt')

 
    input("Press Enter to return to the main menu...")

 
    clear_screen()
    return

if __name__ == "__main__":
    main()
