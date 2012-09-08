import os
import simplejson
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import (User, Security, LoginForm,  login_required,
                                roles_accepted, user_datastore)
from flask.ext.security.datastore.sqlalchemy import SQLAlchemyUserDatastore
from flask import render_template
from flask import url_for
from jinja2 import Template 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uqaahrbxjryovr:5OINFQLm37k1Wwm1ccrzgF2SLS@ec2-107-22-163-194.compute-1.amazonaws.com:5432/dppksd24msr1f'
db = SQLAlchemy(app)
Security(app, SQLAlchemyUserDatastore(db))


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Usuario %r>' % self.username

Usuarios = Usuario.query.all()

#INDEX
@app.route('/')
def home():
    return simplejson.dumps([ dict(id = u.id,
                                   user_name = u.username,
                                   email = u.email) for u in Usuarios])


@app.route("/login")
def login():
    return render_template('login.html', form=LoginForm())

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.before_first_request
def before_first_request():
    user_datastore.create_role(name='admin')
    user_datastore.create_user(username='matt', email='matt@something.com',
                               password='password', roles=['admin'])

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)
