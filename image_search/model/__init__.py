from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from elasticsearch_dsl import connections
connections.create_connection(hosts=["http://fdata.wintoo.io:9200/"], timeout=20)
#client = Elasticsearch()


from .article import Article

from .image import Image