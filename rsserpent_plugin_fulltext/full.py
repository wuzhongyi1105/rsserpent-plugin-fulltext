import re
import requests
from urllib.request import urlopen
from gne import GeneralNewsExtractor

url = 'https://www.freebuf.com/news/307897.html'
datasource = urlopen(url)
""" page = requests.get(url)
page.encoding = 'utf-8' """
""" #编码……恐怕是Python里最让人头疼的问题了
soup = BeautifulSoup(str(page.text), 'html.parser')
print (soup) """

extractor = GeneralNewsExtractor()
result = extractor.extract(datasource)
print(result)


