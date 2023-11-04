import boto3

class JournalDao():
    def __init__(self, dynamodbConnection):
        # Instantiate a table resource object without actually
        # creating a DynamoDB table. Note that the attributes of this table
        # are lazy-loaded: a request is not made nor are the attribute
        # values populated until the attributes
        # on the table resource are accessed or its load() method is called.
        self.table = dynamodbConnection.Table('journal')
    
    def create(self, item):
        self.table.put_item(
        Item = {
                'username': item.username,
                'id':item.id,
                'description':item.description,
                'amount':item.amount,
                'type':item.type,
                'entryDate': item.entryDate
            }
        )
