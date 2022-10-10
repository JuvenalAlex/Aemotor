from model.gestorApp import GestorApp
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class GestorApp(Resource):
    def get(self):
        current_app.logger.info("Get - GestorApp")
        endereco = GestorApp.query\
            .order_by(GestorApp.curso)\
            .all()
        return endereco, 200