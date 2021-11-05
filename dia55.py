from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/usuario/<apellido>')
def hello_world(apellido):
	return f'Hola {escape(apellido)}'

if __name__ == "__main__":
	app.run()