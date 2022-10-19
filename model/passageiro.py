from helpers.database import db


class Passageiro_db(db.Model):

    __tablename__ = 'tb_passageiro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cidadeOrigem = db.Column(db.String(90), nullable=False)
    cidadeDestino = db.Column(db.String(90), nullable=False)
    
    def __init__(self, nome, cidadeOrigem, cidadeDestino):
        self.nome = nome
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino
       