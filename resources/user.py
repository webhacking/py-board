import re
from flask_restful import Resource, reqparse
from flask import abort
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('fullname', type=str, required=False)
    parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", data.email):
            abort(400, 'Invalid email address')

        if UserModel.find_by_email(data.email):
            abort(400, 'Account already exists')

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'user has been created successfully.'}, 201
