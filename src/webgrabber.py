import os
import shutil
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook
import zipfile
import fade 


def download_page(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

  
        with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as file:
            file.write(str(soup))

  
        for resource in soup.find_all(['img', 'link', 'script']):
            src = resource.get('src') or resource.get('href')
            if src and (src.endswith('.jpg') or src.endswith('.png') or src.endswith('.css') or src.endswith('.js')):
                download_resource(url, src, folder)

    except requests.RequestException as e:
        print(f"Erreur lors du téléchargement de la page: {e}")
        raise
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        raise


def download_resource(base_url, resource_url, folder):
    try:
        if not resource_url.startswith('http'):
            resource_url = os.path.join(base_url, resource_url)
        resource_url = resource_url.replace('\\', '/')

        local_filename = os.path.join(folder, os.path.basename(resource_url))
        with requests.get(resource_url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

    except requests.RequestException as e:
        print(f"Erreur lors du téléchargement de la ressource {resource_url}: {e}")


def zip_site(folder):
    try:
        zip_filename = folder + '.zip'
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder))
        return zip_filename
    except Exception as e:
        print(f"Erreur lors de la création du fichier ZIP: {e}")
        raise


def send_to_discord(zip_file, webhook_url):
    try:
        webhook = DiscordWebhook(url=webhook_url)
        with open(zip_file, "rb") as f:
            webhook.add_file(file=f.read(), filename=os.path.basename(zip_file))
        webhook.execute()
    except Exception as e:
        print(f"Erreur lors de l'envoi au webhook Discord: {e}")
        raise


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_main_menu():
    clear_screen()
    text = fade.greenblue ("""       ▄████████    ▄████████  ▄████████     ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███  ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀   ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
           ███    ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
     ▄█    ███    ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
    ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                            ███    ███                  Web Stealer             """)
    print(text)
    choicetext = fade.greenblue ("Choisissez 1 pour copier un site web et 2 pour quitter")
    print(choicetext)
    choice = input("Votre choix: ")
    return choice


def main():
    while True:
        choice = show_main_menu()
        if choice == '1':
            try:
       
                url = input("Entrez l'URL du site web: ")
                webhook_url = input("Entrez l'URL du webhook Discord: ")
                folder_name = 'downloaded_site'


                if os.path.exists(folder_name):
                    shutil.rmtree(folder_name)
                os.makedirs(folder_name)

            
                download_page(url, folder_name)

       
                zip_file = zip_site(folder_name)

        
                send_to_discord(zip_file, webhook_url)

       
                os.remove(zip_file)
                shutil.rmtree(folder_name)

                print("Le site a été téléchargé, zippé et envoyé à Discord avec succès.")
            
            except Exception as e:
                print(f"Une erreur s'est produite: {e}")
            
       
            input("\nAppuyez sur Entrée pour revenir au menu principal...")
        
        elif choice == '2':
            clear_screen()
            break
        
        else:
            print("Option invalide, veuillez réessayer.")


        clear_screen()


if __name__ == "__main__":
    main()
