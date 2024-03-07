from flask_wtf import FlaskForm
from wtforms import StringField , SelectField, BooleanField
from wtforms.validators import InputRequired , DataRequired

class ShippingForm(FlaskForm):
    sender_name = StringField("Sender Name" , validators=InputRequired())
    recipient_name = StringField("Recipient Name" , validators=InputRequired())
    origin = SelectField("Origin" , validators=DataRequired())
    destination = SelectField("Destination" , validators=DataRequired())
    express_shipping = BooleanField("Express Shipping" , default=False)
    