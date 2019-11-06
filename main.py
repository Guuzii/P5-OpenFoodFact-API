import random

import config

from classes import database
from classes import api


def convert_grade_to_number(grade: str):
  grade_formated = grade.lower()

  if grade_formated == "a":
    return 5
  elif grade_formated == "b":
    return 4
  elif grade_formated == "c":
    return 3
  elif grade_formated == "d":
    return 2
  else:
    return 1


def main():
  
  mydb = database.Database(config.db_config["host"], config.db_config["user"], config.db_config["password"])

  run_main = True
  while run_main:
    
    print("-------------------------------------------------------------------------------------")
    user_selection = input("Menu \n\n1=réinitialiser la bdd \n2=Nouvelle recherche \n3=Voir mes produits favoris \n4=Quitter \n5=Test : ")
    
# ----- CHOIX 1 -------------------------------------------------------------------------------------------------------------------
    if user_selection == "1":      
      mydb.create_database()
      mydb.commit_db()
      open_food_fact = api.Api(mydb)

      for category in config.product_categories:
        open_food_fact.get_request(category)

# ----- CHOIX 2 -------------------------------------------------------------------------------------------------------------------
    elif user_selection == "2":
      categories = mydb.get_data("Categories")
      
      run_research = True
      while run_research:
        print("")
        print("-------------------------------------------------------------------------------------")
        print("Catégories disponibles : ")
        print("")
        
        for category in categories:
          print(str(category[0]) + " - " + category[1])
        
        print("")
        selected_category = input("Sélectionnez une catégorie en saisissant son nombre associé : ")

        if selected_category not in ("1", "2", "3", "4", "5", "6"):
          print("Saisie invalide \n")
          continue

        if selected_category == "1":
          category_name = categories[int(selected_category) - 1][1]
        elif selected_category == "2":
          category_name = categories[int(selected_category) - 1][1]
        elif selected_category == "3":
          category_name = categories[int(selected_category) - 1][1]
        elif selected_category == "4":
          category_name = categories[int(selected_category) - 1][1]
        elif selected_category == "5":
          category_name = categories[int(selected_category) - 1][1]
        elif selected_category == "6":
          category_name = categories[int(selected_category) - 1][1]

        products = mydb.get_products_in_category(category_name)
        products_set = random.sample(set(products), config.product_to_display_for_selection)
        products_id = []

        run_product_selection = True
        while run_product_selection:
          print("")
          print("-------------------------------------------------------------------------------------")
          print("Produits disponibles à la sélection pour la catégorie '" + category_name + "' :")
          print("")
          
          for product in products_set:
            products_id.append(str(product[0]))
            print(str(product[0]) + " - " + product[1])

          print("")
          id_selected_product = input("Sélectionnez un produit en saisissant son nombre associé : ")
          
          if id_selected_product not in products_id:
            print("Saisie invalide \n")
            continue
          
          product_selection = mydb.get_data("Products", "*", "id_product", int(id_selected_product))
          product_selection_categories = mydb.get_categories_for_product(int(id_selected_product))
          product_selection_stores = mydb.get_stores_for_product(int(id_selected_product))
          
          print("")
          print("-------------------------------------------------------------------------------------")
          print("Produit Sélectionné :")
          print("")
          print("Id :", product_selection[0])
          print("Nom :", product_selection[1])
          print("Url :", product_selection[2])
          print("NutriScore :", product_selection[3])
          print("Categorie(s) :", product_selection_categories)
          print("Magasin(s) :", product_selection_stores)

          substitute_products = []
          substitute_products_id = []

          for product in products:
            if product_selection[3] == "a":
              if product[3] == "a":
                substitute_products.append(product)
            else:
              if convert_grade_to_number(product[3]) > convert_grade_to_number(product_selection[3]):
                substitute_products.append(product)

          if len(substitute_products) >= 3:
            random_substitute_products = random.sample(set(substitute_products) - {product_selection}, 3)
          else:
            random_substitute_products = substitute_products

          for product in random_substitute_products:
            substitute_products_id.append(product[0])

          print("")
          print("-------------------------------------------------------------------------------------")
          print("Voici le(s) produit(s) de substitution proposé(s) :")

          for product in random_substitute_products:
            product_categories = mydb.get_categories_for_product(product[0])
            product_stores = mydb.get_stores_for_product(product[0])
            
            print("")
            print("Id :", product[0])
            print("Nom :", product[1])
            print("Url :", product[2])
            print("NutriScore :", product[3])
            print("Categorie(s) :", product_categories)
            print("Magasin(s) :", product_stores)

          print("")
          print("")

          run_user_save = True
          while run_user_save:
            saving = input("Voulez vous ajouter à vos favoris un des produits proposés (o/n)? ")

            if saving.lower() == "o":
              id_product_to_save = input("Saisissez l'id du produit que vous voulez ajouter à vos favoris : ")

              if int(id_product_to_save) not in substitute_products_id:
                print("Saisie invalide \n")
                continue
              
              mydb.insert_data("tj_products_users", (int(id_product_to_save), 1))

              print("Produits ajouté à vos favoris avec succés !")
              print("")
              print("")

              run_user_save = False
            elif saving.lower() == "n":
              run_user_save = False
            else:
              print("Saisie invalide \n")

          run_product_selection = False

        run_research = False

# ----- CHOIX 3 -------------------------------------------------------------------------------------------------------------------
    elif user_selection == "3":

      favorites_products = mydb.get_user_favorites_products(1)

      print("")
      print("-------------------------------------------------------------------------------------")
      print("Voici la liste de vos produits favoris :")

      for product in favorites_products:
        product_categories = mydb.get_categories_for_product(product[0])
        product_stores = mydb.get_stores_for_product(product[0])

        print("")
        print("Id :", product[0])
        print("Nom :", product[1])
        print("Url :", product[2])
        print("NutriScore :", product[3])
        print("Categorie(s) :", product_categories)
        print("Magasin(s) :", product_stores)

# ----- CHOIX 4 -------------------------------------------------------------------------------------------------------------------
    elif user_selection == "4":
      run_main = False

# ----- CHOIX 5 -------------------------------------------------------------------------------------------------------------------
    elif user_selection == "5":
      pass

    else:
      print("Saisie invalide \n")


if __name__ == "__main__":
    main()