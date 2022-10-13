from model.funcionario import Funcionario
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Funcionario(Resource):
    def get(self):
        current_app.logger.info("Get - Funcionario")
        funcionario = Funcionario.query\
            .order_by(Funcionario.curso)\
            .all()
        return funcionario, 200