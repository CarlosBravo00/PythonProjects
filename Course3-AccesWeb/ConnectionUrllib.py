import urllib.request , urllib.error , urllib.parse 
import re

fhand = urllib.request.urlopen('https://carlosbravo00.github.io/ArantzaMagallanes/portafolio.html')

allwords = ""
for line in fhand:
    allwords = allwords + line.decode()

print(allwords)