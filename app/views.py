from app import *
from flask import render_template, jsonify, request, session
import os
from config import *
from app.controller import Controller

@app.route("/", methods=["GET"])
def route_index():
    return render_template("index.html",
                            title="Some title",
                            myContent="Some content")

@app.route("/register", methods=["POST"])
def route_register():
    return Controller(get_connection(), app).handle_register(request)

@app.route("/signin", methods=["POST"])
def route_signin():
    return Controller(get_connection(), app).handle_signin(request)

@app.route("/signout", methods=["POST"])
def route_signout():
    return Controller(get_connection(), app).handle_signout()

@app.route("/user", methods=["GET"])
def route_user():
    return Controller(get_connection(), app).handle_user()

@app.route("/user/task/<id>", methods=["GET", "POST"])
def route_user_task_id(id):
    if request.method == "GET":
        return Controller(get_connection(), app).handle_user_task_id_get(id)
    return Controller(get_connection(), app).handle_user_task_id_post(id, request)

@app.route("/user/task/add", methods=["POST"])
def route_user_task_add():
    return Controller(get_connection(), app).handle_user_task_add(request)

@app.route("/user/task/del/<id>", methods=["POST"])
def route_user_task_del_id(id):
    return Controller(get_connection(), app).handle_user_task_del(id)