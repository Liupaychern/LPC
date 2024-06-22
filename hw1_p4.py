input_height = input("Input the height of the 1st ball: ")
input_m1 = input("Input the mass of the 1st ball: ")
input_m2 = input("Input the mass of the 2nd ball: ")


height = float(input_height)
m1 = float(input_m1)
m2 = float(input_m2)

g = 9.8


U1 = m1 * g * height
u1 = (2 * g * height) ** 0.5
u2 = 0


v2 = ((2 * m1 * u1) + (m2 - m1) * u2) / (m1 + m2)



print("Input the height of the 1st ball: ", height)
print("Input the mass of the 1st ball: ", m1)
print("Input the mass of the 2nd ball: ", m2)
print("The velocity of the 1st ball after slide: ", u1)
print("The velocity of the 2nd ball after collision: ", v2)






