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
        except:
            return jsonify({"error" : "internal error"})

    def user_has_task(self, id, username):
        models = Models()
        usr_id = models.get_usr_id(username)[0][0]
        return models.usr_has_task(usr_id, id)

    def id_to_status(self, id):
        possible_ids = [0, 1, 2]
        if id not in possible_ids:
            return "error"
        if id == 0:
            return "not started"
        elif id == 1:
            return "in progress"
        else:
            return "done"

    def handle_user_task_id_get(self, id):
        try:
            if "logged_in" not in session or session['logged_in'] != True or "username" not in session:
                return jsonify({"error" : "you must be logged in"})
            models = Models()
            if not models.task_exist(id):
                return jsonify({"error" : "task id does not exist"})
            if not self.user_has_task(id, session['username']):
                return jsonify({"error" : "not your task lmao"})
            task = models.get_task_info(id)
            return jsonify({"result" : {"title" : str(task[1]), "begin" : str(task[2]), "end" : str(task[3]), "status" : self.id_to_status(int(task[4]))}})
        except:
            return jsonify({"error" : "internal error"})

    def handle_user_task_id_post(self, id, request):
        try:
            if "logged_in" not in session or session['logged_in'] != True or "username" not in session:
                return jsonify({"error" : "you must be logged in"})
            models = Models()
            if not models.task_exist(id):
                return jsonify({"error" : "task id does not exist"})
            if not self.user_has_task(id, session['username']):
                return jsonify({"error" : "not your task lmao"})
            if "title" not in request.args or "begin" not in request.args or "end" not in request.args or "status" not in request.args:
                return jsonify({"error" : "internal error"})
            title = request.args["title"]
            begin = request.args["begin"]
            end = request.args["end"]
            status = request.args["status"]
            models.update_task(id, title, begin, end, status)
            return jsonify({"result" : "update done"})
        except:
            return jsonify({"error" : "internal error"})