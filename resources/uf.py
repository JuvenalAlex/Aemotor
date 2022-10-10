from model.uf import Uf
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Uf(Resource):
    def get(self):
        current_app.logger.info("Get - Uf")
        endereco = Uf.query\
            .order_by(Uf.curso)\
            .all()
        return endereco, 200