from model.rota import Rota
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Rota(Resource):
    def get(self):
        current_app.logger.info("Get - Rota")
        rota = Rota.query\
            .order_by(Rota.curso)\
            .all()
        return rota, 200