from . import *

@bp.route('/search', methods=["POST"])
def image_search():
    form = request.form
    Keyword = form.get("keyword",type=str)
    searchdic = {
        "query": {
            "term": {
            "tags": f"{Keyword.strip()}"
            }
        }
    }

    s =Image.search().from_dict(searchdic)

    response = s.execute()
    res_list = []
    for hit in response:
        item  ={
            "url":hit.url,
            "tags":hit.tags
        }
        res_list.append(item)
        print(hit.tags)

    res = {
        "openid": "112323"
    }

    return jsonify(res_list)