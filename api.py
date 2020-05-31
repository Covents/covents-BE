from flask import Flask
# from flask import abort
from flask_script import Manager
# from flask import make_response
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
# import sqlalchemy as sa
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from datetime import datetime
# from dateutil.tz import *

import os
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
ma = Marshmallow(app)


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    link = db.Column(db.String())
    image = db.Column(db.String())
    date = db.Column(db.String())
    time = db.Column(db.String())

    def __repr__(self):
        return '<id {}>' '<name {}>'.format(self.id, self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'link': self.link,
            'image': self.image,
            'date': self.date,
            'time': self.time
        }


# Events Schema
class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'link', 'image', 'date', 'time')


event_schema = EventSchema(many=False)
events_schema = EventSchema(many=True)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Boss Beginner API</h1>"


#
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)
#

@app.route('/api/v1/resources/events/all', methods=['GET'])
def events_all():
    all_events = Event.query.all()
    result = events_schema.dump(all_events)
    return jsonify(result)


@app.route('/api/v1/resources/event_by_id', methods=['GET'])
def get_event_by_id():
    search_id = request.args.get('id')
    event = Event.query.get(search_id)
    return event_schema.jsonify(event)


@app.route('/api/v1/resources/event_by_name', methods=['GET'])
def get_events_by_name():
    search_name = request.args.get('name')
    event = Event.query.filter_by(name=search_name).first()
    return event_schema.jsonify(event)


@app.route('/api/v1/resources/event_keyword', methods=['GET'])
def get_events_by_keyword():
    keyword = request.args.get('keyword')
    search = "%{}%".format(keyword)
    events = Event.query.filter(Event.name.ilike(search)).all()
    return events_schema.jsonify(events)


@app.route('/api/v1/resources/events/when', methods=['GET'])
def get_events_by_date():
    date = request.args.get('date')
    search = "%{}%".format(date)
    events = Event.query.filter(Event.date.ilike(search)).all()
    return events_schema.jsonify(events)


# @app.route('/api/v1/resources/events/when', methods=['GET'])
# def api_by_date():
#     # check if date was given as part of the URL
#     # if id date present, assign it to a variable
#     # if no date, display error
#     if 'date' in request.args:
#         date = int(request.args['date'])
#     else:
#         return "Error: No date field provided. Please specify a date."


if __name__ == "__main__":
    app.run()
