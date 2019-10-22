import requests
import json

from classes.database import Database


class Api:

    def __init__(self, db: Database):
        self.user_agent = "Pur Beurre - Projet étudiant - Python - Version 3.7.3"
        self.database = db

    def get_request(self, product_category: str):
        print("requete sur category :", product_category)
        request = requests.get("https://fr-en.openfoodfacts.org/cgi/search.pl?search_terms=" + product_category + "&page_size=100&action=process&json=1", headers={ "items": self.user_agent }) 
        response = json.loads(request.text)
        
        i = 0

        for product in response["products"]:

            product_shops = []
            product_categories = []
            product_url = product["url"]
            
            if product["product_name"] is not None and product["product_name"] is not "":
                product_name = product["product_name"]
            else:
                if product["product_name_fr"] is not None and product["product_name_fr"] is not "":
                    product_name = product["product_name_fr"]
                else:
                    continue

            
            if len(product["categories_tags"]) > 0:
                for category in product["categories_tags"]:                
                    new_category = category.replace("en:", "")
                    new_category = new_category.replace("fr:", "")
                    product_categories.append(new_category)

                if product_category in product_categories:
                    pass
                else:
                    continue                   
            else:
                continue

            
            if product["nutrition_grades_tags"][0].lower() not in ["a", "b", "c", "d", "e"]:
                product_nutri_grade = "e"
            else:
                product_nutri_grade = product["nutrition_grades_tags"][0]

            
            if len(product["stores_tags"]) > 0:
                for store in product["stores_tags"]:
                    new_store = store
                    product_shops.append(new_store)
            else:
                product_shops.append("N/A")


            self.database.insert_data("Products", (None, product_name, product_url, product_nutri_grade))

            product_id = self.database.get_last_row_id()


            for store in product_shops:
                shop_name = "'" + store + "'"
                store_id = self.database.get_data("Shops", "id_shop", "shop_name", shop_name)

                if store_id is None:
                    self.database.insert_data("Shops", (None,store))
                    store_id = self.database.get_last_row_id()
                else:
                    store_id = store_id[0][0]

                self.database.insert_data("TJ_Products_Shops", (product_id, store_id))

            
            for category in product_categories:
                category_name = "'" + category + "'"
                category_id = self.database.get_data("Categories", "id_category", "category_name", category_name)

                if category_id is not None:
                    category_id = category_id[0][0]
                    self.database.insert_data("TJ_products_categories", (product_id, category_id))
                    
            i += 1

            print("")
            print("Produit", i)
            print("product_id :", product_id)
            print("")

        print(i)
        