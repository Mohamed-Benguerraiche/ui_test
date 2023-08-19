# main.py
import curses
from views.curses_ui import CursesUI

def main(stdscr):  # Ajoutez l'argument stdscr ici
    # On défini le fichier config à utiliser
    config_path = "./config/app_config.json"
    ui = CursesUI(stdscr)  # Passez stdscr à l'initialisation de CursesUI
    ui.main_loop(config_path)
    ui.close()
    
if __name__ == "__main__":
    curses.wrapper(main)
