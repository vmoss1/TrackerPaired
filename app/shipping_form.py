from flask_wtf import FlaskForm
from wtforms import StringField , SelectField, BooleanField, SubmitField
from wtforms.validators import InputRequired , DataRequired
from map.map import map

cities = [(city, city) for city in map.keys()]

class ShippingForm(FlaskForm):
    # print(cities)
    sender_name = StringField("Sender Name" , validators=[InputRequired()])
    recipient_name = StringField("Recipient Name" , validators=[InputRequired()])
    origin = SelectField("Origin", choices=cities, validators=[DataRequired()])
    destination = SelectField("Destination", choices=cities, validators=[DataRequired()])
    express_shipping = BooleanField("Express Shipping" , default=False)
    submit = SubmitField("Submit")
    cancel = SubmitField('Cancel')
