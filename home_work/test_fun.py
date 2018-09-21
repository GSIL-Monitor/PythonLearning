


def test_fun():
    temp = [lambda x: x * i for i in range(4)]
    return temp


for el in test_fun():
    print(el(2))



def test_fun1():
    temp = [lambda x,i=i:x * i for i in range(4)]
    return temp


for el in test_fun1():
    print(el(2))
