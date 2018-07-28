def p1():
    print "hello world"
def p2(x):
    print "I like %r"%x
def p3(x1,x2):
    print "I like %r and %r"%(x1,x2)

p1()
p2("pi")
p3("pi","2pi")

def add(a,b):
    c=a+b
    return c
    
d=add(23,1)
print(d)



