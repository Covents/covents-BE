from flask import Flask
from flask import abort
from flask import make_response
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# from models import Result


# create some test data
events = [
    {'id': 0,
     'link': 'https://www.eventbrite.co.uk/e/one-direction-2020-at-home-tickets-105236948546?aff=ebdssbonlinesearch',
     'image': 'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F100862282%2F446435521372%2F1%2Foriginal.20200513-122914?w=1080&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C24%2C768%2C384&s=7f4b36f7ca3fae9953b71f9e98df0157',
     'date': '30 May 2020',
     'time': "18:00 - 20:00 BST"},
    {'id': 1,
     'link': 'https://www.eventbrite.co.uk/e/zayn-malik-party-tickets-104380292264?aff=ebdssbonlinesearch',
     'image': 'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F100189414%2F444571810080%2F1%2Foriginal.20200505-023120?w=1080&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C125%2C500%2C250&s=73c9544e3f90a70ea11fdf8080cd6e12',
     'date': '31 May 2020',
     'time': "19:00 CDT"}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Boss Beginner API</h1>"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1/resources/events/all', methods=['GET'])
def events_all():
    return jsonify(events)


# @app.route('/api/v1/resources/events/<int:event_id>', methods=['GET'])
# def by_id(event_id):
#     event = [event for event in events if event['id'] == event_id]
#     if len(event) == 0:
#         abort(404)
#     return jsonify({'event' : event[0]})
#
#
#
@app.route('/api/v1/resources/events/when', methods=['GET'])
def api_by_date():
    # check if date was given as part of the URL
    # if id date present, assign it to a variable
    # if no date, display error
    if 'date' in request.args:
        date = int(request.args['date'])
    else:
        return "Error: No date field provided. Please specify a date."

        # Create an empty list for our results
    results = []

    # Loop through the data and match the result that fits the requested ID.
    for event in events:
        if event['date'] == date:
            results.append(event)

    # Use the jsonify function from Flask to convert to the JSON format.
    return jsonify(results)


app.run()
db = SQLAlchemy(app)