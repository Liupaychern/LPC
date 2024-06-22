input_vel = input("Input velocity: ")

velocity = float(input_vel)

c = 299702458

p = velocity ** 2/ c ** 2
r = 1/ (1-p) ** 0.5

alpha_td = 4.3
Barnard_td = 6.0
Betelgeuse_td = 309
Andromeda_td = 2000000

per_tp = velocity / c
alpha_tp = alpha_td / r 
Barnard_tp = Barnard_td / r 
Betelgeuse_tp = Betelgeuse_td / r 
Andromeda_tp = Andromeda_td / r 

print("Percentage of light speed = ", per_tp)
print("Travel time to Alpha Centauri = ", alpha_tp)
print("Travel time to Barnard's Star = ", Barnard_tp)
print("Travel time to Betelgeuse (in the Milky Way) = ", Betelgeuse_tp)
print("Travel time to Andromeda Galaxy (closest galaxy) = ", Andromeda_tp)

