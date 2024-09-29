import os
import requests
from tabulate import tabulate
import fade
from colorama import Fore

def clear_console():
    """Efface l'écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_github_user_info(username, token=None):
    try:
        url = f"https://api.github.com/users/{username}"
        headers = {}
        if token:
            headers['Authorization'] = f'token {token}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            user_info = {
                "Pseudo": user_data.get("login", "Non disponible"),
                "Nom complet": user_data.get("name", "Non disponible"),
                "Bio": user_data.get("bio", "Non disponible"),
                "Email": user_data.get("email", "Non disponible"),
                "Entreprise": user_data.get("company", "Non disponible"),
                "Localisation": user_data.get("location", "Non disponible"),
                "Blog": user_data.get("blog", "Non disponible"),
                "Nombre de dépôts publics": user_data.get("public_repos", "Non disponible"),
                "Nombre de followers": user_data.get("followers", "Non disponible"),
                "Nombre de following": user_data.get("following", "Non disponible"),
                "Date de création": user_data.get("created_at", "Non disponible"),
            }
            return user_info
        else:
            print(fade.greenblue(f"Erreur {response.status_code}: Impossible de récupérer les informations pour {username}"))
            return None
    except requests.exceptions.RequestException as e:
        print(fade.greenblue(f"Erreur lors de la requête: {e}"))
        return None

def display_table(user_info):
    table = [
        ["Pseudo", user_info["Pseudo"]],
        ["Nom complet", user_info["Nom complet"]],
        ["Bio", user_info["Bio"]],
        ["Email", user_info["Email"]],
        ["Entreprise", user_info["Entreprise"]],
        ["Localisation", user_info["Localisation"]],
        ["Blog", user_info["Blog"]],
        ["Dépôts publics", user_info["Nombre de dépôts publics"]],
        ["Followers", user_info["Nombre de followers"]],
        ["Following", user_info["Nombre de following"]],
        ["Date de création", user_info["Date de création"]],
    ]
    print(fade.greenblue("\nInformations sur l'utilisateur GitHub :\n"))
    print(fade.greenblue(tabulate(table, headers=["Champ", "Valeur"], tablefmt="grid")))

def github_lookup():
    while True:
        clear_console()
        text = fade.greenblue("""                ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
          ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
          ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
          ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
        ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
                 ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
           ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
         ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                                                         GITHUB LOOKUP""")
        print(text)

        username = input(fade.greenblue("Entrez le pseudo GitHub : ")).strip()
        if not username:
            print(fade.greenblue("Aucun pseudo entré. Retour au menu principal."))
            return
        user_info = get_github_user_info(username)
        if user_info:
            display_table(user_info)
        input(fade.greenblue("\nAppuyez sur Entrée pour revenir au menu principal..."))
        return  

def main_menu():
    while True:
        clear_console()
        text = fade.greenblue("""          ▄████████    ▄████████     ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
          ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
          ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
          ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
        ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
                 ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
           ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
         ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                                                         MAIN MENU""")
        print(text)

        print(fade.greenblue("\n1. GitHub Lookup\n2. Quitter"))
        choice = input(fade.greenblue("Choisissez une option : ")).strip()
        if choice == "1":
            clear_console()  
            github_lookup()
        elif choice == "2":
            clear_console() 
            break  
        else:
            print(fade.greenblue("Choix invalide, veuillez réessayer."))

if __name__ == "__main__":
    main_menu()
