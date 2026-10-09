from flask import Blueprint, render_template

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/form_clients')
def form_clients():
    return render_template('/clientes/form_clients.html')

@clients_bp.route('/List_clients')
def List_clients():
    return render_template('/clientes/List_clients.html')