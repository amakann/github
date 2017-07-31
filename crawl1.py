import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.request import urlopen
f = urlopen('http://www.besmith.com/candidates/search-listings/')
encoding = f.info().get_content_charset(failobj="utf-8")
print('encoding:',encoding,file=sys.stderr)
text = f.read().decode('encoding')
print(text)
