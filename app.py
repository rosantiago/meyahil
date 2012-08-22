import os
from flask import Flask
from flask import render_template
from flask import url_for
from jinja2 import Template 


app = Flask(__name__)


#mas enrutamientos

#INDEX
@app.route('/')
def index(name = None):
	return render_template('content.html', name = 'Rodrigo')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	#app.debug = True
	app.run(host='0.0.0.0', port=port)

