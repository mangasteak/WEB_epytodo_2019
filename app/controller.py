from app import *
from flask import jsonify, session, request
from app.models import Models
import hashlib

class Controller():
    def __init__(self, connection, app):
        self.app = app
        self.connection = connection

    def is_connected(self, session=None):
        try:
            if session['logged_in'] == True:
                return True
            return False
        except:
            return False

    def handle_register(self, request):
        try:
            username = request.args["username"]
            password = request.args["password"]
            salt = "BEST_SALT" + username
            hash = hashlib.sha512()
            hash.update(salt.encode())
            hash.update(password.encode())
            password = hash.hexdigest()
            if self.is_connected(session) == True:
                return jsonify({"error" : "internal error"})
            models = Models()
            if models.account_exist(username):
                return jsonify({"error" : "account already exists"})
            models.create_account(username, password)
            return jsonify({"result" : "account created"})
        except:
            return jsonify({"error" : "internal error"})