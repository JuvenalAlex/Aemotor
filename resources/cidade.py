from model.cidade import Cidade
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Cidade(Resource):
    def get(self):
        current_app.logger.info("Get - Cidade")
        cidade = Cidade.query\
            .order_by(Cidade.curso)\
            .all()
        return cidade, 200