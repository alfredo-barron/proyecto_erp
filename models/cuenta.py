from app import db

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    saldo = db.Column(db.Float, default=0.0)
    
    def __repr__(self):
        return f'<Cuenta {self.nombre}>'
