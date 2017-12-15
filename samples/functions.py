def func1():
    print("I am a function")
    print "dfd"

print func1()
print func1


def func2(arg1, arg2):
    print arg1, " ", arg2

func2(1, 2)

def cube(x):
    return x*x*x 

print cube(3)


print "power ---------------"
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print power(2)
print power(2, 2)
print power(x = 2, num = 5)
print power(num = 5)

print "function with variable number of arguments  ----------"
def multi_add(*arg):
    result = 0
    for x in arg:
        result = result + x
    return result

print multi_add(1, 6, 3, 5)