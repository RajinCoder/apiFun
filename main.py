#from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect, request
import git

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#app.debug = True
#toolbar = DebugToolbarExtension(app)


@app.route("/update_server", methods=['POST'])
def webhook():
 if request.method == 'POST':
    repo = git.Repo('/home/apiFun/apiFun')
    origin = repo.remotes.origin
    origin.pull()
    return 'Updated PythonAnywhere successfully', 200
 else:
    return 'Wrong event type', 400

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', subtitle='Compare Two Players!')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")