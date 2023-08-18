import json
from typing import Callable, Dict

# Classe pour enregistrer les actions rapides
class MethodRegistry:
    jump_table: Dict[str, Callable] = {}

    # Méthode statique pour enregistrer les actions rapides
    @classmethod
    def register(cls, shortcut: str, function: str) -> Callable:
        def decorator(quick_action: Callable) -> Callable:
            cls.jump_table[shortcut] = quick_action
            quick_action.function_name = function
            return quick_action
        return decorator

    # Méthode statique pour obtenir la jump_table liée
    @classmethod
    def get_bound_jump_table(cls) -> Dict[str, Callable]:
        return {
            command: quick_action.__get__(None, cls)
            for command, quick_action in cls.jump_table.items()
        }

# Classe pour le contrôleur de fenêtre QuickActionsWindowController
class QuickActionsWindowController:
    class QuickActions(MethodRegistry):
        pass

    # Méthode statique pour ouvrir le fichier de configuration
    @staticmethod
    def open_config_file(config_path):
        with open(config_path) as json_file:
            config = json.load(json_file)
            return config       

    # Constructeur de la classe QuickActionsWindowController
    def __init__(self, config_path) -> None:
        self.config = self.open_config_file(config_path)
        self.quick_actions = self.QuickActions.get_bound_jump_table()

    # Enregistrement des actions rapides
        for action in self.config["Application"]["Modules"]["Actions"]:
            @QuickActionsWindowController.QuickActions.register(action["Shortcut"], action["Name"])
            def action_function(action=action):
                print(f"Shortcut: {action['Shortcut']}, Function: {action['Name']}")
              
            action_function()

# # Variable vers le fichier de configuration
# config_path = "../config/app_config.json"

# # Créer une instance du contrôleur de fenêtre QuickActionsWindowController
# QuickActionsWindowController(config_path)

