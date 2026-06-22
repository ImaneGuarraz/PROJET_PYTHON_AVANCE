# application_desktop_python
Création d'une application desktop avec l'utilisation du module Python Tkinter. L'application stocke les données téléchargées depuis Internet dans la base de données et afficher des résumés des données téléchargées et leur représentation graphique.


## Structure du projet 

Python_App_Desktop/
│
├── main.py                # Fenêtre Tkinter + menus + boutons
├── database.py            # Connexion SQLite + CRUD
├── api.py                 # Téléchargement JSON depuis Internet
├── charts.py              # Graphiques matplotlib
├── config.py              # Options (couleurs, polices…)
└── app_desktop_python.db  # Base SQLite (créée automatiquement)


## Les outils 

- MySQL
- TablePlus
- Visual Studio Code


## Les Vue d’ensemble du projet

Ton appli va faire :

- Télécharger des données JSON depuis Internet
- Les stocker dans une base SQLite (app_desktop_python.db)
- Afficher des résumés (agrégations SQL)
- Afficher des graphiques dans une fenêtre Tkinter
- Proposer un menu pour :
  - effacer la base
  - télécharger les données
  -  changer des options (couleurs, polices…)
