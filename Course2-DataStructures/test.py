arr1 = [5, 6, 20, 50,60]
arr2 =  [2, 3, 4, 5]
i1 = 0
i2 = 0
arrf = []

while True:
        if(i1 == len(arr1) or i2 ==len(arr2)): break 
    
        if(arr1[i1] <  arr2[i2]):
            arrf.append(arr1[i1])
            i1 = i1 + 1
        else:
            arrf.append(arr2[i2])
            i2 = i2 + 1

while i1 < len(arr1):
    arrf.append(arr1[i1])
    i1 = i1 + 1
        
while i2 < len(arr2):
    arrf.append(arr2[i2])
    i2 = i2 + 1
        
print(arrf)
    
        