import unittest
import json
from application import create_app, db
from application.models.event import Event, EventSchema


class TestEvents(unittest.TestCase):
    def setUp(self):
        print("Setting Up")
        self.app = create_app('testing')
        db.init_app(self.app)
        self.test_app = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        print("Tearing Down")
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

    def test_empty_db(self):
        """Start with a blank database."""

        rv = self.test_app.get('/')
        assert b'Boss Beginner API' in rv.data

    def test_get_all_events(self):
        event1 = Event('Metallica', "picture.com", "Sat, May 30, 2020", "6:00 pm EST", 'sample_link')
        event2 = Event('Staind', "picture2.com", "Sun, May 31, 2020", "7:00 pm EST", 'sample2_link')
        with self.app.app_context():
            db.session.add(event1)
            db.session.add(event2)
            db.session.commit()

        response = self.test_app.get(
            '/api/v1/resources/events/all',
            follow_redirects=True
        )

        # Assert response is 200 OK.
        assert response.status == "200 OK"
        payload = json.loads(response.data)
        self.assertEquals(len(payload), 2)
        assert payload[0]['name'] == "Metallica"
        assert payload[0]['date'] == "Sat, May 30, 2020"
        assert payload[0]['image'] == "picture.com"
        assert payload[0]['link'] == 'sample_link'
        assert payload[0]['time'] == "6:00 pm EST"
        assert payload[1]['name'] == "Staind"
        assert payload[1]['date'] == "Sun, May 31, 2020"
        assert payload[1]['image'] == "picture2.com"
        assert payload[1]['link'] == 'sample2_link'
        assert payload[1]['time'] == "7:00 pm EST"
        # with self.app.app_context():
        db.session.delete(event1)
        db.session.delete(event2)
        db.session.commit()

    def test_get_all_events_again(self):
        event1 = Event('Metallica', "picture.com", "Sat, May 30, 2020", "6:00 pm EST", 'sample_link')
        event2 = Event('Staind', "picture2.com", "Sun, May 31, 2020", "7:00 pm EST", 'sample2_link')
        with self.app.app_context():
            db.session.add(event1)
            db.session.add(event2)
            db.session.commit()

        response = self.test_app.get(
            '/api/v1/resources/events/all',
            follow_redirects=True
        )

        # Assert response is 200 OK.
        assert response.status == "200 OK"
        payload = json.loads(response.data)
        self.assertEquals(len(payload), 2)
        assert payload[0]['name'] == "Metallica"
        assert payload[0]['date'] == "Sat, May 30, 2020"
        assert payload[0]['image'] == "picture.com"
        assert payload[0]['link'] == 'sample_link'
        assert payload[0]['time'] == "6:00 pm EST"
        assert payload[1]['name'] == "Staind"
        assert payload[1]['date'] == "Sun, May 31, 2020"
        assert payload[1]['image'] == "picture2.com"
        assert payload[1]['link'] == 'sample2_link'
        assert payload[1]['time'] == "7:00 pm EST"
        # with self.app.app_context():
        db.session.delete(event1)
        db.session.delete(event2)
        db.session.commit()
