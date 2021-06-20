# 2_Analyse_marche
Projet 2 - Analyse de marché

Le projet contient 3 fichiers python :
one_book.py : permet de récupérer les données d'un seul livre, dans un fichier *.csv qui sera nommé comme le livre, et de telecharger l'image de couverture 
  dans un dossier du nom de la category du livre.
one_category.py : permet de récupérer les données d'une categorie complete, dans un fichier *.csv contenant les données de toute la categorie. Les images 
  des couvertures des livres seront dans un dossier du nom de la categorie.
scrapper-Books.toScrap.py : permet de récupérer les données de tout les livres du site, chaque categorie sera stockée dans un fichier *.csv different, 
  et les images seront dans des dossiers par categorie.


1) Installation python :
-Allez sur https://www.python.org/downloads/ , et telecharger la derniere version de python, puis lancez le fichier telechargé pour l'installer.

2) Telecharger le code :
-Sur le repository github, cliquez sur le bouton "Code", puis "Download ZIP".
-Ensuite décompressez le fichier dans votre dossier de travail.

3) creation environement virtuel :
-Ouvrez un terminal, puis allez dans votre dossier de travail avec la commande cd.
-Dans le terminal, tapez : python3 -m venv env
Puis, pour activer l'environement virtuel,
Si vous etes sous mac, ou linx :
  -tapez : source env/bin/activate 
Si vous etes sous windows :
  -tapez env/Scripts/activate.bat

3) Installation des modules necessaires :
-dans le terminal, tapez : pip install -r requirements.txt

4) lancer le script :
-dans le terminal tapez : python3 nom_du_script_voulu.py
(Dans votre dossier de travail, vous verrez que les dossiers "csv_files" et "images" seront créés automatiquement.)

5) Pour fermer l'environement virtuel :
-dans le terminal, tapez : deactivate






