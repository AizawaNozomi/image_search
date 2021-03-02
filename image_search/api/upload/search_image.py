from . import *
# from elasticsearch_dsl import connections
# from elasticsearch import Elasticsearch
# from elasticsearch_dsl import Search
#connections.create_connection(hosts=["http://fdata.wintoo.io:9200/"], alias="default", timeout=20)


@bp.route('/search', methods=["POST"])
def image_search():
    form = request.form
    Keyword = form.get("Keyword",type=str)
    # client = Elasticsearch()

    searchdic = {
        "query": {"match": {"tags": "love"}}
    }

    s =Image.search().from_dict(searchdic)

    response = s.execute()

    for hit in response:
        print(hit.tags)

    res = {
        "openid": "112323"
    }

    return jsonify(res)