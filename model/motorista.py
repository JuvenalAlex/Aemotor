from helpers.database import db


class Motorista(db.Model):

    __tablename__ = 'tb_motorista'

    id = db.Column(db.Integer, primary_key=True)
    rotas = db.Column(db.String(80), nullable=False)
    
    def __init__(self, rotas):
        self.rotas = rotas
     