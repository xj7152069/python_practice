def s(pi,r):
    s=4*pi*r**2
    return s
def l(pi,r):
    l=2*pi*r
    return l
pi=3.1415926
a=1
while a!=0:
    r=float(raw_input("please inpue the r: "))
    print "the surfance area is: %.3f"%s(pi,r)
    print "The lenth is: %.3f"%l(pi,r)
    a=float(raw_input("input 0 to quit... "))
    if a!=0:
        print "the calculation is continued...\n"
print "END\n"


