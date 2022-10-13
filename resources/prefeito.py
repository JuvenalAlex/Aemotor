from model.prefeito import Prefeito
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Prefeito(Resource):
    def get(self):
        current_app.logger.info("Get - Prefeito")
        prefeito = Prefeito.query\
            .order_by(Prefeito.curso)\
            .all()
        return prefeito, 200