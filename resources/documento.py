##---Otros---##
from flask_restful import Resource
from flask import request
##from auth import token_required
from process import lecturaDoc

class Documento(Resource):

    process = lecturaDoc()

    # @token_required
    def post(self):

        """fecha_inicio = request.args["fecha_inicio"]
        fecha_final = request.args["fecha_final"]
        formato = request.args["formato"]
        oficial = request.args["oficial"]"""
        
        return self.process
        

    # @token_required
    def get(self):
        return self.post()
