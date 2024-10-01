import requests, string, threading, time, random, zlib, os, datetime, fade, phonenumbers, base64, pyshorteners, binascii, marshal, getpass
from marshal import dumps
from colorama import Fore, Style, init
from pystyle import Colors, Colorate
from phonenumbers import geocoder, carrier, timezone


init(autoreset=True)

def clear_screen():
   
    os.system('cls' if os.name == 'nt' else 'clear')

def default_menu():
  
    print("Retour au menu par défaut...")

def Obf():
    clear_screen()
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
                                             OBFUSCATOR""")
    print(banner)

    def generer_chaine_aleatoire(longueur=10):
        
        return ''.join(random.choices(string.ascii_letters + string.digits, k=longueur))

    def obfusquer_code(code_source, couches=1):
        
        code = code_source
        for _ in range(couches):
            try:
                code_compile = compile(code, '<string>', 'exec')
                code_serialise = marshal.dumps(code_compile)
                code_compresse = zlib.compress(code_serialise)
                code_encode = base64.b64encode(code_compresse).decode()
                code = f"""
import marshal; import zlib; import base64; exec(marshal.loads(zlib.decompress(base64.b64decode('{code_encode}'))))
"""
            except Exception as e:
                print(f"Erreur lors de l'obfuscation : {e}")
                return None
        return code

    def obfusquer_fichier(fichier_entree, couches=1):
        """ Obfusque un fichier source et enregistre le résultat sur le bureau. """
        try:
           
            with open(fichier_entree, 'r', encoding='utf-8') as f:
                contenu_script = f.read()

     
            code_obfusque = obfusquer_code(contenu_script, couches)
            if not code_obfusque:
                print("L'obfuscation a échoué.")
                return

          
            code_base16 = binascii.hexlify(code_obfusque.encode()).decode()
            code_base32 = base64.b32encode(code_base16.encode()).decode()

            code_final_obfusque = f"""
import base64; import binascii
exec(binascii.unhexlify(base64.b32decode('{code_base32}')).decode())
"""

         
            nom_fichier, extension = os.path.splitext(fichier_entree)
            fichier_sortie = f"{nom_fichier}-obf{extension}"
            chemin_bureau = os.path.join(os.path.expanduser("~"), "Desktop", os.path.basename(fichier_sortie))

            with open(chemin_bureau, 'w', encoding='utf-8') as f:
                f.write(code_final_obfusque)

            print(f"Obfuscation terminée. Le script obfusqué est enregistré sous '{chemin_bureau}'.")

        except FileNotFoundError:
            print(f"Le fichier '{fichier_entree}' est introuvable.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
        finally:
            default_menu()

    fichier_entree = input(">> Glissez et déposez le fichier à obfusquer ici : ").strip().strip('"')

    try:
        couches = int(input(">> Nombre de couches d'obfuscation (par défaut 1) : ") or 1)
    except ValueError:
        print("Valeur incorrecte, le nombre de couches doit être un entier.")
        couches = 1

    obfusquer_fichier(fichier_entree, couches)

  
    input(f"{Fore.GREEN}[✔] Script Obfusqué avec succès. Appuyez sur Entrée pour effacer l'écran.")
    clear_screen()  

if __name__ == "__main__":
    Obf()
