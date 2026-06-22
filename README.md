# application_desktop_python
Création d'une application desktop avec l'utilisation du module Python Tkinter. L'application stocke les données téléchargées depuis Internet dans la base de données et afficher des résumés des données téléchargées et leur représentation graphique.


## Structure du projet 

project/
│── app.py                # Point d'entrée Tkinter
│── database.py           # Gestion SQLite
│── fetcher.py            # Téléchargement JSON
│── ui/
│     ├── main_window.py  # Fenêtre principale
│     ├── menu_bar.py     # Menu
│     └── charts.py       # Graphiques matplotlib
│── assets/               # Icônes, thèmes, etc.
│── data.db               # Base SQLite
