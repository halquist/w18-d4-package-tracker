from flask import Flask, render_template
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config) # loads the secret key and other config values from the .env file

@app.route('/')
def index():
  return '<h1>Package Tracker</h1>'
