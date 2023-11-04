from flask_restful import Resource, reqparse, request
from models.journal_entry import JournalEntryEntity
from database.local_database_connection import DynamoDBConnection
from database.journal_dao import JournalDao
import uuid

class Journal(Resource):
    def __init__(self):
        self.dao = JournalDao(DynamoDBConnection.get_connection())

    def get(self):
        username = request.args['username']
        return {'entries': self.dao.find_by_username(username)}     
      
    def post(self):
        args = reqparse.RequestParser()
        args.add_argument('description')
        args.add_argument('username')
        args.add_argument('amount')
        args.add_argument('type')
        data = args.parse_args()
        new_entry = JournalEntryEntity(id=str(uuid.uuid4()), **data)
        self.dao.create(new_entry)
        return new_entry.get_journal_entry(), 201