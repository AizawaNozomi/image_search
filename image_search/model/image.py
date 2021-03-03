from . import *


class Image(Document):
    url = Text()
    tags = Text(analyzer="whitespace" )
    text = Text(analyzer="standard")
    tag_completion = Completion()

    class Index:
        name = 'image_base'
        settings = {
          "number_of_shards": 2,
        }