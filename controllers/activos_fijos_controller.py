from flask import Blueprint, render_template, redirect, url_for
from models.activo_fijo import ActivoFijo
from app import db

activos_fijos_bp = Blueprint('activos_fijos_bp', __name__, url_prefix='/activos-fijos')

@activos_fijos_bp.route('/')
def listar_activos():
    activos = ActivoFijo.query.all()
    return render_template('activos_fijos/listar_activos.html', activos=activos)

@activos_fijos_bp.route('/<int:activo_id>')
def detalles_activo(activo_id):
    activo = ActivoFijo.query.get_or_404(activo_id)
    return render_template('activos_fijos/detalles_activo.html', activo=activo)
