# main.py
import curses
from views.curses_ui import CursesUI

def main(stdscr):  # Ajoutez l'argument stdscr ici
    ui = CursesUI(stdscr)  # Passez stdscr à l'initialisation de CursesUI
    ui.main_loop()
    ui.close()

if __name__ == "__main__":
    curses.wrapper(main)
