from helpers.database import db


class Aluno(db.Model):

    __tablename__ = 'tb_aluno'

    id = db.Column(db.Integer, primary_key=True)
    instituicaoDeEnsino = db.Column(db.String(80), nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)

    def __init__(self, instituicaoDeEnsino, curso, matricula):
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula
        