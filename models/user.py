from db import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    fullname = db.Column(db.String(80))

    def __init__(self, email, password, fullname):
        self.email = email
        self.password = password
        self.fullname = fullname

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(eamil=email).first()


