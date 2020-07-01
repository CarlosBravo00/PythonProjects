import re
agg = 0
for line in open('example2.txt','r'):
    nums = re.findall('[0-9]+',line)
    for num in nums :
        agg += int(num)
print(agg)
