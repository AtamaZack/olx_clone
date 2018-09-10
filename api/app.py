from flask import Flask
from flask_restful import Api
from .ver1.views import Home, Signup

APP = Flask(__name__)
version = '/api/ver1/'
API = Api(APP)

API.add_resource(Home, '{}'.format(version))
API.add_resource(Signup, '{}signup'.format(version))

