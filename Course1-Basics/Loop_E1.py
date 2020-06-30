num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    try :
        fval = float(sval)
        num = num + 1
        tot = tot + fval
    except:
        if sval == 'done':
           break 
        else:
            print('Bad Input')
            continue 

print('All DONE')
print(tot,num,tot/num)