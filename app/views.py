from app import app
from flask import render_template, jsonify
import pymysql as sql
import os
from config import *

@app.route("/", methods=["GET"])
def route_index():
    return render_template("index.html",
                            title="Hello World",
                            myContent="My SUPER content!!")

@app.route("/user/<username>", methods=["GET"])
def route_user(username):
    return render_template("index.html",
                            title="Hello " + username,
                            myContent="My SUPER content for " + username + "!!!")

@app.route("/user")
def route_all_users():
    result = ""
    try:
        connect = sql.connect(host=DATABASE_HOST,
                              user=DATABASE_USER,
                              passwd=DATABASE_PASS,
                              db=DATABASE_NAME)
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM user")
        result = cursor.fetchall()
        cursor.close()
        connect.close()
    except Exception as e:
        print("Caught an exception :", e)
    return jsonify(result);