from config.config import Config
import mysql.connector


class MysqlClient:

    def __init__(self, config: Config):
        self.select_all_query = "SELECT * FROM"
        self.user = config.mysql_username
        self.password = config.mysql_password
        self.port = config.mysql_port
        self.host = config.mysql_host
        self.database = config.mysql_db_name
        self.mydb = None

    def setup(self):
        db_config = {
            'user': self.user,
            'password': self.password,
            'host': self.host,
            'port': self.port,
            'database': self.database
        }
        self.mydb = mysql.connector.connect(**db_config)

    def select_all(self, table_name):
        self.setup()
        query = self.select_all_query + ' ' + table_name + ' ;'
        cursor = self.mydb.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        self.mydb.commit()
        cursor.close()
        self.mydb.close()
        return records

    def insert_into_stacks(self, table_name, column_values):
        self.setup()
        cursor = self.mydb.cursor()
        query = 'INSERT INTO ' + table_name + ' VALUES( '
        for column_value in column_values:
            if isinstance(column_value, str):
                query = query + '"' + column_value + '"' + ', '
            else:
                query = query + column_value + ', '
        query = query[:-2] + ');'
        try:
            print(query)
            cursor.execute(query)
        except:
            return "Storing this stack failed"
        self.mydb.commit()
        cursor.close()
        self.mydb.close()
        return 200
