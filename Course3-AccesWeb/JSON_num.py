import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving',url)
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data)

agg = 0
for item in info['comments']:
    agg += int(item['count'])

print ('Sum:',agg)