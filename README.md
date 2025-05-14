 ===========================================
    Dépôt GitHub et modification sur WSL
============================================= 
<br><br>
## ⚠️ À tenir en compte :
        - Atteindre "✅" avant de commencer à travailler
        - Être dans un répertoire vide que vous decider d'en faire votre lieu de travail du projet
(Comment Faire ?) : Connectez vous à WSL sur votre PC, choisissez l'emplacement qui vous convient et créez un répertoire, "dna-project" par ex. et rentrez dans le nouveau répertoire créé. Vous y êtes !
<br><br>
# 1. Cloner le dépôt et naviguer dans le répertoire du projet
git clone https://github.com/votre_nom_utilisateur/nom_du_depot.git
cd nom_du_depot

Explication :
    - Sur votre WSL, dans un dossier que auriez nommé "dna-project" par ex., vous pouvez cloner notre dépôt gitHub
    - Vous obtiendrez ainsi : 
        - tous les fichiers .py se trouvant dans le dossier python, chacune contenant une classe
        - le fichier .gitignore
        - le fichier requirements.txt contenant toutes les déendances
        - le fichier main.py qui appelle les classes
<br>
# 2. Créer l'environnement virtuel Python
python3 -m venv env

Explication :
    - Cette commande va créer un dossier nommé "env" dans dna-project, à coté de "dna-model-python", le dépôt github
    - Il ne contient pas encore toutes les dépendances dont vous aurez besoin pour travailler durant le projet.
<br>
# 3. Activer l'environnement virtuel
source env/bin/activate
<br>
# 4. Installer les dépendances du projet
pip install -r dna-model-python/requirements.txt

Explication :
    - ✅ : À partir d'ici, vous pouvez travailler sur votre local, modifier comme vous voulez ce que vous voulez.

# (Optionnel) À la fin, si vous avez ajouté des dépendances, n'oubliez pas de les geler avec la commande suivante
pip freeze > requirements.txt
<br>
# 5. Gérer les modifications avec Git
git add .
git commit -m "Votre message de commit ici"
git push origin main

<br><br>
## ⚠️ : Next time you come again, just move to your dna-python-directory, open the terminal and write git pull to have the latest changes before you start !
[image](https://github.com/user-attachments/assets/efd3562d-fe76-40f0-8ea9-89cd4b9464fc)
working !
