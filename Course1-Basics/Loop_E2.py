smallest  = None 
largest  = None
while True :
    sval = input('Enter a number: ')
    try :
        fval = float(sval)
    except:
        if sval == 'done':
           break 
        else:
            print('Invalid input')
            continue 

    if (smallest is None):
        smallest = fval 
    elif(fval < smallest):
        smallest = fval

    if (largest is None):
        largest = fval
    elif(fval > largest):
        largest = fval

print("Maximum is", int(largest))
print("Minimum is", int(smallest))