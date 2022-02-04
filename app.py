"""Flask app for adopt app."""

from flask import Flask, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


connect_db(app)
db.create_all()


app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)


@app.get("/")
def homepage():
    """Homepage which lists pets"""

    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)
