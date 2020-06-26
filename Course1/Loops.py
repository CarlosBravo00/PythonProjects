# Order a set of int values 

count = 0
for i in [10,42,21,53,12,32] :
    count = count + 1
print("count " + str(count))


largest  = -1
for i in [10,42,21,53,12,32] :
    if(i > largest):
        largest = i
print("largest " + str(largest))


smallest  = None 
for i in [10,42,21,53,12,32] :
    if (smallest is None):
        smallest = i 
    if(i < smallest):
        smallest = i
print("smallest "+ str(smallest))


total = 0
for i in [10,42,21,53,12,32] :
    total += i
print("total "+ str(total))


found = False 
for i in [10,42,21,53,12,32] :
    if i == 12:
        found = True
        break
print("12 found "+ str(found))


largest  = -1
for i in [10,42,21,53,12,32] :
    if(i > largest):
        largest = i
print("largest " + str(largest))


