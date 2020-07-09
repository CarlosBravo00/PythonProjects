import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving',url)
xml = urllib.request.urlopen(url, context=ctx).read()

stuff = ET.fromstring(xml)
lst = stuff.findall('comments/comment')

print('Count', len(lst),)

agg = 0
for item in lst:
    agg += int(item.find('count').text)

print ('sum',agg)