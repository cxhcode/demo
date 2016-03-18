# -*- coding: utf-8 -*-

from urllib import request
from html.parser import HTMLParser
from pyquery import PyQuery as pq
from lxml import etree

response = request.urlopen('http://www.5442.com/meinv/')
content = response.read().decode('gbk')
