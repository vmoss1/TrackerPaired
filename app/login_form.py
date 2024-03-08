from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired , DataRequired


class LoginForm(FlaskForm):

    first_name = StringField("First Name" , validators=[InputRequired()])
    last_name = StringField("Last Name" , validators=[InputRequired()])
    username = StringField("User", choices=cities, validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
