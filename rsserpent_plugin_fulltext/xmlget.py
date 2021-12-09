import xml.sax

class itemHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.title = ""
      self.link = ""
      self.pub_date = ""
      self.description = ""

   # 元素开始调用
   def startElement(self, tag, attributes):
      self.CurrentData = tag

   # 元素结束调用
   def endElement(self, tag):
      if self.CurrentData == "title":
         print ("Title:", self.title)
      elif self.CurrentData == "link":
         print ("Link:", self.link)
      elif self.CurrentData == "pub_date":
         print ("pubDate:", self.pub_date)
      elif self.CurrentData == "description":
         print ("Description:", self.description)
      self.CurrentData = ""

   # 读取字符时调用
   def characters(self, content):
      if self.CurrentData == "title":
         self.title = content
      elif self.CurrentData == "link":
         self.link = content
      elif self.CurrentData == "pub_date":
         self.pub_date = content
      elif self.CurrentData == "description":
         self.description = content
  
if ( __name__ == "__main__"):
   
   # 创建一个 XMLReader
   parser = xml.sax.make_parser()
   # 关闭命名空间
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # 重写 ContextHandler
   Handler = itemHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("http://freebuf.com/feed")