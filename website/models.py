from . import db
from sqlalchemy.sql import func


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(1000))
    state = db.Column(db.String(1000))
    country = db.Column(db.String(1000))
    nickname = db.Column(db.String(1000))
