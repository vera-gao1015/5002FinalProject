import pygame
import sys

# Initialize Pygame
pygame.init()

# Map and cell settings
cell_size = 20  # Size of each cell

# Load the background image
background_image = pygame.image.load("picture/map.jpg")
map_width, map_height = background_image.get_size()
screen_width = map_width
screen_height = map_height

# Scale cell size to fit the map
grid_width = map_width // cell_size
grid_height = map_height // cell_size

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Map Editor with Background")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Map array: 1 for walkable, 0 for blocked
game_map = [[1] * grid_width for _ in range(grid_height)]
blocked_cells = set()

# Draw the background image and grid overlay
def draw_background():
    screen.blit(background_image, (0, 0))

def draw_grid():
    for y in range(grid_height):
        for x in range(grid_width):
            if game_map[y][x] == 0:
                pygame.draw.rect(screen, RED, (x * cell_size, y * cell_size, cell_size, cell_size), 0)
            pygame.draw.rect(screen, BLACK, (x * cell_size, y * cell_size, cell_size, cell_size), 1)

# Toggle cell status for drawing with mouse drag
def toggle_cell(x, y):
    if 0 <= x < grid_width and 0 <= y < grid_height:
        if game_map[y][x] == 1:  # If cell is walkable, block it
            game_map[y][x] = 0
            blocked_cells.add((x, y))  # Use set to avoid duplicates

# Main loop
running = True
drawing = False  # Track if the mouse is held down

while running:
    draw_background()  # Draw background image
    draw_grid()  # Draw grid overlay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Start drawing when the mouse is clicked
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Stop drawing when the mouse is released
            drawing = False

    # Draw while mouse is held down
    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid_x, grid_y = mouse_x // cell_size, mouse_y // cell_size
        toggle_cell(grid_x, grid_y)

    pygame.display.flip()

# Print blocked cells when exiting
print("Blocked cells:", list(blocked_cells))

pygame.quit()
sys.exit()
