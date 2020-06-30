fname = input("Enter file name: ")
try:
    fhand = open(fname,'r')
except:
    print('file cannot be opened: ',fname)
    quit()

count = 0
scount = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else :
        pos = line.find(':')
        num = line[pos+1:]
        num = num.strip()
        value = float(num)

        count = count + 1 
        scount = scount + value
        avrg = scount/count

print("Average spam confidence:",str(avrg))

