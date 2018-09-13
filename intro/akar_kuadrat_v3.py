from cmath import sqrt

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

print("x1 = {:18.10f} + {:18.10f}j".format(x1.real, x1.imag))
print("x2 = {:18.10f} + {:18.10f}j".format(x2.real, x2.imag))

print("x1 = %18.10f + %18.10fj" % (x1.real, x1.imag))
print("x2 = %18.10f + %18.10fj" % (x2.real, x2.imag))


