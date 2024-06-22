# n = int(input("Enter the size of the grid: "))
# matrix = [["_" for i in range(n)] for j in range(n)]

# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=" ")
#     print()

# while True:
#     cell_coordinates = input("Enter the cell coordinates to edit: ") 
#     if cell_coordinates == "done":
#         break

#     row, col = cell_coordinates.split(",")  
#     row, col = int(row), int(col)
#     new_value = input("Enter the new value for the cell: ")
#     matrix[row][col] = new_value

#     for i in range(n):
#         print(" ".join(matrix[i]))





n = int(input("Enter the size of the grid: "))
matrix = [["_" for i in range(n)] for j in range(n)]

for i in range(n):
	for j in range(n):
		print(matrix[i][j], end = " ")
	print()

while True:
	cell_coordinates = input("Enter the cell coordinates to edit: ")
	if cell_coordinates == "done":
		break

	col,row = cell_coordinates.split(",")
	col,row = int(col), int(row)
	new_value = input("Enter the new value for the cell: ")
	matrix[col][row] = new_value

	for i in range(n):
		for j in range(n):
			print(matrix[i][j], end = " ")
		print()
