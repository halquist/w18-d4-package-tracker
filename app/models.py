from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Package():
  __tablename__ = 'packages'

  id = db.Column(db.Integer, primary_key=True)
