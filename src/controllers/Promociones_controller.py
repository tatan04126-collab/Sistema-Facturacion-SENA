from flask import Blueprint, render_template

promociones_bp = Blueprint('promociones', __name__)

@promociones_bp.route('/list_promociones')
def list_promociones():
    return render_template('promociones/list_promociones.html')

@promociones_bp.route('/form_promociones')
def form_promociones():
    return render_template('promociones/form_promociones.html')