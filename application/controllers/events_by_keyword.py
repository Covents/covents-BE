from application.models.event import Event
from application import db
from flask_restful import Resource, reqparse, request, abort
from flask_marshmallow import Marshmallow
from application import build_schemas
from flask import jsonify


class EventsByKeywordResource(Resource):
    def get(self):
        keyword = request.args.get('keyword')
        search = "%{}%".format(keyword)
        events = Event.query.filter(Event.name.ilike(search)).all()
        events_schema, event_schema = build_schemas()
        results = events_schema.dump(events)
        if len(events) == 0:
            abort(404)
        return jsonify(results)
