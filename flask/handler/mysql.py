from client.mysql import MysqlClient
from config.config import Config
from client.mysql import MysqlClient

from util.json_utils import JsonUtils


class MysqlHandler:

    def __init__(self, config: Config):
        self.table_name = config.mysql_table_name
        # self.column_names = config.mysql_column_names
        self.sql_client = MysqlClient(config)

    def select_all_from_stacks(self):
        return JsonUtils.array_to_json_array(self.sql_client.select_all(self.table_name))
