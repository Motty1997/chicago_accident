from flask import Flask
from controllers.accident_blueprint import accident_blueprint


def create_app():
    flask_app = Flask(__name__)
    return flask_app

if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(accident_blueprint, url_prefix="/api")
    app.run(debug=True)