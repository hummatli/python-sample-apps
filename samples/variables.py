# Declare a variable and initialize it
f = 0
print f;

# re-declaring the variable works
f = 'abc'
print f

#concatinate diferent types
#print("salam " + 123) //Gives error
#print"salam " + 123 //Gives error

print "salam " + str(123)


print '-----------------Global Local Vars ----------------'
#Gloabal vs local variables
#gloabal
d = 2
print d

def someFunction():
    global d
    d = "abc"
    print d

someFunction()
print d

del(d)

d = 6
print d
