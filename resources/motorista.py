from model.motorista import Motorista
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Motorista(Resource):
    def get(self):
        current_app.logger.info("Get - Motorista")
        endereco = Motorista.query\
            .order_by(Motorista.curso)\
            .all()
        return endereco, 200