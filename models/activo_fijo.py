from app import db

class ActivoFijo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<ActivoFijo {self.nombre}>'
