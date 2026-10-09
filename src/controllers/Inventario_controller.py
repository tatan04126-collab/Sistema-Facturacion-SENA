from flask import Blueprint, render_template

inventario_bp = Blueprint('inventario', __name__)

@inventario_bp.route('/list_inventario')
def list_inventario():
    return render_template('/inventario/list_inventario.html')

@inventario_bp.route('/form_inventario')
def form_inventario():
    return render_template('/inventario/form_inventario.html')