import os
from pystyle import Colorate, Colors
import fade

os.system('cls')  

def search_files(search_term, database_folder, max_results=10):
    results = []
    results_found = 0
    for root, _, files in os.walk(database_folder):
        if results_found >= max_results:
            break
        for file in files:
            if file.endswith(('.txt', '.csv', '.sql', '.json')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', errors='ignore') as f:
                    lines = f.readlines()
                    for index, line in enumerate(lines):
                        if results_found >= max_results:
                            break
                        if search_term in line:
                            result_str = f'{line.strip()}'
                            results.append(result_str)
                            results_found += 1
    return results

def main():
    database_folder = r"C:\Users\Desktop\Data_Searcher\Databases"

    text = fade.greenblue("""   
       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                             ███    ███                                          
    """)
    print(text)

    while True:
        term = input(fade.greenblue("Entre un mot clé à chercher dans tes DB ou appuyez sur q pour quitter => ")).strip()

        if term.lower() == 'q':
            os.system('cls') 
            break

        results = search_files(term, database_folder)

        if results:
            print(Colorate.Horizontal(Colors.blue_to_red, "Résultats trouvés :"))
            for result in results:
                print(result)
        else:
            print(Colorate.Horizontal(Colors.blue_to_red, "Aucun résultat n'a été trouvé dans les DB"))

if __name__ == "__main__":
    main()
