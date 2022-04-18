from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Olá Live de Python 162'
    
    return app


