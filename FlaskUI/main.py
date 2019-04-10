import pyrebase
from flask import *

app = Flask(__name__)

config = {
    "authDomain": "rjiimageprocessing.firebaseapp.com",
    "apiKey": "AIzaSyC0hVt4CnAht6Mvo7M-yGO0Nf4kqlOW2-M",
    "databaseURL": "https://rjiimageprocessing.firebaseio.com",
    "projectId": "rjiimageprocessing",
    "storageBucket": "rjiimageprocessing.appspot.com",
    "messagingSenderId": "11581998729"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

@app.route('/', methods=['Get', 'Post'])
def login():
	unsuccessful = 'Invalid Login'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_in_with_email_and_password(email, password)
			return render_template("template.html")
		except:
			return render_template('login.html', us=unsuccessful)
	return render_template('login.html')	 

@app.route('/main')
def main():
    return render_template("template.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)


