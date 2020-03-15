import csv

from config.config import Config
import mysql.connector


class SQLClient:

    def __init__(self, config: Config):
        self.select_stacks_query = "SELECT * FROM stacks"
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

    def fetch_all_stacks(self):
        if self.mydb is None:
            self.setup()
        cursor = self.mydb.cursor()
        cursor.execute(self.select_stacks_query)
        records = cursor.fetchall()
        self.mydb.commit()
        cursor.close()
        self.mydb.close()
        return records

    def insert_into_stacks(self, name, image, build, port):
        if self.mydb is None:
            self.setup()
        cursor = self.mydb.cursor()
        try:
            query = 'INSERT INTO stacks VALUES("'+name+'", "'+image+'", "'+build+'", '+port+')'
            print(query)
            cursor.execute(query)
        except:
            return "Storing this stack failed"
        self.mydb.commit()
        cursor.close()
        self.mydb.close()
        return 200

