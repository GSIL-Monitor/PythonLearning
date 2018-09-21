
a = [1, 2, 3]
c = [4, 5, 6]
d = ['', 3, None]
b = []
b = a + c + d

# print(a)
print(len(''))
# print(b)


def retNone(a):
    if a is None or len(str(a)) == 0:
        return None
    else:
        return a


def setNone(a):
    return [retNone(x) for x in a]


print(b)

print(setNone(b))
