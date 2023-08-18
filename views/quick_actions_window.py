# quick_actions_window.py

import curses

class QuickActionsWindow:
    def __init__(self, window):
        self.window = window

    def draw(self):
        text = "Menu des actions rapides"
        # Dessiner les bordures
        self.window.border(0)
        # Afficher le texte de la variable 'text' dans la fenêtre de sortie
        self.window.addstr(1, 1, text, curses.color_pair(1))
        # Dessiner le menu des actions rapides ici
        self.window.refresh()
