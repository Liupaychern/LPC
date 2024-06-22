n = int(input("Input the range number: "))
i = 2

while i < n:
	k = 1
	sum = 0
	while k < i:
		if i % k == 0:
			sum += k
		k += 1
	if sum == i:
		print("Perfect numbers:", i)
    i+=1
    