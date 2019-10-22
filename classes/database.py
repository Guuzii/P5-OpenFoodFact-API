import config
import mysql.connector as mysql


class Database:

    def __init__(self, host: str, user: str, passwd: str):
        self.database = mysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=config.database_name
        )
        self.cursor = self.database.cursor()


    def execute_script_from_file(self, file_path: str):
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
        self.execute_script_from_file(config.path_to_creating_db_script)
        for category in config.product_categories:
            self.insert_data("Categories", (None, category))

    
    def use_db(self, db_name:str):
        self.cursor.execute("USE " + db_name)


    def get_data(self, table: str, column_to_get:str = None, column_to_search:str = None, entry:str = None):
        if column_to_get is not None and column_to_search is None:
            self.cursor.execute("SELECT " + column_to_get + " FROM " + table)
            response = self.cursor.fetchall()
        elif column_to_get is not None and column_to_get is not None:
            self.cursor.execute("SELECT " + column_to_get + " FROM " + table + " WHERE " + column_to_search + "=" + entry + ";")
            response = self.cursor.fetchall()
        else:
            self.cursor.execute("SELECT * FROM " + table + ";")
            response = self.cursor.fetchall()
            
        if len(response) > 0:
            return response
        else:
            return None            


    def insert_data(self, table: str, data: tuple):
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
        return self.cursor.lastrowid
        

    def commit_db(self):
        self.database.commit()


    def close_cursor(self):
        self.cursor.close()


    def close_db(self):
        self.database.close()

