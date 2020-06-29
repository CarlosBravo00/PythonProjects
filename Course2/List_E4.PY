fname = input("Enter file name: ")
try:
    fhand = open(fname,'r')
except:
    print('file cannot be opened: ',fname)
    quit()

lst = list()
biglist = list()

for line in fhand:
    line = line.rstrip()
    lst = line.split() 
    for word in lst:
        if word not in biglist:
            biglist.append(word)


biglist.sort()
print(biglist)