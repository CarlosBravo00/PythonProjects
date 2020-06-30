x=input('Number: ')

stuff = list()
for i in range(int(x)):
    stuff.append(input('Give me number ' + str(i+1) + ': '))
    
print(stuff,len(stuff))
stuff.sort()
print(stuff,len(stuff))


a='123123213'
stuff = a.split('2')
print(stuff,len(stuff))

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])