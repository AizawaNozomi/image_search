from . import *
from flask import jsonify


@bp.route('/save', methods=["POST"])
def save_image():
    form = request.form
    url = form.get("url",type=str)
    tags = form.get("tags", type=str)
    print(tags, url)
    res = {
        "openid": "112323"
    }
    return jsonify(res)