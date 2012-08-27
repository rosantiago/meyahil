import os
from flask import Flask
from flask import render_template
from flask import url_for
from jinja2 import Template 
from sqlalchemy import create_engine
import tweepy


app = Flask(__name__)


Vars = {'title':"titulo", 'head':"cabecera", 'name':"Rodrigo Santiago de la Torre"}

#tweepy vars
TOKEN = "85831956-oNc3bTqUb3RxvrWXmxAGUyRRirnxaa2Mx1HuPmuU"
TOKEN_KEY ="KyKZgLyhVWNqSWMyWHd9wb06xMASiH80czc6cewLk8"
CON_SEC = "bLJQSgEg9JEYt2jnAooSnw"
CON_SEC_KEY = "XqS4cQ7NhF5GHUPHUYxwDUQVXyjzsg2LSDhkQhsM"

auth = tweepy.OAuthHandler(CON_SEC, CON_SEC_KEY)
auth.set_access_token(TOKEN, TOKEN_KEY)

#conectar con twitter
api = tweepy.API(auth)
Nombre = api.me().name
user = api.get_user("scarlettagle")
#print amigo.__getstate__()
Amigos = []
for friend in user.friends():
	Amigos.append(friend.screen_name)



#Postgresql Heroku
engine = create_engine("postgresql+psycopg2://uqaahrbxjryovr:5OINFQLm37k1Wwm1ccrzgF2SLS@ec2-107-22-163-194.compute-1.amazonaws.com:5432/dppksd24msr1f", client_encoding='utf8')
Nombre = engine.execute("select 1").scalar()


#INDEX
@app.route('/')
def index():
	return render_template('index.html', amigos = Amigos)

@app.route('/prueba')
def prueba(variables = Vars):
	return render_template('prueba.html', nombre = Nombre)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)
