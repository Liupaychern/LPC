def bfs(matrix, x, y, k):
    locations = []

    row, col = len(matrix), len(matrix[0])

    # Check if the pixel is of the color z
    z = matrix[x][y]

    # Create a queue for BFS
    queue = []
    queue.append((x, y))

    # Create a visited matrix to keep track of visited pixels
    visited = [[False for _ in range(col)] for _ in range(row)]

    # Create a direction matrix for the 4 directions: left, right, up, down
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while queue:
        x, y = queue.pop(0)
        locations.append((x, y))
        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the pixel is within the matrix
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue

            # Check if the pixel is of the color z
            if matrix[nx][ny] == z and not visited[nx][ny]:
                queue.append((nx, ny))

        print(queue)

    return locations


print("Enter index x, y, k (separated by space):")
x, y, k = input().split()

x = int(x)
y = int(y)
k = int(k)

print("Enter the matrix by multiple lines:")
matrix = []
line = ""
while line != "q":
    line = input()
    if line != "q":
        matrix.append(list(map(int, line.split())))
# print(matrix)

# Replace the element at index (x, y) with k
print(matrix)

# replace the color 𝑧 of the given pixel 〈𝑥,𝑦〉 and all of its adjacent (excluding diagonally adjacent) same colored 𝑧 pixels with the given target color 𝑘.
# The adjacent pixels are the pixels to the left, right, up, and down of the pixel 〈𝑥,𝑦〉
# If the pixel 〈𝑥,𝑦〉 is already of the target color 𝑘, then do nothing.

locations = bfs(matrix, x, y, k)
for x, y in locations:
    matrix[x][y] = k

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()