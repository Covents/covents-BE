from application.models.event import Event
from application import db
from flask_restful import Resource, reqparse, request, abort
from flask_marshmallow import Marshmallow
from application import build_schemas
from flask import jsonify


class EventsByIdResource(Resource):
    def get(self):
        search_id = request.args.get('id')
        event = Event.query.get(search_id)
        events_schema, event_schema = build_schemas()
        if event is None:
            abort(404)
        return event_schema.jsonify(event)

