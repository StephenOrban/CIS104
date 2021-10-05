def computepay(h,r):
    if h>40 :
        op = (h-40)*r*1.5
        rp = r*40
        p = op+rp
    else:
        p = h*r
    return(p)
hrs = input("enter hours: ")
h = float(hrs)
rat = input("enter rate: ")
r = float(rat)
pay= computepay (h,r)
print ("Pay", pay)
