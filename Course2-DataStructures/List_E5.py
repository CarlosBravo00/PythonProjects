fname = input("Enter file name: ")
try:
    fhand = open(fname,'r')
except:
    print('file cannot be opened: ',fname)
    quit()


lst = list()
count = 0
for line in fhand:
    line = line.rstrip()
    lst = line.split() 
    if len(lst) < 3 or lst[0] != 'From' : 
        continue

    print(lst[1])
    count = count +1

print("There were", count, "lines in the file with From as the first word")

