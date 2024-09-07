import os
import shutil
from git import Repo
import platform
import stat


repo_url = "https://github.com/SearchX01/SearchXTools/"

destination_src = "src"

def clear_console():

    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def on_rm_error(func, path, exc_info):

    os.chmod(path, stat.S_IWRITE)  
    os.remove(path)

def update_python_files(repo_url, destination_src):
   
    temp_dir = os.path.join(os.getcwd(), "temp_clone")
    
 
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, onerror=on_rm_error)

    try:

        print("Clonage du dépôt...")
        repo = Repo.clone_from(repo_url, temp_dir)
        print("Dépôt cloné avec succès.")

 
        repo_src_dir = os.path.join(temp_dir, "src")

     
        if os.path.exists(repo_src_dir):
    
            for item in os.listdir(repo_src_dir):
                source_path = os.path.join(repo_src_dir, item)
                destination_path = os.path.join(destination_src, item)
                
                
                if os.path.isfile(source_path) and item.endswith(".py"):
                    shutil.copy2(source_path, destination_path)
                    print(f"Fichier {item} mis à jour.")
        else:
            print("Le dossier 'src' n'existe pas dans le dépôt cloné.")
    
    except Exception as e:
        print(f"Erreur lors du clonage ou de la copie des fichiers : {e}")
    
    finally:

        repo.close()
        
       
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, onerror=on_rm_error)
        print("Mise à jour terminée et dossier temporaire supprimé.")


update_python_files(repo_url, destination_src)


clear_console()


