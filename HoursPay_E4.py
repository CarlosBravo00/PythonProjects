def computepay(h,r):
    if h < 40 :
        pay = h*r
        return pay
    else :
        pay = 40*r
        epay = (h-40) * (1.5*r)
        return pay + epay 

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)
