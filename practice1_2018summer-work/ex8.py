from sys import argv
script,filename=argv
text=open(filename,'r')
print "the name of file is: %r"%filename
text.seek(16)
print text.read(3),"\n"
text.close

textname=raw_input("What is the name of file? ")
text=open(textname)
print "the name of file is: %r"%textname
print text.read(),"\n"
text.close

textname=raw_input("What is the name of file you want to write? ")
text=open(textname,'w+')
print "the name of file is: %r"%textname
l1=raw_input("what do you want to input of line1?" )
text.write(l1)
text.write("\n")
lnum=3.14159265358979
l2=str(lnum)
text.write(l2)
text.seek(0,0)
print text.read(),"\n"
text.close
print "\n"

textname=raw_input("What is the name of file you want to add? ")
text=open(textname,'a+')
print text.read()
text.write("\n")
print "the name of file is: %r"%textname
l3=raw_input("what do you want to add of line3?" )
text.write(l3)
text.seek(0,0)
print text.read(),"\n"
text.close
