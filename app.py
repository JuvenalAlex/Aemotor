from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from resources.cidade import Cidade
from resources.funcionario import Funcionario
from resources.gestorApp import GestorApp  # added to top of file
from resources.index import IndexResource
from resources.prefeitura import Prefeitura
from resources.endereco import Endereco
from resources.rota import Rota
from resources.pessoa import Pessoa
from resources.aluno import Aluno
from resources.prefeitura import Prefeitura
from resources.prefeito import Prefeito
from resources.passageiro import Passageiro
from resources.motorista import Motorista
from resources.uf import Uf
from resources.veiculo import Veiculo

from helpers.database import db

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aemotor:aemotor@localhost:5432/aemotor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


migrate = Migrate(app,db)

api = Api(app)

api.add_resource(IndexResource, '/')
api.add_resource(Endereco, '/enderecos')
api.add_resource(Pessoa, '/pessoas')
api.add_resource(Prefeitura, '/pessoas')
api.add_resource(Aluno, '/Aluno')
api.add_resource(Funcionario, '/Funcionario')
api.add_resource(GestorApp, '/GestorApp')
api.add_resource(Cidade, '/Cidade')
api.add_resource(Motorista, '/Motorista')
api.add_resource(Passageiro, '/Passageiro')
api.add_resource(Rota, '/Rota')
api.add_resource(Prefeito, '/Prefeito')
api.add_resource(Uf, '/Uf')
api.add_resource(Veiculo, '/Veiculo')

if __name__ == '__main__':
    
    app.run(debug=False)
