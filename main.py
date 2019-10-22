import config

from classes import database
from classes import api


def main():

  run_loop = True
  mydb = database.Database("localhost", "root", "root")

  while run_loop:

    user_selection = input("Menu \n\n1=réinitialiser la bdd \n2=test : ")

    if user_selection == "1":      
      mydb.create_database()
      mydb.commit_db()
      open_food_fact = api.Api(mydb)

      for category in config.product_categories:
        open_food_fact.get_request(category)

      run_loop = False      
    elif user_selection == "2":
      print("test")
      mydb.get_data("TR_shops", "id_shop", "shop_name", "'carrefour'")
      
      run_loop = False
    else:
      print("Saisie invalide \n")
      


if __name__ == "__main__":
    main()