from model.aluno import Aluno
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Aluno(Resource):
    def get(self):
        current_app.logger.info("Get - Aluno")
        endereco = Aluno.query\
            .order_by(Aluno.curso)\
            .all()
        return endereco, 200