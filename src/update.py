import os
import shutil
from git import Repo

# URL du dépôt GitHub
repo_url = "https://github.com/SearchX01/SearchXTools/"
# Dossier cible où se trouvent les fichiers .py à remplacer
destination_src = "src"

def update_python_files(repo_url, destination_src):
    # Cloner le dépôt dans un répertoire temporaire en mémoire (sans le dossier visible)
    temp_dir = os.path.join(os.getcwd(), "temp_clone")
    
    # Supprimez le dossier temporaire s'il existe déjà
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

    try:
        # Clone le dépôt dans le répertoire temporaire
        print("Clonage du dépôt...")
        Repo.clone_from(repo_url, temp_dir)
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
    
    # Supprimer le dossier temporaire après la copie
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        print("Dossier temporaire supprimé, mise à jour terminée.")

# Appel de la fonction pour mettre à jour les fichiers Python dans src
update_python_files(repo_url, destination_src)
