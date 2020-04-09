from flask import Flask
from app import *
from app.db_connection import *

app = Flask(__name__)
app.config.from_object("config")

connection = Connection(app)

def get_connection():
    return connection.get_connection()

from app import views