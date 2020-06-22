hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)

if h < 40 :
    pay = h*r
    print(pay)
else :
    pay = 40*r
    epay = (h-40) * (1.5*r)
    print( pay + epay )