from flask import  Flask

app = Flask(__name__)

@app.route('/')
def homepage():
	return "This is a HomePage"


@app.route('/about')
def about():
	return "This is the about page"

if __name__ == "__main__":
	app.run(debug = True)
