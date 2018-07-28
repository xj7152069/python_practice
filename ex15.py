def s(pi,r):
    s=4*pi*r**2
    return s
def l(pi,r):
    l=2*pi*r
    return l
from sys import argv
script,r1=argv
r=float(r1)
pi=3.1415926
print "the surfance area is: %.3f"%s(pi,r),"km**2"
print "The lenth is: %.3f"%l(pi,r),"km"
if l(pi,r)>22500:
    print "the plant is more similiar with Earth"
else:
    print "the plant is more similiar with Mars"


