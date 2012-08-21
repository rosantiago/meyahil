import os
from flask import Flask
from flask import render_template
from flask import url_for
from jinja2 import Template 


app = Flask(__name__)


#enrutamientos

#INDEX
@app.route('/')
def index(name = None):
<<<<<<< HEAD
	return render_template('content.html', name = 'Rodrigo Santiago de la Torre')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
=======
	return render_template('content.html', name = 'Rodrigo')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	#app.debug = True
>>>>>>> 11fe13be07f4f1101ca053041a30ba9c1b867800
	app.run(host='0.0.0.0', port=port)

