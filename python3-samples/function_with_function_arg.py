def func1(a):
    print("Inside arg funct {}".format(a))

def func5(func, t):
    print("inside complex fun")
    func(t)


func5(func1, 2)