from model.veiculo import Veiculo
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Veiculo(Resource):
    def get(self):
        current_app.logger.info("Get - Veiculo")
        veiculo = Veiculo.query\
            .order_by(Veiculo.curso)\
            .all()
        return veiculo, 200