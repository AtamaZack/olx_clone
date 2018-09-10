import re
from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from .models import USER_table, add_user

class Home(Resource):
    def get(self):
        return "Welcome to Katale stores"
class Signup(Resource):
    def get(self):
        return USER_table
    def post(self):
        json_data = request.get_json()
        required_fields = ["first name", "second name", "email", "password", "confirm password"]
        error_dict = dict()
        error_dict['errors'] = 0
        for field in required_fields:
            if field not in json_data.keys():
                error_dict['errors'] += 1
                error_dict['error {}'.format(error_dict['errors'])] = "missing json field for {}".format(field)
        for k, v in json_data.items():
            if v == "":
                error_dict['errors'] += 1
                error_dict['error {}'.format(error_dict['errors'])] = "missing field for {}".format(k)
        if json_data['password'] != json_data['confirm password']:
                error_dict['errors'] += 1
                error_dict['error {}'.format(error_dict['errors'])] = "passwords do not match"
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        email_check = re.match(email_regex, json_data['email'])
        if not email_check:
            error_dict['errors'] += 1
            error_dict['error {}'.format(error_dict['errors'])] = "email format invalid"
        for user in USER_table:
            if user['email'] == json_data['email']:
                error_dict['errors'] += 1
                error_dict['error {}'.format(error_dict['errors'])] = "Email already in use"
        if error_dict['errors'] == 0:
            hashed_pwd = generate_password_hash(
                json_data['password'], method='sha256')
            json_data['password'] = hashed_pwd
            json_data['token'] = ""
            del json_data['confirm password']
            add_user(json_data)
            return "Sign up successful!"
        return error_dict