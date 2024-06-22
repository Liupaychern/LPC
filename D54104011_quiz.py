import curses
import random
import time

# Define constants
SCREEN_HEIGHT = 20
SCREEN_WIDTH = 80
SNAKE_LENGTH = 3
SNAKE_HEAD = "O"
SNAKE_BODY = "o"
FOOD = "π"
SPECIAL_FOOD = "X"
OBSTACLE = "#"

# Function to generate obstacles
def generate_obstacles():
    obstacles = []
    num_obstacles = (SCREEN_HEIGHT * SCREEN_WIDTH) // 20  # About 5% of the screen
    for _ in range(num_obstacles):
        if random.choice([True, False]):
            start_x = random.randint(1, SCREEN_HEIGHT - 6)
            start_y = random.randint(1, SCREEN_WIDTH - 2)
            for i in range(5):
                obstacles.append([start_x + i, start_y])
        else:
            start_x = random.randint(1, SCREEN_HEIGHT - 2)
            start_y = random.randint(1, SCREEN_WIDTH - 6)
            for i in range(5):
                obstacles.append([start_x, start_y + i])
    return obstacles

# Function to initialize the screen
def init_screen():
    screen = curses.initscr()
    curses.curs_set(0)
    screen.keypad(1)
    screen.timeout(100)
    return screen

# Function to draw the game screen
def draw_screen(screen, snake, food, special_food, obstacles, score, special_food_eaten):
    screen.clear()
    sh, sw = screen.getmaxyx()

    for y, x in snake:
        screen.addch(y, x, SNAKE_HEAD if [y, x] == snake[0] else SNAKE_BODY)

    screen.addch(food[0], food[1], FOOD)

    if special_food:
        screen.addch(special_food[0], special_food[1], SPECIAL_FOOD)

    for oy, ox in obstacles:
        screen.addch(oy, ox, OBSTACLE)

    screen.addstr(0, 2, f"Score: {score}  Special Food Eaten: {special_food_eaten}")
    screen.refresh()

# Main game function
def main(screen):
    sh, sw = screen.getmaxyx()

    snake = [[sh // 2, sw // 2 + i] for i in range(SNAKE_LENGTH)]
    food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
    special_food = None
    obstacles = generate_obstacles()
    score = 0
    special_food_eaten = 0
    key = curses.KEY_RIGHT
    paused = False

    while True:
        next_key = screen.getch()
        if next_key != -1:
            key = next_key

        if key == ord('p'):
            paused = not paused
            continue

        if paused:
            continue

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN or key == ord('s'):
            new_head[0] += 1
        if key == curses.KEY_UP or key == ord('w'):
            new_head[0] -= 1
        if key == curses.KEY_LEFT or key == ord('a'):
            new_head[1] -= 1
        if key == curses.KEY_RIGHT or key == ord('d'):
            new_head[1] += 1

        # Wrap around screen boundaries
        new_head[0] = (new_head[0] + sh) % sh
        new_head[1] = (new_head[1] + sw) % sw

        if new_head in snake or new_head in obstacles:
            break

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            food = None
            while not food:
                nf = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
                food = nf if nf not in snake and nf not in obstacles else None

            if score % 5 == 0 and not special_food:
                while not special_food:
                    sf = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
                    special_food = sf if sf not in snake and sf not in obstacles else None
        elif special_food and new_head == special_food:
            special_food = None
            if len(snake) > 1:
                snake.pop()
                special_food_eaten += 1
        else:
            snake.pop()

        draw_screen(screen, snake, food, special_food, obstacles, score, special_food_eaten)
        time.sleep(0.1)

    screen.clear()
    screen.addstr(sh // 2, sw // 2 - len("Game Over!") // 2, "Game Over!")
    screen.addstr(sh // 2 + 1, sw // 2 - len(f"Score: {score}  Special Food Eaten: {special_food_eaten}") // 2, f"Score: {score}  Special Food Eaten: {special_food_eaten}")
    screen.refresh()
    time.sleep(3)

    # Wait for any key press to exit
    screen.getch()

curses.wrapper(main)
