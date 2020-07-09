import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

print('Retrieving:',url)
tags = soup('a')
alist = []
for tag in tags:
    alist.append(tag.get('href', None))

for x in range(count):
    url=alist[position]

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    print('Retrieving:',url)

    tags = soup('a')
    alist = []
    for tag in tags:
        alist.append(tag.get('href', None))


