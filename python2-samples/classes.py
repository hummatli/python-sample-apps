#initial class
print "Initial class ----------------"
class myClass():
    x = 0
    def method1(self):
        print "myClass method1   x=" + str(self.x)

    def method2(self, someString):
        print "myClass method2:" + someString


c = myClass()
c.method1()
c.method2("This is arg String")


#extended class
print "Extended class ---------"

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print "anotherClass method1"

    def method2(self):
        print "anotherClass method2:"


c2 = anotherClass()
c2.method1()