import os
import simplejson
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uqaahrbxjryovr:5OINFQLm37k1Wwm1ccrzgF2SLS@ec2-107-22-163-194.compute-1.amazonaws.com:5432/dppksd24msr1f'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username



#INDEX
@app.route('/')
def home():
    return simplejson.dumps([ dict(id = u.id,
                                   user_name = u.username,
                                   email = u.email) for u in User.query.all()])


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)
