from flask import Flask
app = Flask(__name__)

def delayer(function):
	def wrapper_function():
		time.sleep(2)
		function()
	return wrapper_function

@delayer
@app.route('/')
def hello_world():
	return "TEST"

if __name__ == "__main__":
	app.run()