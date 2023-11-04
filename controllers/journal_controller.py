from flask_restful import Resource, reqparse, request
from models.journal_entry import JournalEntryEntity
from database.database_connection import DynamoDBConnection
from database.journal_dao import JournalDao

entries = []

class Journal(Resource):
    
    def __init__(self):
        self.dao = JournalDao(DynamoDBConnection.get_connection())

    def get(self):
        username = request.args['username']
        return {'entries': self.dao.find_by_username(username)}

class JournalEntry(Resource):
    def __init__(self):
        self.dao = JournalDao(DynamoDBConnection.get_connection())

    def get(self, id):
        username = request.args['username']
        journalEntry = self.dao.get(username, id)
        if journalEntry:
            return journalEntry, 200
        return {'message':'Journal entry not found'}, 404
        
    def post(self, id):
        args = reqparse.RequestParser()
        args.add_argument('description')
        args.add_argument('username')
        args.add_argument('amount')
        args.add_argument('type')
        data = args.parse_args()
        new_entry = JournalEntryEntity(id=id, **data)
        self.dao.create(new_entry)
        entries.append(new_entry.get_journal_entry())
        return new_entry.get_journal_entry(), 201
    
    def delete(self, id):
        pass

    def find_journal_entry(self, id):
        for entry in entries:
            if entry['id'] == id:
                return entry
        return None