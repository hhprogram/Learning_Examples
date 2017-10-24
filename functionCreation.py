class A():
    def __init__(self, id):
        self.a = 10
        self.id = id

def makeFunction(arg):
    def _func(indicator):
        if indicator:
            if arg.id == "A":
                print("A")
            elif arg.id == 'b':
                print("b")
            arg.a = 5
        else:
            if arg.id == "A":
                print("A")
            elif arg.id == 'b':
                print("b")
            arg.a = 15
    return _func

a = A("A")
b = A("b")
func_list = [a,b]
funcs = {}
for i in range(2):
    funcs[i] = makeFunction(func_list[i])

funcs[0](True)
print(a.a)
funcs[1](False)
print(b.a)
