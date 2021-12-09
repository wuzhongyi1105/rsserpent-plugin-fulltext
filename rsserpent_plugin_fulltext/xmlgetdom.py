from xml.dom.minidom import parse
import xml.dom.minidom
from urllib.request import urlopen

# 使用minidom解析器打开 XML 文档
datasource = urlopen('http://www.freebuf.com/feed')
#DOMTree = xml.dom.minidom.parse('http://www.freebuf.com/feed')
DOMTree = xml.dom.minidom.parse(datasource)
collection = DOMTree.documentElement

titles = collection.getElementsByTagName("title")[0]
links = collection.getElementsByTagName("link")[0]
descriptions = collection.getElementsByTagName("description")[0]
print ("Title: %s" % titles.firstChild.data)
print ("Link: %s" % links.firstChild.data)
print ("Description: %s" % descriptions.firstChild.data)
# 在集合中获取所有
items = collection.getElementsByTagName("item")

# 打印每个的详细信息
for item in items:
   print ("*****item*****")

   title = item.getElementsByTagName('title')[0]
   print ("Title: %s" % title.childNodes[0].data)
   link = item.getElementsByTagName('link')[0]
   print ("Link: %s" % link.childNodes[0].data)
   pubDate = item.getElementsByTagName('pubDate')[0]
   print ("pubDate: %s" % pubDate.childNodes[0].data)
   description = item.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)