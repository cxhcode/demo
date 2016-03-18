from urllib import request


response = request.urlopen('http://image.5442.com/2015/0201/05/01.jpg!960.jpg')

content = response.read()

with open('img1.jpg','wb') as f:
    f.write(content)
