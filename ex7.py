from sys import argv
script,first,second=argv
print "The script is called: ",script
print "The first variable is: ",first
print "The second variable is: ",second

r=float(first)
pi=float(second)
l=2*pi*r
print ("the lenth of earth is: %.3f km"%l),(" r= %r ; pi= %r ;"%(r,pi))

s=4*pi*r*r
print "\n\tsurface area(km**2):\t%.3f\n\tlenth(km):      \t%.3f\n\tpi=             \t%r\n\tr=                 \t%r\n"%(s,l,pi,r)








