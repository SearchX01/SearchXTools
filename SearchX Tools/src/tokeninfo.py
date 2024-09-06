import requests
import datetime
import os
import fade
import colorama

colorama.init(autoreset=True)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_token(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    # Make a request to the Discord API to fetch user information
    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    
    if response.status_code == 200:
        user_info = response.json()
        return user_info
    elif response.status_code == 401:
        print(fade.greenblue("Token invalide."))
        return None
    else:
        print(fade.greenblue(f"Erreur lors de la vérification du token : {response.status_code}"))
        return None

def get_creation_date(user_id):
    discord_epoch = 1420070400000
    timestamp = ((int(user_id) >> 22) + discord_epoch) / 1000
    
    # Use timezone-aware datetime to avoid deprecation warning
    creation_date = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
    return creation_date.strftime('%Y-%m-%d %H:%M:%S UTC')

def display_user_info(user_info):
    user_id = user_info['id']
    username = user_info['username']
    discriminator = user_info['discriminator']
    email = user_info.get('email', 'Non fourni')
    phone = user_info.get('phone', 'Non fourni')
    mfa_enabled = user_info.get('mfa_enabled', False)
    verified = user_info.get('verified', False)
    premium_type = user_info.get('premium_type', 0)

    # Determine if the user has Nitro
    nitro_status = "Aucun"
    if premium_type == 1:
        nitro_status = "Nitro Classic"
    elif premium_type == 2:
        nitro_status = "Nitro"

    creation_date = get_creation_date(user_id)

    # Display the information in a table-like format
    print(fade.greenblue(f"""
    Informations du compte Discord :
    ╔═════════════════════════════════╤═════════════════════════════════════════╗
    ║ Nom d'utilisateur               │ {username}#{discriminator}              
    ╟─────────────────────────────────┼─────────────────────────────────────────╢
    ║ ID utilisateur                  │ {user_id}                               
    ╟─────────────────────────────────┼─────────────────────────────────────────╢
    ║ Date de création du compte      │ {creation_date}                         
    ╟─────────────────────────────────┼─────────────────────────────────────────╢
    ║ Adresse email                   │ {email}                                 
    ╟─────────────────────────────────┼─────────────────────────────────────────╢
    ║ Numéro de téléphone             │ {phone}                                 
    ╟─────────────────────────────────┼─────────────────────────────────────────╢
    ║ 2FA activée                     │ {'Oui' if mfa_enabled else 'Non'}        
    ╟─────────────────────────────────┼─────────────────────────────────────────╢
    ║ Compte vérifié                  │ {'Oui' if verified else 'Non'}           
    ╟─────────────────────────────────┼─────────────────────────────────────────╢
    ║ Statut Nitro                    │ {nitro_status}                           
    ╚═════════════════════════════════╧═════════════════════════════════════════╝
    """))

text = fade.greenblue ("""
       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                             ███    ███                                          """)
print (text)
def main():
    print(fade.greenblue("Entrez votre token Discord :  "))
    token = input().strip()  # Retiré le "fade.greenblue("> ")"
    
    user_info = check_token(token)
    if user_info:
        clear_screen()  # Efface l'écran avant d'afficher les résultats
        display_user_info(user_info)

    # Wait for user input before clearing the screen and closing the script
    input(fade.greenblue("Appuyez sur Entrée pour quitter."))
    clear_screen()

if __name__ == "__main__":
    main()
