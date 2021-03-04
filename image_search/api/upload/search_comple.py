from . import *

@bp.route('/comple', methods=["POST"])
def comple_search():
    form = request.form
    Keyword = form.get("keyword",type=str)
    searchdic = {
        "suggest": {
            "tagsuggester": {
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
    response = response.suggest.tagsuggester[0].options
    for item in response:
        res_list.append(item.text)
    return jsonify(res_list)