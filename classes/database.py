import random

import config
import mysql.connector as mysql


class Database:
    """
        Database Object
        
        Initialize a Database object and connect to database specified in config.
        Handle the database requests.

        Parameters :
            - host (str): the host for mysql connection
            - user (str): the username for mysql connection
            - passwd (str): the password for specified username
        
        Attributes:
            - database: the database reference
            - cursor: the cursor reference
    """

    def __init__(self, host: str, user: str, passwd: str):
        self.database = mysql.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.cursor = self.database.cursor()


    def available_databases(self):
        """
            Get all available databases and return it as a list of string

            Returns:
                - list (str): list of all available databases
                - None: if no databases available
        """
        database_available = []

        self.cursor.execute("SHOW databases;")
        response = self.cursor.fetchall()

        for db in response:
            database_available.append(db[0])

        if len(database_available) > 0:
            return database_available
        else:
            return None

        
    def execute_script_from_file(self, file_path: str):
        """
            Execute SQL script specified in argument

            Parameters :
                - file_path (str): path to the sql script file
        """
        file = open(file_path, 'r')
        sql_file = file.read()
        file.close()
        sql_commands = sql_file.split(';')

        for command in sql_commands:
            try:
                if command.strip() != '':
                    # print(command)
                    self.cursor.execute(command)
            except IOError as msg:
                print("command skipped", msg)


    def create_database(self):
        """
            Create database and insert categories in Categories table
        """
        self.execute_script_from_file(config.path_to_creating_db_script)
        for category in config.product_categories_fr:
            self.insert_data("Categories", (None, category))

    
    def get_data(self, table: str, column_to_get:str = None, column_to_search:str = None, entry:str = None):
        '''
            Get data in database depending on passed arguments

            Parameters:
                - table (str): the table to get data from
                - column_to_get (str): the column to get in the table (if specified)
                - column_to_search (str): the column on wich the WHERE condition is apply
                - entry (str): the value to search in column_to_search

            Returns:
                - List (tuple): all datas for specified arguments
        '''
        if column_to_get is not None and column_to_search is None:
            self.cursor.execute(
                "SELECT " + column_to_get +
                " FROM " + table + ";"
            )
            response = self.cursor.fetchall()
        elif column_to_get is not None and column_to_get is not None:
            query_params = (entry,)
            self.cursor.execute(
                "SELECT " + column_to_get + 
                " FROM " + table + 
                " WHERE " + column_to_search + " = %s;", query_params
            )
            response = self.cursor.fetchall()
        else:
            self.cursor.execute(
                "SELECT * "
                "FROM " + table + ";"
            )
            response = self.cursor.fetchall()
            
        if len(response) > 0:
            if len(response) <= 1:
                return response[0]
            else:
                return response
        else:
            return None            


    def get_products_in_category(self, category: str):
        '''
            Get products for specified category

            Parameters:
                - category (str): the name of the category of products to get

            Returns:
                - List (tuple): all products for specified category
        '''
        self.cursor.execute(
            "SELECT p.* "
            "FROM Products AS p "
            "INNER JOIN TJ_Products_Categories AS pc "
                "ON p.id_product = pc.id_product "
            "INNER JOIN Categories AS c "
                "ON c.id_category = pc.id_category "
            "WHERE c.category_name = '" + category + "';"
        )
        response = self.cursor.fetchall()
        
        if len(response) > 0:
            return response
        else:
            return None


    def get_categories_for_product(self, product_id: int):
        '''
            Get categories for specified product

            Parameters:
                - product_id (int): the id of the product to get categories from

            Returns:
                - List (str): all categories for specified product id
        '''
        categories_list = []
        id = (product_id,)

        self.cursor.execute(
            "SELECT c.category_name "
            "FROM Categories c "
            "INNER JOIN TJ_Products_Categories pc "
                "ON c.id_category = pc.id_category "
            "INNER JOIN Products p "
                "ON p.id_product = pc.id_product "
            "WHERE p.id_product = %s;", id
        )

        response = self.cursor.fetchall()

        if len(response) > 0:
            for category in response:
                categories_list.append(category[0])

            return categories_list
        else:
            return None


    def get_stores_for_product(self, product_id: int):
        '''
            Get stores for specified product

            Parameters:
                - product_id (int): the id of the product to get stores from

            Returns:
                - List (str): all stores for specified product id
        '''
        stores_list = []
        id = (product_id,)

        self.cursor.execute(
            "SELECT s.shop_name "
            "FROM Shops s "
            "INNER JOIN TJ_Products_Shops ps "
                "ON s.id_shop = ps.id_shop "
            "INNER JOIN Products p "
                "ON p.id_product = ps.id_product "
            "WHERE p.id_product = %s;", id
        )

        response = self.cursor.fetchall()

        if len(response) > 0:
            for store in response:
                stores_list.append(store[0])

            return stores_list
        else:
            return None


    def get_user_favorites_products(self, user_id: int):
        '''
            Get products saved in database for specified user

            Parameters:
                - user_id (int): the id of the user to get products for

            Returns:
                - List (tuple): all products saved by user (none if no products saved yet)
        '''
        id = (user_id,)

        self.cursor.execute(
            "SELECT p.* "
            "FROM Products AS p "
            "INNER JOIN TJ_Products_Users AS pu "
                "ON p.id_product = pu.id_product "
            "INNER JOIN Users AS u "
                "ON u.id_user = pu.id_user "
            "WHERE u.id_user = %s;", id
        )

        response = self.cursor.fetchall()

        if len(response) > 0:
            return response
        else:
            return None

    
    def insert_data(self, table: str, data: tuple):
        '''
            Save data passed in argument to specified table in datadase

            Parameters:
                - table (str): the name of the table in wich the data should be inserted
                - data (tuple): the datas to insert. Refer to table description for datas order in tuple
        '''
        insert_request = None

        if (table.lower() == "categories"):
            insert_request = (
                "INSERT INTO Categories "
                "(id_category, category_name) "
                "VALUES (%s, %s)"
            )

        if (table.lower() == "shops"):
            insert_request = (
                "INSERT INTO Shops "
                "(id_shop, shop_name) "
                "VALUES (%s, %s)"
            )

        if (table.lower() == "users"):
            insert_request = (
                "INSERT INTO Users "
                "(id_user, user_first_name, user_last_name) "
                "VALUES (%s, %s, %s)"
            )

        if (table.lower() == "products"):
            insert_request = (
                "INSERT INTO Products "
                "(id_product, product_name, product_url, nutrition_score) "
                "VALUES (%s, %s, %s, %s)"
            )

        if (table.lower() == "tj_products_categories"):
            insert_request = (
                "INSERT INTO TJ_Products_Categories "
                "(id_product, id_category) "
                "VALUES (%s, %s)"
            )
        
        if (table.lower() == "tj_products_shops"):
            insert_request = (
                "INSERT INTO TJ_Products_Shops "
                "(id_product, id_shop) "
                "VALUES (%s, %s)"
            )

        if (table.lower() == "tj_products_users"):
            insert_request = (
                "INSERT INTO TJ_Products_Users "
                "(id_product, id_user) "
                "VALUES (%s, %s)"
            )

        if (insert_request != None):
            self.cursor.execute(insert_request, data)
        
        self.commit_db()

    
    def get_last_row_id(self):
        '''
            Return the id of the last row inserted at cursor position
        '''
        return self.cursor.lastrowid
        

    def commit_db(self):
        '''
            Commit changes to the database
        '''
        self.database.commit()

    def use_db(self, db_name: str):
        self.cursor.execute("USE " + db_name + ";")