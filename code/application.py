from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'

db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'hello!'


@app.route('/drinks')
def get_drink():
    drinks = Drink.query.all()
    output = []

    for drink in drinks:
        drink_data = {
            'name': drink.name,
            'description': drink.description
        }
        output.append(drink_data)

    return {'drinks': output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    