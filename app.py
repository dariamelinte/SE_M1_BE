from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from config.config import PORT, Config
from resources.login import Login
from resources.logout import Logout
from resources.forgot_password import ForgotPassword
from resources.register import Register

from resources.doctors import Doctors
from resources.patients import Patients

app = Flask(__name__)

app.config.from_object(Config)
db = MongoEngine()
db.init_app(app)
api = Api(app)
CORS(app,supports_credentials=True,origins='*')

api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(ForgotPassword, '/forgot_password')
api.add_resource(Register, '/register')

api.add_resource(Doctors, '/doctors')
api.add_resource(Patients, '/patients')

if __name__ == '__main__':
    app.run(port=PORT, host="0.0.0.0", debug=False)
