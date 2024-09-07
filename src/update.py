import os
import shutil
from git import Repo
import platform
import stat

# URL du dépôt GitHub
repo_url = "https://github.com/SearchX01/SearchXTools/"
# Dossier cible où se trouvent les fichiers .py à remplacer
destination_src = "src"

def clear_console():
    # Effacer la console selon le système d'exploitation
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def on_rm_error(func, path, exc_info):
    # Gestion des erreurs de suppression dues aux permissions
    os.chmod(path, stat.S_IWRITE)  # Changer les permissions pour permettre la suppression
    os.remove(path)

def update_python_files(repo_url, destination_src):
    # Créer un répertoire temporaire pour le clonage
    temp_dir = os.path.join(os.getcwd(), "temp_clone")
    
    # Supprimer le dossier temporaire s'il existe déjà
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, onerror=on_rm_error)

    try:
        # Cloner le dépôt dans le répertoire temporaire
        print("Clonage du dépôt...")
        repo = Repo.clone_from(repo_url, temp_dir)
        print("Dépôt cloné avec succès.")

        # Chemin du dossier src du dépôt cloné
        repo_src_dir = os.path.join(temp_dir, "src")

        # Vérifiez si le dossier src existe dans le dépôt cloné
        if os.path.exists(repo_src_dir):
            # Parcourir et remplacer uniquement les fichiers .py dans le dossier src
            for item in os.listdir(repo_src_dir):
                source_path = os.path.join(repo_src_dir, item)
                destination_path = os.path.join(destination_src, item)
                
                # Remplacer uniquement les fichiers .py
                if os.path.isfile(source_path) and item.endswith(".py"):
                    shutil.copy2(source_path, destination_path)
                    print(f"Fichier {item} mis à jour.")
        else:
            print("Le dossier 'src' n'existe pas dans le dépôt cloné.")
    
    except Exception as e:
        print(f"Erreur lors du clonage ou de la copie des fichiers : {e}")
    
    finally:
        # Fermer le repo pour libérer les ressources
        repo.close()
        
        # Tenter de supprimer le répertoire temporaire
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, onerror=on_rm_error)
        print("Mise à jour terminée et dossier temporaire supprimé.")

# Appel de la fonction pour mettre à jour les fichiers Python dans src
update_python_files(repo_url, destination_src)

# Effacer la console après le clonage et la mise à jour
clear_console()

# Terminer le programme proprement
