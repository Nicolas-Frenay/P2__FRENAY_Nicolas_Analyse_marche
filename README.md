# 2_Analyse_marche
# Projet 2 - Analyse de marché

Le projet contient 3 fichiers python :
- one_book_V2.py : permet de récupérer les données d'un seul livre, dans un fichier csv qui sera nommé comme le livre, 
  et de télécharger l'image de couverture 
  dans un dossier du nom de la catégorie du livre.
- one_category_V2.py : permet de récupérer les données d'une catégorie complete, dans un fichier csv contenant les 
  données de toute la catégorie. Les images 
  des couvertures des livres seront dans un dossier du nom de la catégorie.
- scrapper-Books.toScrap_V2.py : permet de récupérer les données de tout les livres du site, chaque catégorie sera 
  stockée dans un fichier csv different, 
  et les images seront dans des dossiers nommés par catégorie.


## Instructions :


1) Installation python :
- Allez sur [https://www.python.org/downloads/](url) , et télécharger la dernière version de python, puis lancez le fichier 
  téléchargé pour l'installer.

2) Télécharger le code :
- Sur le repository github, cliquez sur le bouton "Code", puis "Download ZIP".
- Ensuite décompressez le fichier dans votre dossier de travail.

3) creation environnement virtuel :
- Ouvrez un terminal, puis allez dans votre dossier de travail avec la commande cd.
- Dans le terminal, tapez : ``` python3 -m venv env ```

4) Activer l'environnement virtuel :
  - Si vous êtes sous mac, ou linux :
    - tapez : ```source env/bin/activate ```
  - Si vous êtes sous windows :
    - tapez ```env/Scripts/activate.bat```
  (Les scripts n'utilisent pas de modules externes, il n'y a donc rien à installer en plus)  

5) lancer le script :
- dans le terminal tapez : ```python3 <nom_du_script_voulu.py>```

  (Dans votre dossier de travail, vous verrez que les dossiers "csv_files" et "images" seront créés automatiquement.)

6) Pour fermer l'environnement virtuel :
- Dans le terminal, tapez : ```deactivate ```










