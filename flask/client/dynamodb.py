import boto3
from botocore.client import Config

class DynamodbClient:

    """
    This initalizes the aws credentials
    """
    def __init__(self,aws_access_key_id,aws_secret_access_key,region):
        self.session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
        self.dynamodb_client = self.session.client('dynamodb', region_name=region)
        self.dynamodb_resource = self.session.resource('dynamodb')

    """
    Given table name fetches all rows in the given table
    """
    def get_dynamodb_items(self,table):
        table = self.dynamodb_resource.Table(table)
        response = table.scan()
        return response['Items']

    """
    Puts an item to the table
    Eg : format of json data for table : {'name': {'S': 'Forrest Gump'}, 'year': {'S': '2023'}}
    """
    def put_dynamodb_item(self,table,data):
        self.dynamodb_client.put_item(TableName=table, Item=data)






