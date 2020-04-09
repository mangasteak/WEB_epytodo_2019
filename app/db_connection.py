import pymysql as sql
from config import *
import sys

class Connection():

    def __init__(self, app):
        self.app = app
        try:
            self.connection = sql.connect(host=DATABASE_HOST,
                                    user=DATABASE_USER,
                                    unix_socket=DATABASE_SOCK,
                                    passwd=DATABASE_PASS,
                                    db=DATABASE_NAME)
            if self.connection == None:
                raise Exception
        except Exception as error:
            print(error)
            sys.exit(84)

    def get_connection(self):
        return self.connection