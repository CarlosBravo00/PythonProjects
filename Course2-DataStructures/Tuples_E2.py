fname = input("Enter file name: ")
fhand = open('mbox-short.txt','r')

counts = dict()
Datalst = list()

for line in fhand:
    line = line.rstrip()
    lst = line.split() 
    if len(lst) < 3 or lst[0] != 'From' : 
        continue
    else:
        date = lst[5]
        dates = date.split(':')
        counts[dates[0]] = counts.get(dates[0],0) + 1

for k , v in sorted(counts.items()):
    print (k,v)