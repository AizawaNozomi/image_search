from . import *


class Image(Document):
    url = Text()
    tags = Keyword()
    
    class Index:
        name = 'image'
        settings = {
          "number_of_shards": 2,
        }