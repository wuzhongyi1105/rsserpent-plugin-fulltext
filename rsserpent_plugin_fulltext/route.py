import time
import arrow
from rsserpent.utils import cached
from xml.dom.minidom import parse
import xml.dom.minidom
from urllib.request import urlopen
import requests
from gne import GeneralNewsExtractor

path = "/fulltext"

@cached
async def provider(url: str = None ) -> dict:    

    # 使用minidom解析器打开 XML 文档
    datasource = urlopen(url)
    DOMTree = xml.dom.minidom.parse(datasource)
    collection = DOMTree.documentElement

    titles = collection.getElementsByTagName("title")[0]
    links = collection.getElementsByTagName("link")[0]
    descriptions = collection.getElementsByTagName("description")[0]

    # 在集合中获取所有
    items = collection.getElementsByTagName("item")
    extractor = GeneralNewsExtractor()

    return {
        "title": titles.firstChild.data,
        "link": links.firstChild.data,
        "description": "",
        "items": [
            {
                "title": item.getElementsByTagName('title')[0].childNodes[0].data,
                "description": extractor.extract(str(requests.get(item.getElementsByTagName('link')[0].childNodes[0].data).text)),
                "link": item.getElementsByTagName('link')[0].childNodes[0].data,
                "pub_date": item.getElementsByTagName('pubDate')[0].childNodes[0].data,
            }
            for item in items
        ],
    }
