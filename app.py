import os
from flask import Flask
from flask import render_template
from flask import url_for
from jinja2 import Template 
from sqlalchemy import create_engine
import tweepy


app = Flask(__name__)

#pruebas
#Vars = {'title':"titulo", 'head':"cabecera", 'name':"Rodrigo Santiago de la Torre"}

#TWITTER CONNECTION
tweepy_TOKEN = "85831956-oNc3bTqUb3RxvrWXmxAGUyRRirnxaa2Mx1HuPmuU"
tweepy_TOKEN_KEY ="KyKZgLyhVWNqSWMyWHd9wb06xMASiH80czc6cewLk8"
tweepy_CON_SEC = "bLJQSgEg9JEYt2jnAooSnw"
tweepy_CON_SEC_KEY = "XqS4cQ7NhF5GHUPHUYxwDUQVXyjzsg2LSDhkQhsM"

tweepy_auth = tweepy.OAuthHandler(tweepy_CON_SEC, tweepy_CON_SEC_KEY)
tweepy_auth.set_access_token(tweepy_TOKEN, tweepy_TOKEN_KEY)

tweepy_api = tweepy.API(tweepy_auth)
tweepy_Nombre = tweepy_api.me().name
tweepy_user = tweepy_api.get_user("brokenarrow16")
#print amigo.__getstate__()
tweepy_Amigos = []
for friend in tweepy_user.friends():
	tweepy_Amigos.append(friend.screen_name)

tweepy_Seguidores = []
for seguidor in tweepy_user.followers():
	tweepy_Seguidores.append(seguidor.screen_name)
#Postgresql Heroku
engine = create_engine("postgresql+psycopg2://uqaahrbxjryovr:5OINFQLm37k1Wwm1ccrzgF2SLS@ec2-107-22-163-194.compute-1.amazonaws.com:5432/dppksd24msr1f", client_encoding='utf8')
Nombre = engine.execute("select 1").scalar()


#INDEX
@app.route('/')
def index():
	return render_template('index.html', amigos = tweepy_Amigos)

@app.route('/prueba')
def prueba(variables = Vars):
	return render_template('prueba.html', nombre = Nombre)

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)
