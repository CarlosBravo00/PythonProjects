s = input("Numero: ") 
#S tiene que ser Int
try:
    n = int(s)
    n = n + 5
    if type (n) == int:
        print (n) 
    else:
        print ("Error") 
except:
    n = 0
    print ("Error") 
