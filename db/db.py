import sys
import MySQLdb
from utils.properties import get_config


def get_connection():

    db_config = get_config()["database"]
    conn = MySQLdb.connect(
        host = db_config["server"],
        user = db_config["user"],   
        passwd = db_config["password"],  
        db = db_config["database"]
    )

   
    return conn
