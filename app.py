import os
from flask import Flask
from flask import render_template
from flask import url_for
from jinja2 import Template 


app = Flask(__name__)


Vars = {'title':"titulo", 'head':"cabecera", 'name':"Rodrigo Santiago de la Torre"}

#enrutamientos

#INDEX
@app.route('/')
def index(variables = Vars):
	return render_template('index.html', name = variables["name"])

@app.route('/prueba')
def prueba(variables = Vars):
	return render_template('prueba.html', name = variables["name"])

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)
