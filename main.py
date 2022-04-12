from flask import Flask, request, jsonify
from flask_restful import Resource, Api
# from flask_apscheduler import APScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import json
import threading

from resources.documento import *

app = Flask(__name__)
api = Api(app)
api.add_resource(Documento, '/lectura_documento')

def header():
    print(""" ------- INICIO DE EJECUCION  ------- """)


if __name__ == '__main__':
    header()
    print("****** Entra al main y ejecuta proceso ******")
    app.run(port='5000')
    




