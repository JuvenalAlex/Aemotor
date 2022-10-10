from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal

from model.pessoa import PessoaModel


class Pessoa(Resource):
    def get(self):
        current_app.logger.info("Get - Pessoas ")
        prefeitura = Pessoa.query\
            .order_by(PessoaModel.email)\
            .all()
        return prefeitura, 200