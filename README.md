====================================================================================================
Guide de modification d'un Environnement Python sur WSL-Ubuntu dans un Dépôt GitHub Commun
====================================================================================================
# 1. Cloner le dépôt et naviguer dans le répertoire du projet
git clone https://github.com/votre_nom_utilisateur/nom_du_depot.git
cd nom_du_depot

# 2. Créer l'environnement virtuel Python
python3 -m venv env

# 3. Activer l'environnement virtuel
source env/bin/activate

# 4. Installer les dépendances du projet
pip install -r dna-model-python/requirements.txt

# (Optionnel) Mettre à jour le fichier requirements.txt après modification des dépendances
pip freeze > requirements.txt

# 5. Gérer les modifications avec Git
git add .
git commit -m "Votre message de commit ici"
git push origin main

# Pour récupérer les dernières modifications du dépôt distant
git pull origin main




====================================================================================================
Guide d'Initialisation d'un Environnement Python sur WSL-Ubuntu dans un Dépôt GitHub Commun
====================================================================================================

----------------------------
Étape 1 : Cloner le dépôt GitHub
----------------------------

Commande :
    git clone https://github.com/ton_nom_utilisateur/nom_du_depot.git

Explication :
    - Cette commande va récupérer le dépôt distant depuis GitHub et créer une copie locale sur ton WSL.
    - Tu obtiendras ainsi tous les fichiers et l'historique des commits du projet.
    
À ce stade :
    - Ton dépôt est présent sur ta machine. 
    - Tu peux parcourir les fichiers et préparer tes modifications localement.
    
Ce que tu ne peux pas faire :
    - Modifier directement le dépôt distant sans passer par un commit et un push.

----------------------------
Étape 2 : Se positionner dans le dossier du dépôt
----------------------------

Commande :
    cd nom_du_depot

Explication :
    - Cette commande change ton répertoire de travail pour celui du projet cloné.
    
À ce stade :
    - Tu es dans le répertoire de ton projet et prêt(e) à y ajouter/modifier des fichiers.

----------------------------
Étape 3 : Configurer le fichier .gitignore (Optionnel mais recommandé)
----------------------------

Commande :
    echo "env/" >> .gitignore

Explication :
    - Cette commande ajoute la ligne "env/" dans le fichier .gitignore.
    - Elle permet à Git d’ignorer le dossier de ton environnement virtuel pour ne pas le pousser sur GitHub.
    
À ce stade :
    - Ton dépôt est configuré pour éviter de versionner les fichiers générés dans l'environnement virtuel.
    - Tu peux continuer à modifier d'autres fichiers sans que Git ne suive ceux du dossier « env ».

----------------------------
Étape 4 : Créer un Environnement Virtuel Python
----------------------------

Commande :
    python3 -m venv env

Explication :
    - Cette commande utilise le module venv de Python et crée un environnement isolé nommé "env".
    - Cet environnement contient une installation locale de Python et pip, distincte de celle du système.
    
À ce stade :
    - Un dossier "env" apparaît dans ton projet, contenant l'environnement isolé.
    
Ce que tu peux faire :
    - Installer et gérer des packages Python indépendamment du système global.
    
Ce que tu ne peux pas faire :
    - Modifier directement les fichiers de l'environnement ; il faut passer par l’installation de packages.

----------------------------
Étape 5 : Activer l’Environnement Virtuel
----------------------------

Commande :
    source env/bin/activate

Explication :
    - Cette commande active ton environnement virtuel.
    - Tu verras normalement le nom de l'environnement (exemple : "(env)") dans ton invite de commande.
    
À ce stade :
    - Toute commande Python ou pip sera exécutée dans l'environnement virtuel.
    
Ce que tu peux faire :
    - Installer des packages et exécuter ton code sans interférer avec la configuration globale de ton système.
    
Ce que tu ne peux pas faire :
    - Utiliser la version de Python globale tant que tu restes dans l'environnement virtuel.
    - Pour revenir à la configuration globale, il faut taper "deactivate".

----------------------------
Étape 6 : Installer les Dépendances et Créer un Fichier requirements.txt
----------------------------

Commande pour installer des dépendances (exemple) :
    pip install numpy flask

Explication :
    - Cette commande installe les packages "numpy" et "flask" dans ton environnement virtuel.
    - Adapte cette commande avec les dépendances dont tu as besoin pour ton projet.
    
Commande pour générer le fichier des dépendances :
    pip freeze > requirements.txt

Explication :
    - "pip freeze" liste l'ensemble des packages installés dans ton environnement.
    - La redirection ">" enregistre cette liste dans le fichier requirements.txt, ce qui permettra à tes collègues d'installer exactement les mêmes versions.
    
À ce stade :
    - Ton environnement Python est configuré avec les packages requis.
    - Le fichier requirements.txt documente tous les packages installés.

----------------------------
Étape 7 : Ajouter et Commiter Tes Modifications dans Git
----------------------------

Commande pour ajouter tous les fichiers modifiés :
    git add .

Explication :
    - Cette commande prépare tous les fichiers modifiés (y compris .gitignore et requirements.txt) pour être enregistrés dans un commit.
    - Le dossier "env/" est ignoré grâce au .gitignore.
    
Commande pour créer un commit :
    git commit -m "Initialisation de l'environnement Python et ajout de requirements.txt"

Explication :
    - Cette commande enregistre un snapshot de l'état de ton projet avec un message explicatif.
    
À ce stade :
    - Tes modifications sont sauvegardées localement dans l’historique Git.
    
Ce que tu ne peux plus faire :
    - Changer l'état du projet sur GitHub sans repasser par un nouveau commit et un push.

----------------------------
Étape 8 : Pousser Tes Changements Vers le Dépôt Distant
----------------------------

Commande :
    git push origin main

Explication :
    - Cette commande envoie tes commits locaux vers le dépôt distant sur GitHub.
    - Remplace "main" par le nom de ta branche si celle-ci diffère (ex. "master").
    
À ce stade :
    - Le dépôt GitHub est mis à jour avec tes modifications.
    - Tes collaboratrices peuvent maintenant récupérer ces changements en clonant ou en faisant un pull.
    
Ce que tu peux faire ensuite :
    - Continuer à développer sur ton projet et répéter ces étapes pour chaque nouvelle modification.

====================================================================================================
Rappel des Commandes en Un Coup d'Œil :
====================================================================================================

1. Cloner le dépôt :
       git clone https://github.com/ton_nom_utilisateur/nom_du_depot.git

2. Se déplacer dans le dossier du dépôt :
       cd nom_du_depot

3. Configurer .gitignore pour ignorer l'environnement :
       echo "env/" >> .gitignore

4. Créer l'environnement virtuel :
       python3 -m venv env

5. Activer l'environnement virtuel :
       source env/bin/activate

6. Installer les dépendances et créer requirements.txt :
       pip install numpy flask
       pip freeze > requirements.txt

7. Ajouter et commiter les modifications :
       git add .
       git commit -m "Initialisation de l'environnement Python et ajout de requirements.txt"

8. Pousser vers GitHub :
       git push origin main

====================================================================================================
