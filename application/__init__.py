from flask import Flask, make_response, jsonify, g
from flask.cli import with_appcontext
# from flask import abort
# from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from application.models.event import Event, EventSchema
import os
from application.config import app_config
from flask_restful import Api

event_schema = None
events_schema = None
db = SQLAlchemy()
ma = Marshmallow()

def build_schemas():
    global event_schema, events_schema
    from application.models.event import Event, EventSchema
    if event_schema is None:
        event_schema = EventSchema(many=False)
    if events_schema is None:
        events_schema = EventSchema(many=True)
    return events_schema, event_schema


def create_app(config_name):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    ma.init_app(app)
    build_schemas()
    api = Api(app)
    api.prefix = '/api/v1/resources'

    from application.controllers.events_all import EventsAllResource
    # from application.controllers import *

    api.add_resource(EventsAllResource, '/events/all', '/events/all')

    # api.add_resource(EventsResource, '/events/when', '/events/when')
    # api.add_resource(EventsResource, '/events', '/events/all')
    # api.add_resource(EventsResource, '/events', '/events/all')
    # api.add_resource(EventsResource, '/events', '/events/all')

    # api.add_resource(TasksResource, '/tasks', '/tasks/<int:task_id>')

    @app.route('/', methods=['GET'])
    def home():
        return "<h1>Boss Beginner API</h1>"

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app

    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'link': self.link,
    #         'image': self.image,
    #         'date': self.date,
    #         'time': self.time
    #     }

#
# @app.route('/api/v1/resources/events/all', methods=['GET'])
# def events_all():
#     all_events = Event.query.all()
#     result = events_schema.dump(all_events)
#     if len(result) == 0:
#         abort(404)
#     return jsonify(result)

#
# @app.route('/api/v1/resources/event_by_id', methods=['GET'])
# def get_event_by_id():
#     search_id = request.args.get('id')
#     event = Event.query.get(search_id)
#     if event is None:
#         abort(404)
#     return event_schema.jsonify(event)
#
#
#
# @app.route('/api/v1/resources/event_by_name', methods=['GET'])
# def get_events_by_name():
#     search_name = request.args.get('name')
#     event = Event.query.filter_by(name=search_name).first()
#     if event is None:
#         abort(404)
#     return event_schema.jsonify(event)
#
#
# @app.route('/api/v1/resources/event_keyword', methods=['GET'])
# def get_events_by_keyword():
#     keyword = request.args.get('keyword')
#     search = "%{}%".format(keyword)
#     events = Event.query.filter(Event.name.ilike(search)).all()
#     results = events_schema.dump(events)
#     if len(events) == 0:
#         abort(404)
#     return jsonify(results)
#
#
# @app.route('/api/v1/resources/events/when', methods=['GET'])
# def get_events_by_date():
#     date = request.args.get('date')
#     search = "%{}%".format(date)
#     events = Event.query.filter(Event.date.ilike(search)).all()
#     if len(events) == 0:
#         abort(404)
#     return events_schema.jsonify(events)

# from application.controllers.events_all import EventsResource


# if __name__ == "__main__":
#     app.run()
