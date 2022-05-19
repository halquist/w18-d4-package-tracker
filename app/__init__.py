from flask import Flask, render_template, redirect
from app.config import Config
from app.shipping_form import ShippingForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config) # loads the secret key and other config values from the .env file
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
  return '<h1>Package Tracker</h1>'

  CONNECTION_PARAMETERS = {
  'dbname': "package_tracker_app",
  'user': 'package_tracker_user',
  'password': 'password'
}

@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
  form = ShippingForm()
  if form.validate_on_submit():
    return redirect('/')
  return render_template('shipping_request.html', form=form)
