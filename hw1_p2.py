#constant
G = 6.67 * 10 ** -11
c = 299792458

#input
force = float(input("Input the force: "))
m1 = float(input("Input the mass of m1: "))
r = float(input("Input the distance: "))

m2 = (force / (G * m1)) * r ** 2
E = m2 * c ** 2

print("The mass of m2 = ", m2)
print("The energy of m2 = ", E)