from flask import Flask
from dotenv import load_dotenv
import os

from flask_sqlalchemy import SQLAlchemy
from os import path

load_dotenv()
secret_key = os.getenv('SECRET_KEY')

db = SQLAlchemy()
db_name = os.getenv('DB_NAME')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import Location

    with app.app_context():
        db.create_all()

    return app


def create_database():
    try:
        db.engine.execute('DROP TABLE IF EXISTS location')
        db.create_all()
        print('Created Database!')
    except Exception as e:
        print(f'Error occurred: {str(e)}')
