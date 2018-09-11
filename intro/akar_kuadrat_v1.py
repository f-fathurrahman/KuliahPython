from math import sqrt

a = 1.0
b = 4.0
c = -38.0

D = b**2 - 4*a*c

print("D = ", D)

x1 = ( -b + sqrt(D) )/(2*a)
x2 = ( -b - sqrt(D) )/(2*a)

print("x1 = {}".format(x1))
print("x2 = {}".format(x2))

print("x1 = {:18.10f}".format(x1))
print("x2 = {:18.10f}".format(x2))

print("x1 = %18.10f" % x1)
print("x2 = %18.10f" % x2)


