from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl import connections
from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
connections.create_connection(hosts=['192.168.50.92:9200'], timeout=20)
client = Elasticsearch()
