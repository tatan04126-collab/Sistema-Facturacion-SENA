from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.controllers.home_controller import home_bp
    from src.controllers.clients_controller import clients_bp
    from src.controllers.Promociones_controller import promociones_bp
    from src.controllers.Vendedores_controller import vendedores_bp
    from src.controllers.Administracion_controller import admin_bp
    from src.controllers.Inventario_controller import inventario_bp
    from src.controllers.Facturacion_controller import facturacion_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(promociones_bp)
    app.register_blueprint(vendedores_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(inventario_bp)
    app.register_blueprint(facturacion_bp)

    return app