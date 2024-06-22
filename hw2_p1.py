#problem 1-1

s1 = "spam"
s2 = "ni!"

#a
a = "The Knights who say,"
b = a + s2
print(b)

#b
a = 3 * s1
b = 2 * s2
c = a + b 
print(c)

#c
print(s1[1])

#d
print(s1[1:3])

#e
print(s1[2]+ s2[:2])

#f
print(s1+s2[-1])

#g
print(s2[len(s2)//2])

#problem 1-2
#a
new_s2 = s2.replace("ni!", "NI")
print(new_s2)

#b
new_s2 = s2 + s1 + s2
print(new_s2)

#c
a = s2.replace("n", "N")
new_s2 = (s1 + a + ' ') * 3
print(new_s2)

#d
new_s1 = s1.replace("m", "n")
print(new_s1)

#e
new_s1 = s1[0:2] + s1[3:]
print(new_s1)

#problem1-4
#a
x = 5
y = 3
if x >= y:
	x = x - 2
print(x)

#b
tc = 100
tf = (9/5) * tc +32
print(tf)

#c
x = 0
while x < 5:
	x = x + 1
print(x)

#d
x = 1
i = 1
while x <= 5:
	x = x * i
	i = i +1
	print(x)

#e
x = 0
while x < 6:
	if x % 2 == 0:
		print('even', x)
	else:
		print('odd', x)
	x = x + 1

#f
i = 0 
while i < 6:
	j = 0
	while j < i:
		print("*")
		j = i + 1
	i = i + 1
	print()

#g
score = 40
while score > 1:
	score = (score / 2) - 1
print(score)
