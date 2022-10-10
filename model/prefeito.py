from helpers.database import db


class Prefeito(db.Model):

    __tablename__ = 'tb_prefeito'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
     