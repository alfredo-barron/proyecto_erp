from flask import Blueprint, render_template, redirect, url_for
from models.libro_mayor import RegistroLibroMayor
from app import db

libro_mayor = Blueprint('libro_mayor', __name__, url_prefix='/libro-mayor')

@libro_mayor.route('/')
def listar_registros():
    registros = RegistroLibroMayor.query.all()
    return render_template('libro_mayor/listar_registros.html', registros=registros)

@libro_mayor.route('/<int:registro_id>')
def detalles_registro(registro_id):
    registro = RegistroLibroMayor.query.get_or_404(registro_id)
    return render_template('libro_mayor/detalles_registro.html', registro=registro)
