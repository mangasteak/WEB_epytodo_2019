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