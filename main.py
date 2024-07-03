#from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#app.debug = True
#toolbar = DebugToolbarExtension(app)


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', subtitle='Compare Two Players!')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")