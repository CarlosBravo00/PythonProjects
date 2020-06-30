fname = input("Enter file name: ")
try:
    fhand = open(fname,'r')
except:
    print('file cannot be opened: ',fname)
    quit()

counts = dict()
lst = list()
for line in fhand:
    line = line.rstrip()
    lst = line.split() 
    if len(lst) < 3 or lst[0] != 'From' : 
        continue

    counts[lst[1]] = counts.get(lst[1],0) + 1
    
bigcount = None
bigword = None 
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword,bigcount)