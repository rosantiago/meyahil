from meyahil import app
from meyahil.database import db_session

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    return 'Hello World!'