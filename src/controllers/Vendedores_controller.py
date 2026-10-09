from flask import Blueprint, render_template

vendedores_bp = Blueprint('vendedores', __name__)

@vendedores_bp.route('/list_vendedores')
def list_vendedores():
    return render_template('vendedores/list_vendedores.html')

@vendedores_bp.route('/form_vendedores')
def form_vendedores():
    return render_template('vendedores/form_vendedores.html')