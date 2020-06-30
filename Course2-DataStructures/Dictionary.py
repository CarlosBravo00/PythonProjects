bag = dict()
bag['money'] = 13
bag['candy'] = 0
bag['tissues'] = 75
print(bag)

while True :
    x = input('new object: ')
    if x in bag:
        print('added object')
        bag[x] += 1

    else:
        if x == 'done' or x =='Done':
            break
        else:
            print('adding new object')
            bag[x] = 1

    print(bag)

print('All done',bag)