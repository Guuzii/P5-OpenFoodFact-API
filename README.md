# P5-OpenFoodFact-API

Small Programm that use openfoodfact.org API to get substittute product to a selection.
This programm has been developped for a python course.

## Requirements

    - Python 3.7
    - Pip
    - Mysql

## Installation

Clone project.
Open Console and place yourself in the project directory.
Run :
    commande installation environnement (pipfile.lock)

Configure access to your mysql database in the config.py file by changing host, user and password (lines 4, 5, 6)

## Usage

Place yourself in the programm directory and run :

'''console
    python main.py
'''

Select an options in the different menus by typing the number corresponding to your choice:
'''
    Menu

    1 - Réinitialiser la bdd
    2 - Nouvelle recherche
    3 - Voir mes produits enregistrés
    4 - Quitter le programme :
'''

## Modify categories

You can add or delete categories available in the menu and the database by modifying the product_categories_fr dictionnary in config.py file.
Be sure to reset database once you have added or deleted some categories.

'''
    product_categories_fr = {
        "plant-based-foods": "Fruits, Légumes, Plantes",
        "cereals-and-potatoes": "Féculents",
        "meats": "Viandes",
        "fishes": "Poissons",
        "desserts": "Desserts",
        "beverages": "Boissons"
    }
'''
