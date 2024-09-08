import os
import shutil
from git import Repo
import platform
import stat
import subprocess

repo_url = "https://github.com/SearchX01/SearchXTools/"
destination_src = "src"
destination_main = "."
requirements_file = os.path.join(destination_main, "requirements.txt")

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.remove(path)

def install_git_if_missing():
    try:
        subprocess.run(["git", "--version"], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        if platform.system() == "Windows":
            print("Git n'est pas installé. Téléchargez-le ici : https://git-scm.com/downloads")
        else:
            print("Git n'est pas installé. Installation via le gestionnaire de paquets.")
            try:
                subprocess.run(["sudo", "apt-get", "install", "git", "-y"], check=True)
            except subprocess.CalledProcessError:
                print("Erreur lors de l'installation de Git. Veuillez installer Git manuellement.")

def update_files(repo_url, destination_src, destination_main):
    temp_dir = os.path.join(os.getcwd(), "temp_clone")
    
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, onerror=on_rm_error)

    try:
        print("Clonage du dépôt...")
        repo = Repo.clone_from(repo_url, temp_dir)
        print("Dépôt cloné avec succès.")

        repo_src_dir = os.path.join(temp_dir, "src")
        repo_main_path = os.path.join(temp_dir, "main.py")
        repo_requirements_path = os.path.join(temp_dir, "requirements.txt")

        if os.path.exists(repo_src_dir):
            for item in os.listdir(repo_src_dir):
                source_path = os.path.join(repo_src_dir, item)
                destination_path = os.path.join(destination_src, item)
                
                if os.path.isfile(source_path) and (item.endswith(".py") or item.endswith(".txt")):
                    shutil.copy2(source_path, destination_path)
                    print(f"Fichier {item} mis à jour.")
                elif os.path.isdir(source_path):
                    if os.path.exists(destination_path):
                        shutil.rmtree(destination_path, onerror=on_rm_error)
                    shutil.copytree(source_path, destination_path)
                    print(f"Dossier {item} mis à jour.")
        else:
            print("Le dossier 'src' n'existe pas dans le dépôt cloné.")

        if os.path.exists(repo_main_path):
            shutil.copy2(repo_main_path, destination_main)
            print("Fichier main.py mis à jour.")
        else:
            print("Le fichier main.py n'existe pas dans le dépôt cloné.")

        if os.path.exists(repo_requirements_path):
            shutil.copy2(repo_requirements_path, requirements_file)
            print("Le fichier requirements.txt a été remplacé avec succès.")
        else:
            print("Le fichier requirements.txt n'existe pas dans le dépôt cloné.")
    
    except Exception as e:
        print(f"Erreur lors du clonage ou de la copie des fichiers : {e}")
    
    finally:
        repo.close()
        
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, onerror=on_rm_error)
        print("Mise à jour terminée et dossier temporaire supprimé.")

install_git_if_missing()
update_files(repo_url, destination_src, destination_main)
clear_console()
