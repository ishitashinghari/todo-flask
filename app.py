from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret-key'

db = SQLAlchemy(app)

from routes import *

with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)
