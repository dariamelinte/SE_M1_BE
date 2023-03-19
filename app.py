from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from resources.login import Login

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')

if __name__ == '__main__':
    app.run(port=3001, host="0.0.0.0", debug=False)
