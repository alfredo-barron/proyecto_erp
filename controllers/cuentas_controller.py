from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.cuenta import Cuenta
from forms.cuenta_form import CuentaForm
from app import db

cuentas = Blueprint('cuentas', __name__, url_prefix='/cuentas')

@cuentas.route('/')
def listar_cuentas():
    cuentas = Cuenta.query.all()
    return render_template('cuentas/listar_cuentas.html', cuentas=cuentas)

@cuentas.route('/nueva', methods=['GET', 'POST'])
def nueva_cuenta():
    form = CuentaForm()
    if form.validate_on_submit():
        # Crear una nueva cuenta con los datos del formulario
        cuenta = Cuenta(nombre=form.nombre.data, saldo=form.saldo.data)
        
        # Guardar la nueva cuenta en la base de datos
        db.session.add(cuenta)
        db.session.commit()
        
        # Mensaje flash para indicar que la cuenta se ha creado exitosamente
        flash('La cuenta ha sido creada correctamente.', 'success')

        # Redirigir a la lista de cuentas o a donde desees
        return redirect(url_for('cuentas.listar_cuentas'))
    return render_template('nueva_cuenta.html', title='Nueva Cuenta', form=form)

@cuentas.route('/<int:cuenta_id>')
def detalles_cuenta(cuenta_id):
    cuenta = Cuenta.query.get_or_404(cuenta_id)
    return render_template('cuentas/detalles_cuenta.html', cuenta=cuenta)

@cuentas.route('/<int:cuenta_id>/editar', methods=['GET', 'POST'])
def editar_cuenta(cuenta_id):
    cuenta = Cuenta.query.get_or_404(cuenta_id)
    if request.method == 'POST':
        cuenta.nombre = request.form['nombre']
        cuenta.saldo = float(request.form['saldo'])
        db.session.commit()
        flash('Cuenta actualizada exitosamente!', 'success')
        return redirect(url_for('cuentas.listar_cuentas'))
    return render_template('cuentas/editar_cuenta.html', cuenta=cuenta)

@cuentas.route('/<int:cuenta_id>/eliminar', methods=['POST'])
def eliminar_cuenta(cuenta_id):
    cuenta = Cuenta.query.get_or_404(cuenta_id)
    db.session.delete(cuenta)
    db.session.commit()
    flash('Cuenta eliminada exitosamente!', 'success')
    return redirect(url_for('cuentas.listar_cuentas'))
