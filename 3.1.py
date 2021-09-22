hrs = input("enter hours: ")
h = float(hrs)
rat = input("enter rate: ")
r = float(rat)
if h>40 :
    op = (h-40)*r*1.5
    rp = r*40
    p = op+rp
else:
    p = h*r
print(p)
