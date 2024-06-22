import random
# 
with open("grid99.txt", "r") as file:
    file_contents = file.read()
with open("grid77.txt", "r") as file:
    file_contents = file.read()

def generate_path(maze, N, M):
    # Start from the top-left corner
    current_position = (0, 0)
    maze[current_position] = 2  # Mark the starting point as part of the path

    while current_position != (N-1, M-1):  # Continue until reaching the bottom-right corner
        # Decide whether to move right or down
        if current_position[1] < M - 1 and (maze[current_position[0], current_position[1] + 1] == 0 or maze[current_position[0], current_position[1] + 1] == 2):
            # Move right if it's possible and if the cell is empty or already part of the path
            current_position = (current_position[0], current_position[1] + 1)
            maze[current_position] = 2  # Mark the new position as part of the path
        elif current_position[0] < N - 1 and (maze[current_position[0] + 1, current_position[1]] == 0 or maze[current_position[0] + 1, current_position[1]] == 2):
            # Move down if it's possible and if the cell is empty or already part of the path
            current_position = (current_position[0] + 1, current_position[1])
            maze[current_position] = 2  # Mark the new position as part of the path

    return maze

def add_obstacles(maze, min_obstacles, N, M):
    added_obstacles = 0  # Track the number of obstacles added
    
    while added_obstacles < min_obstacles:
        i = random.randint(0, N-1)  # Randomly select row index
        j = random.randint(0, M-1)  # Randomly select column index
        
        # Check if the selected cell is empty
        if maze.get((i, j), 0) == 0:
            maze[(i, j)] = 1  # Set the cell to obstacle
            added_obstacles += 1  # Increment obstacle count
        else:
            print(f"Obstacle already exists at ({i}, {j})")
    
    return maze

def set_obstacle(maze, N, M):
    while True:
        try:
            i = int(input("Enter the row index for the obstacle: "))
            j = int(input("Enter the column index for the obstacle: "))

            # Check if the coordinates are within bounds
            if not (0 <= i < N and 0 <= j < M):
                raise ValueError("Coordinates are out of bounds.")

            # Check if the cell is empty
            if maze.get((i, j), 0) != 0:
                print("Error: Cell is already occupied.")
                continue  # Prompt user again

            # Set the cell as an obstacle
            maze[(i, j)] = 1
            print(f"Obstacle set at position ({i}, {j}).")
            break  # Exit the loop after setting the obstacle

        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyError:
            print("Error: Coordinates must be integers.")

    return maze

def remove_obstacle(maze, N, M):
    while True:
        try:
            i = int(input("Enter the row index for the obstacle to remove: "))
            j = int(input("Enter the column index for the obstacle to remove: "))

            # Check if the coordinates are within bounds
            if not (0 <= i < N and 0 <= j < M):
                raise ValueError("Coordinates are out of bounds.")

            # Check if the cell contains an obstacle
            if maze.get((i, j), 0) != 1:
                print("Error: No obstacle at the specified position.")
                continue  # Prompt user again

            # Remove the obstacle from the cell
            del maze[(i, j)]
            print(f"Obstacle removed from position ({i}, {j}).")
            break  # Exit the loop after removing the obstacle

        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyError:
            print("Error: Coordinates must be integers.")

    return maze

def print_maze(maze, N, M):
    for i in range(N):
        for j in range(M):
            cell = maze.get((i, j), 0)
            if cell == 0:
                print('   ', end='')  # Empty cell
            elif cell == 1:
                print(' X ', end='')  # Obstacle
            elif cell == 2:
                print(' O ', end='')  # Path
        print()  # Move to the next row

def main():
    valid_files = ["grid99.txt", "grid77.txt"]
    
    while True:
        try:
            filename = input("Enter file name : ").strip()
            if filename not in valid_files:
                print("Invalid file name. Please enter 'grid99.txt' or 'grid77.txt'.")
                continue
            
            with open(filename, "r") as file:
                N, M = map(int, file.readline().split())
                break  # Exit loop if file is opened and dimensions are successfully read
        except IOError:
            print("IOError occurred in main function. File not found. Please enter a valid file name.")
        except ValueError:
            print("Error: Unable to load maze dimensions from file. Invalid format or dimensions not found.")

    # Ask user for minimum number of obstacles
    try:
        min_obstacles = int(input("Enter the minimum number of obstacles (0-55): "))
    except ValueError:
        print("ValueError occurred in main function. Invaild number of obstacles.")
        return

    # Generate path
    maze = {(i, j): 0 for i in range(N) for j in range(M)}  # Create a maze filled with empty cells
    maze = generate_path(maze, N, M)

    # Add obstacles
    maze = add_obstacles(maze, min_obstacles, N, M)

    # Main loop
    while True:
        print("\nMenu:")
        print("1. Set obstacle")
        print("2. Remove obstacle")
        print("3. Exit")
        choice = input("Enter your choice : ")

        if choice == '1':
            maze = set_obstacle(maze, N, M)
        elif choice == '2':
            maze = remove_obstacle(maze, N, M)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
