import uuid
import re
import os
import threading
from datetime import date, datetime
import time
import csv
from db.db import get_connection

def lecturaDoc():

    conn = get_connection()
    sql = """INSERT INTO `tbl_datos` (`datoRegistrado`, `fechaCreacion`) VALUES ("'%s'", "'%s'")"""
    
    with open('example.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:

            cols = row[0].split(';') 
            for col in cols:
                
                fecha = datetime.today
               
                valores = (col, fecha)
                cursor = conn.cursor()
                cursor.execute(sql, valores)
            
    conn.commit()
    conn.close()
                
            