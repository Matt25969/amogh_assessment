from application import db
from flask_login import UserMixin

class Planets(db.Model):
    planet_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(20), nullable=False)
    year_of_discovery = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Float(5), nullable=False)
    radius = db.Column(db.Float(5), nullable=False)
    semi_major_axis = db.Column(db.Float(5), nullable=False)

    def __repr__(self):
        return ''.join([
            'Name: ', self.name,
            'Year of Discovery: ', self.year_of_discovery,
            'Mass: ', self.mass,
            'Radius: ', self.radius,
            'Semi-major Axis: ', self.semi_major_axis
        ])

class Users(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email])

class Favourites(db.Model):
    choice_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.planet_id'))

    def __repr__(self):
        return ''.join([
            'Choice ID: ', str(self.choice_id),
            'User ID: ', str(self.user_id),
            'Planet ID: ', str(self.planet_id)
        ])
