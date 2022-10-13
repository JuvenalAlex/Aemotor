from model.instituicaoEnsino import InstituicaoDeEnsino
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class InstituicaoDeEnsino(Resource):
    def get(self):
        current_app.logger.info("Get - InstituicaoDeEnsino")
        instituicao = InstituicaoDeEnsino.query\
            .order_by(InstituicaoDeEnsino.curso)\
            .all()
        return instituicao, 200