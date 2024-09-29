import phonenumbers
from phonenumbers import geocoder, carrier
import fade
from colorama import Fore, init
import os

init(autoreset=True)


text = fade.greenblue("""       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄
                                                                   Phone Number INFO""")
print(text)

def generer_liens_messagerie(numero_telephone):
    numero_telephone = numero_telephone.strip()
    try:
        numero_parsed = phonenumbers.parse(numero_telephone)
        if not phonenumbers.is_valid_number(numero_parsed):
            return f"{Fore.RED}Le numéro {numero_telephone} n'est pas valide."

        pays = geocoder.description_for_number(numero_parsed, "fr")
        operateur = carrier.name_for_number(numero_parsed, "fr")

        liens = {
            "WhatsApp": f"https://wa.me/{numero_parsed.country_code}{numero_parsed.national_number}",
            "Viber": f"viber://add?number={numero_parsed.country_code}{numero_parsed.national_number}",
            "Telegram": f"https://t.me/+{numero_parsed.country_code}{numero_parsed.national_number}",
        }

        info_numero = f"{Fore.GREEN}Le numéro {numero_telephone} est valide.\n"
        info_numero += f"{Fore.CYAN}Pays: {pays}\n"
        info_numero += f"{Fore.CYAN}Opérateur: {operateur if operateur else 'Inconnu'}\n"
        info_numero += "\nLiens pour messageries :\n"
        for app, lien in liens.items():
            info_numero += f"{Fore.YELLOW}{app}: {lien}\n"
        
        return info_numero

    except phonenumbers.phonenumberutil.NumberParseException:
        return f"{Fore.RED}Le numéro {numero_telephone} n'est pas reconnu comme un numéro de téléphone valide."

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rechercher_numero_telephone():
    while True:
        prompt = fade.greenblue("Saisir le numéro de téléphone avec l'indicatif pays (ex: +33612345678) : ")
        print(prompt, end="")
        numero_saisi = input().strip()
        resultat = generer_liens_messagerie(numero_saisi)
        print(resultat)
        input("\nAppuyez sur Entrée pour revenir au menu...")
        clear_screen()
        break

if __name__ == "__main__":
    rechercher_numero_telephone()
