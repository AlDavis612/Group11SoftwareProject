from flask import *

app = Flask(__name__)

@app.route('/')
def main():
    # login for users
    # User selects a catogory of photos to be processed
    #       - Dropdown list of pre trained models for different catagories of images
    # Code to let the user choose a file and send it to our algortihm
    return render_template('template.html')

@app.route("/about")
def about():
    #Displays information about the development team
    return render_template("about.html")

@app.route("/home")
def home():
    # Code to ping the algorithm and collect top ranked images and
    # display them for the user to see
    # assign tags to the ranked photos
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)


