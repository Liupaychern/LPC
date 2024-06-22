year = int(input("Please input Year: "))
month = int(input("Please input Month: "))

while m ==2:
	if y % 4 == 0 and y % 100 == 0 or y % 400 == 0:
		days = 28
	else:
		days = 29
print("Sun, Mon, Tue, Wed, Thu, Fri, Sat")