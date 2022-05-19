from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

city_list = [city for city in map]

class ShippingForm(FlaskForm):
  sender = StringField('Sender', validators=[DataRequired()])
  recipient = StringField('Recipient', validators=[DataRequired()])
  origin = SelectField('Origin', choices=city_list, validators=[DataRequired()])
  destination = SelectField('Destination', choices=city_list, validators=[DataRequired()])
  express = BooleanField('Express')
  submit = SubmitField('Submit')
