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
    for word in lst:
        counts[word] = counts.get(word,0) + 1
    
top10 = list()

#LONG#
# # for key, val in counts.items():
# #     newtup = (val,key)
# #     top10.append(newtup)

# # top10 = sorted(top10, reverse=True)

#SHORT#
top10 = sorted( [ (v,k) for  k,v in counts.items() ] , reverse=True)

count = 0
for val,key in top10[:10] :
    print(count+1,':',key,val)
    count += 1