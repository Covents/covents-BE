import os
import tempfile
from application import create_app
config_name = "testing"
app = create_app(config_name)
from application.models.event import Event, EventSchema
import pytest


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            app.init_db()
        yield client

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'No entries here so far' in rv.data

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])