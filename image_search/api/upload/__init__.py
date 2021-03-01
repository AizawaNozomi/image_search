from flask import Blueprint
from image_search.model import *
from flask import request, g
from  typing import List

bp = Blueprint("Image", __name__)

from .saveImage import save_image