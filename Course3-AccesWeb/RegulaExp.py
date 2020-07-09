import re

hold = dict()
hand = open('example.txt')
for line in hand:
    line = line.rstrip()
    #if re.search('^X-.*:',line):
    if re.search('^X-\S+?:',line) :
        lst = line.split(':')
        hold[lst[0]] = int(lst[1].strip())
print (hold)


x = 'Code 124 Attack 24 Defense 52'
y = re.findall('[0-9]+',x)
print(y)


para = 'From carloemiliobravomarquez@gmail.com Sat Jan  5'
email = re.findall('^From (\S+@\S+)',para)
print(email[0])

para = 'We just received $10.30 cookies'
y = re.findall('\$([0-9.]+)',para)
print(float(y[0]))