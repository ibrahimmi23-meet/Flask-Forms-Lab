from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["amin","omar","loubna", "judeh", "Fouad", "Celina"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':

		return render_template('login.html')
	else:
		user = request.form['username']
		password1 = request.form['password']
		if user == username and password1 == password:
			return redirect(url_for('home'))
		return render_template('login.html')
	
@app.route('/home' )
def home():
	return render_template('home.html' , friends = facebook_friends)

@app.route('/friend/<string:name>', methods = ['GET', 'POST'] )
def friend(name):
	return render_template('friend_exists.html')


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)