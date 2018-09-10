from flask import Flask
from flask_restful import Api
from .ver1.views import Home

APP = Flask(__name__)
version = '/api/ver1/'
API = Api(APP)

API.add_resource(Home, '{}'.format(version))

