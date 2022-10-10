from model.passageiro import Passageiro
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Passageiro(Resource):
    def get(self):
        current_app.logger.info("Get - Passageiro")
        endereco = Passageiro.query\
            .order_by(Passageiro.curso)\
            .all()
        return endereco, 200