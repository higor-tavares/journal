from flask import Flask
from flask_restful import Api
from controllers.journal_controller import Journal

app = Flask(__name__)
api = Api(app)

api.add_resource(Journal, '/')

if __name__ == '__main__':
    app.run(debug=True)