"""Forms for adopt app."""

from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, AnyOf, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(["cat", "dog", "porcupine"], "Invalid species")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message = "Not a url")])
    age = SelectField(
        "Age",
        choices=[
            ("baby", "Baby"),
            ("young", "Young"),
            ("adult", "Adult"),
            ("senior", "Senior"),
        ],
        validators = [InputRequired(), AnyOf(["baby","young","adult","senior"])]
    )
    notes = TextAreaField("Notes")
