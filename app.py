from flask import Flask
from flask_restful import Api
from config import postgresqlConfig
from resources.user import UserRegister

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, '/sign-up')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run()
