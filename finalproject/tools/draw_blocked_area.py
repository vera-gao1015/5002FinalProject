import pygame
import json

def load_blocked_areas(filename):
    filename ="blocked_areas.json"                         # json: key-value pairs, like dictionary
    
    with open(filename, "r") as file:                      # open this file in "read" mode
        data = json.load(file)
    return [pygame.Rect(area["x"], area["y"], area["width"], area["height"]) for area in data]   # top-left corner at (x, y)

def draw_blocked_areas(screen, blocked_areas):              # draw for debug
    for area in blocked_areas:
        pygame.draw.rect(screen, (255, 0, 0), area, 1)      # Red outlines for blocked areas
        
def check_blocked(hero, blocked_areas, new_x, new_y):
    """Check if the new position collides with any blocked areas."""
    new_rect = hero.rect.move(new_x - hero.rect.x, new_y - hero.rect.y)
    for area in blocked_areas:
        if new_rect.colliderect(area):                     # Collision detected
            return True
    return False

def save_blocked_areas_to_file(blocked_areas, filename):
    """
    Save blocked areas to a JSON file.
    Each area is represented as a dictionary with x, y, width, and height.
    """
    data = [{"x": area.x, "y": area.y, "width": area.width, "height": area.height} for area in blocked_areas]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Blocked areas saved to {filename}")
    


def main(path_background_image, file_name_saved):
    # Initialize Pygame
    pygame.init()

    # Screen settings
    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Draw Blocked Area")

    # Load and scale the background image
    background_image = pygame.image.load(path_background_image)
    background_image = pygame.transform.scale(background_image, (width, height))

    # Colors
    blocked_color = (255, 0, 0)  # Red for blocked areas
    temporary_color = (0, 255, 0)  # Green for drawing area (temporary)

    # Blocked areas
    blocked_areas = []
    drawing = False
    temp_rect = None

    clock = pygame.time.Clock()
    running = True

    while running:
        # Draw the background
        screen.blit(background_image, (0, 0))

        # Draw all finalized blocked areas
        for area in blocked_areas:
            pygame.draw.rect(screen, blocked_color, area)

        # Draw the temporary rectangle while dragging
        if temp_rect:
            pygame.draw.rect(screen, temporary_color, temp_rect, 2)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Automatically save blocked areas when quitting
                save_blocked_areas_to_file(blocked_areas,file_name_saved)
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Start drawing a blocked area
                drawing = True
                start_x, start_y = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                # Finalize the blocked area
                if drawing:
                    end_x, end_y = event.pos
                    x = min(start_x, end_x)
                    y = min(start_y, end_y)
                    width = abs(start_x - end_x)
                    height = abs(start_y - end_y)
                    if width > 0 and height > 0:  # Only add valid areas
                        blocked_areas.append(pygame.Rect(x, y, width, height))
                drawing = False
                temp_rect = None

        # Update the temporary rectangle while dragging
        if drawing:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x = min(start_x, mouse_x)
            y = min(start_y, mouse_y)
            width = abs(start_x - mouse_x)
            height = abs(start_y - mouse_y)
            temp_rect = pygame.Rect(x, y, width, height)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    path_background_image="picture/map1.jpg"
    file_name_saved="tools/blocked_areas_map1.json"
    main(path_background_image, file_name_saved)
