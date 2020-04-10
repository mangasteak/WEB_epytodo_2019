from app import *
from flask import *
from app.models import Models
import hashlib

class Controller():
    def __init__(self, connection, app):
        self.app = app
        self.connection = connection

    def is_connected(self, session):
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

    def handle_signin(self, request):
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
            if models.pwd_and_usr_match(username, password):
                session['logged_in'] = True
                session['username'] = username
                return jsonify({"result" : "signin successful"})
            return jsonify({"error" : "login or password does not match"})
        except:
            return jsonify({"error" : "internal error"})

    def handle_signout(self):
        session['logged_in'] = False
        session.pop('username', None)
        return jsonify({"result" : "signout successful"})

    def handle_user(self):
        try:
            if "logged_in" not in session or session['logged_in'] != True or "username" not in session:
                return jsonify({"error" : "you must be logged in"})
            return jsonify({"result" : {"username" : session["username"]}})
        except Exception as e:
            print(e)
            return jsonify({"error" : "internal error"})