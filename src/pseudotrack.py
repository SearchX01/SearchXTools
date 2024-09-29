import os
import urllib.parse

def clear_screen():
    """Efface l'écran en fonction du système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')

def search_github(pseudo):
    return f"https://github.com/{pseudo}"

def search_youtube(pseudo):
    search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(pseudo)}"
    return search_url

def search_instagram(pseudo):
    return f"https://www.instagram.com/{pseudo}/"

def search_facebook(pseudo):
    search_url = f"https://www.facebook.com/public/{urllib.parse.quote(pseudo)}"
    return search_url

def search_linkedin(pseudo):
    search_url = f"https://www.linkedin.com/in/{urllib.parse.quote(pseudo)}/"
    return search_url

def search_tiktok(pseudo):
    return f"https://www.tiktok.com/@{pseudo}"

def display_results(links):
    print("\nRésultats de la recherche :")
    for platform, link in links.items():
        print(f"{platform}: {link}")

def main():
    clear_screen()  
    print("\033[92mBienvenue dans le programme de recherche de pseudonyme.\033[0m")
    
    while True:
        pseudo = input("Entrez le pseudonyme à rechercher ou tapez 'q' pour quitter : ")
        if pseudo.lower() == 'q':
            break
        
        clear_screen()  
        
        print("\033[94mRecherche en cours...\033[0m")
        
        links = {
            "GitHub": search_github(pseudo),
            "YouTube": search_youtube(pseudo),
            "Instagram": search_instagram(pseudo),
            "Facebook": search_facebook(pseudo),
            "LinkedIn": search_linkedin(pseudo),
            "TikTok": search_tiktok(pseudo),
        }
        
        display_results(links)
        
        input("\033[96mAppuyez sur Entrée pour continuer...\033[0m")
        clear_screen() 

    clear_screen() 

if __name__ == "__main__":
    main()
