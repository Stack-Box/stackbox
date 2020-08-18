from client.dynamodb import DynamodbClient
from config.config import Config

class DynamoDBHandler:

    def __init__(self, aws_access_key_id, aws_secret_access_key, region):
        """
        Initializes the dynamodb client
        :param aws_access_key_id:
        :param aws_secret_access_key:
        :param region:
        """
        self.dynamodbClient = DynamodbClient(aws_access_key_id,aws_secret_access_key,region)

    def get_dynamodb_items(self,table):
        """
        Gets all the items from dynamodb given the table
        :param table:
        :return:
        """
        result = self.dynamodbClient.get_dynamodb_items(table)

    def put_dynamodb_item(self,table,data):
        """
        Puts an item into the dynaodb given the table and data
        :param table:
        :param data:
        :return:
        """
        result = self.dynamodbClient.put_dynamodb_item(table,data)

