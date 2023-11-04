import boto3

class DynamoDBConnection():

    @staticmethod
    def get_connection():
        # Get the service resource.
        return boto3.resource('dynamodb', endpoint_url='http://localhost:8000')