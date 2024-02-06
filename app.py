from flask import Flask
from flask_restful import Api
from controllers.journal_controller import Journal
from flask_cors import CORS

app = Flask(__name__)
# Add CORS to the app
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

api = Api(app)

api.add_resource(Journal, '/')

if __name__ == '__main__':
    app.run(debug=True)