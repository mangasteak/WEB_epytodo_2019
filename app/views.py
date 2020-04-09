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