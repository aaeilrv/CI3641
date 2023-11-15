X = 2
Y = 3
Z = 3

a = 2 * X + 3 * Y + 2
b = 4 * Y + 5 * Z + 1
c = 5 * X + 2 * Z + 3
d = (a + b + c) % 7

def misterio(a, b, c, d):
    if c == 0:
        yield a
        for x in misterio(b, a, b, d - 1):
            yield x
    elif d > 0:
        for x in misterio(a, b + 1, c - 1, d):
            yield x

for x in misterio(0, 1, 0, d + 1):
    print(x)