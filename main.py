from classes import database

mydb = database.Database("localhost", "root", "root")

mydb.execute_script_from_file("./sql_scripts/create_db_and_tables.sql")

mydb.commit_db()