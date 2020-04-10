import pymysql as sql
from app import *
from flask import jsonify

class Models():
    def __init__(self):
        self.connection = get_connection()

    def account_exist(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(1) FROM user WHERE username = '%s'"% (username))
        result = cursor.fetchone()[0]
        cursor.close()
        if result == 0:
            return False
        return True

    def pwd_and_usr_match(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(1) FROM user WHERE username = '%s' AND password = '%s'"% (username, password))
        result = cursor.fetchone()[0]
        cursor.close()
        if result == 0:
            return False
        return True

    def create_account(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO user (username, password) VALUES ('%s', '%s')"% (username, password))
        self.connection.commit()
        cursor.close()
