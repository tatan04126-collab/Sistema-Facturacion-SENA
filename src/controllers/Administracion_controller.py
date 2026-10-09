from flask import Blueprint, render_template

admin_bp = Blueprint('administracion', __name__)

@admin_bp.route('/list_administracion')
def list_administracion():
    return render_template('list_administracion.html')