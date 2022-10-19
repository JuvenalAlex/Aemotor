from helpers.database import db


class GestorApp_db(db.Model):

    __tablename__ = 'tb_gestorApp'

    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.String(80), nullable=False)
    
    def __init__(self, admin):
        self.admin = admin
     