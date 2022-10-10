from helpers.database import db


class Uf(db.Model):

    __tablename__ = 'tb_uf'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(90), nullable=False)
    sigla = db.Column(db.String(6), nullable=False)
   
    
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        