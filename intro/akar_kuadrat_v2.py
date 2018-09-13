from math import sqrt

a = float( input("Masukkan nilai a = ") )
b = float( input("Masukkan nilai b = ") )
c = float( input("Masukkan nilai c = ") )

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


