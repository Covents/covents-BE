from app import db


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    link = db.Column(db.String())
    image = db.Column(db.String())
    date = db.Column(db.String())
    time = db.Column(db.String())


    def __init__(self, name, link, image, date, time):
        self.name = name
        self.link = link
        self.image = image
        self.date = date
        self.time = time


    def __repr__(self):
        return '<id {}>'.format(self.id)