#Read a simple file
fname = input('Enter the file name:  ')
try:
    fhand = open(fname,'r')
except:
    print('file cannot be opened: ',fname)
    quit()

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)

    