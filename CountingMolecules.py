import numpy

c, h, o = [int(x) for x in input().split()]
a = [[0, 2, 1], [1, 0, 1], [6, 12, 6]]
b = [c, h, o]
x = numpy.linalg.solve(a, b)
print(x)