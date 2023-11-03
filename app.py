from flask import Flask
from flask_restful import Api
from controllers.journal_controller import Journal, JournalEntry

app = Flask(__name__)
api = Api(app)

api.add_resource(Journal, '/')
api.add_resource(JournalEntry, '/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)