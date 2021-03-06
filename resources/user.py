import sqlite3
from sqlite3.dbapi2 import Cursor, connect
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        connection = sqlite3.connect('ooblets-collection.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201