from app import db

class RegistroLibroMayor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuenta_id = db.Column(db.Integer, db.ForeignKey('cuenta.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    
    cuenta = db.relationship('Cuenta', backref=db.backref('registros', lazy=True))
    
    def __repr__(self):
        return f'<RegistroLibroMayor {self.fecha} - {self.descripcion}>'
