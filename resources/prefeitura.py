from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal

from model.prefeitura import Prefeitura


class Prefeitura(Resource):
    def get(self):
        current_app.logger.info("Get - Prefeituras ")
        prefeitura = Prefeitura.query\
            .order_by(Prefeitura.email)\
            .all()
        return prefeitura, 200