from flask import Flask
from flask_cors import CORS
from .model import *
from .config import *
from .api import *


def init_elk_model():
    Image.init()


# init_model()
def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    #init_elk_model()
    app.register_blueprint(image_bp)
    return app