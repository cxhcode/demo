from pyquery import PyQuery as pq
from lxml import etree
import time
from urllib import request
import os

d = pq("<html></html>")
d = pq(etree.fromstring("<html></html>"))
d = pq(url='http://www.5442.com/meinv/')

for li in d(".imgList > ul > li"):
    x = pq(li)
    img_src = x("a > img[src]").attr('src')
    filename = img_src.split('/')[-1].split('!')[0]
    timestr = time.strftime('%Y/%m/%d/%M/', time.localtime(time.time()))
    if not os.path.exists(timestr):
        os.makedirs(timestr)
    with open(timestr + filename, 'wb') as f:
        f.write(request.urlopen(img_src).read())
