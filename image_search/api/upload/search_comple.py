from . import *

@bp.route('/comple', methods=["POST"])
def comple_searhc():
    form = request.form
    Keyword = form.get("keyword",type=str)
    searchdic = {
        "size": 0,
        "suggest": {
            "article-suggester": {
            "prefix": f"{Keyword.strip()}",
            "completion": {
                "field": "tag_completion"
            }
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