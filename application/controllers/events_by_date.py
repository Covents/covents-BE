from application.models.event import Event
from application import db
from flask_restful import Resource, reqparse, request, abort
from flask_marshmallow import Marshmallow
from application import build_schemas
from flask import jsonify


class EventsByDateResource(Resource):
    def get(self):
        date = request.args.get('date')
        search = "%{}%".format(date)
        events = Event.query.filter(Event.date.ilike(search)).all()
        events_schema, event_schema = build_schemas()
        if len(events) == 0:
            abort(404)
        return events_schema.jsonify(events)

