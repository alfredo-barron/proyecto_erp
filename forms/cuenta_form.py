from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired

class CuentaForm(FlaskForm):
    nombre = StringField('Nombre de la cuenta', validators=[DataRequired()])
    saldo = FloatField('Saldo inicial', validators=[DataRequired()])
    
