from flask import Flask
from controllers.area_controller import areas
from controllers.times_controller import times
import logging


def create_app():
    flask_app = Flask(__name__)
    return flask_app

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(areas, url_prefix="/api/area")
    app.register_blueprint(times, url_prefix="/api/date")
    app.run(debug=True)
