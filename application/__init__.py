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
    from application.controllers.events_by_date import EventsByDateResource
    from application.controllers.events_by_id import EventsByIdResource
    from application.controllers.events_by_name import EventsByNameResource
    from application.controllers.events_by_keyword import EventsByKeywordResource

    api.add_resource(EventsAllResource, '/events/all', '/events/all')
    api.add_resource(EventsByDateResource, '/events/when', '/events/when')
    api.add_resource(EventsByIdResource, '/event_by_id', '/event_by_id')
    api.add_resource(EventsByNameResource, '/event_by_name', '/event_by_name')
    api.add_resource(EventsByKeywordResource, '/event_keyword', '/event_keyword')


    # api.add_resource(TasksResource, '/tasks', '/tasks/<int:task_id>')

    @app.route('/', methods=['GET'])
    def home():
        return "<h1>Boss Beginner API</h1>"

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app

