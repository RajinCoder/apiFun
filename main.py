#from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import CompareForm
from flask_behind_proxy import FlaskBehindProxy
import git

app = Flask(__name__)
proxied = FlaskBehindProxy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'ba9758665999f3ca30026ae10bbb2ad7'
db = SQLAlchemy(app)

class comparedPlayers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player1 = db.Column(db.String(20), unique=True, nullable=False)
    player2 = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Compared('{self.player1}' vs '{self.player2}')"

with app.app_context():
    db.create_all()


@app.route("/update_server", methods=['POST'])
def webhook():
 if request.method == 'POST':
    repo = git.Repo('/home/apiFun/apiFun')
    origin = repo.remotes.origin
    origin.pull()
    return 'Updated PythonAnywhere successfully', 200
 else:
    return 'Wrong event type', 400


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    form = CompareForm()
    if form.validate_on_submit():
        compared = comparedPlayers(player1=form.player1.data, player2=form.player2.data)
        db.session.add(compared)
        db.session.commit()

        flash(f'Comparison for {form.player1.data} and {form.player2.data}!', 'success')
        return redirect(url_for('comparison'))
    return render_template('home.html', subtitle='Compare Two Players!', form=form)

@app.route("/comparison")
def comparison():
    return render_template('compare.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")