#problem1-1
#a
result = 4.0 / 10.0 + 3.5 * 2
print(type(result))

#b
result = 10 % 4 + 6 / 2
print(type(result))

#c
result = (6.5 - 5.0) ** (0.5) + 7*3
print(type(result))

#d
result = 3 * 10/ 3 + 10 % 3
print(type(result))

#e is invalid, 因為分母＝0

#problem 1-2
#a
print(12 / 6.0)

#b
print(21 // 10)

#c
print(25 // 10.0)

#problem1-3
a = 2
b = 5
c = 2
q = b*b - 4*a*c
q_sr = q ** (1/2)
x1 = (-b + q_sr) / 2*a
x2 = (-b - q_sr) / 2*a
print (x1, x2)