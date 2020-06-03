from application.models.event import Event
from application import db
from flask_restful import Resource, reqparse, request, abort
from flask_marshmallow import Marshmallow
from application import build_schemas
from flask import jsonify



class EventsAllResource(Resource):
    def get(self):
        all_events = Event.query.all()
        events_schema, event_schema = build_schemas()
        result = events_schema.dump(all_events)
        if len(result) == 0:
            abort(404)
        return jsonify(result)

