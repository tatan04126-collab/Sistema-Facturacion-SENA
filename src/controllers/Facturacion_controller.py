from flask import Blueprint, render_template

facturacion_bp = Blueprint('facturacion', __name__)

@facturacion_bp.route('/list_facturacion')
def list_facturacion():
    return render_template('list_facturacion.html')