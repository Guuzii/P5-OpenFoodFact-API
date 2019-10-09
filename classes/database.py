import mysql.connector as mysql

class Database:

    def __init__(self, host: str, user: str, passwd: str):
        self.database = mysql.connect(
            host=host,
            user=user,
            passwd=passwd
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


    def commit_db(self):
        self.database.commit()

    def gat_data(self):
        return