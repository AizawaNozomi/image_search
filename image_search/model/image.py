from . import *


class Image(Document):
    url = Text()
    tags = Text(analyzer="whitespace" )

    class Index:
        name = 'image_base'
        settings = {
          "number_of_shards": 2,
        }