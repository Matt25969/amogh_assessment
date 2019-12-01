from application import db

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

