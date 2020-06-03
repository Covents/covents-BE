from flask_marshmallow import Marshmallow
# from application import
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    link = db.Column(db.String())
    image = db.Column(db.String())
    date = db.Column(db.String())
    time = db.Column(db.String())

    def __init__(self, name, image, date, time, link):
        self.name = name
        self.image = image
        self.date = date
        self.time = time
        self.link = link

    def __repr__(self):
        return '<id {}>' '<name {}>'.format(self.id, self.name)


# Events Schema
class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'link', 'image', 'date', 'time')
