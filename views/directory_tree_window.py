# directory_tree_window.py

import curses
from controllers.__main__ import *

class DirectoryTreeWindow:
    def __init__(self, window):
        self.window = window

    def draw(self):
        # Dessiner les bordures
        self.window.border(0)

         # On défini le fichier config à utiliser
        config_path = "./config/app_config.json"

        # Afficher le texte de la variable 'text' dans la fenêtre de sortie
        directory_tree = DirectoryTreeWindowController.get_directory_tree(config_path, 0)
        self.window.addstr(1, 1, directory_tree, curses.color_pair(1))
        # Dessiner l'arborescence des dossiers ici
        self.window.refresh()
