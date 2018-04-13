from flask import Flask

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    bootstrap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
