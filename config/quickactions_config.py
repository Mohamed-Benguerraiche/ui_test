# Création d'une classe et de méthodes pour les raccourcis d'actions rapides

import json

class QuickActionsConfig:


# Si config_path = app_config
## Chaque clé "Shortcut" renvoi à la clé "ConfigPath" correspondant au module concerné


# Si config_path = antivirus_config
## Chaque clé "Shortcut" renvoi à la clé "Name" correspondant à la fonction concernée
### Renvoyer les paramètres à la fonction soit un path (le chemin du fichier à envoyer au service VirusTotal) de la clé "UserInput" et une clé API de la clé "ApiKey"

