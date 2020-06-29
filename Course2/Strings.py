fruit = 'Banana'
print(fruit[0])
print(len(fruit))

count = 0
for letter in fruit:
    print(letter)
    if letter == 'a':
        count = count + 1
print(count)

print(fruit[2:])  # print(fruit[2:6])

if 'nana' in fruit :
    print('yeah')

fruit = fruit.lower()
print(fruit)   