import pygame

# Define the Box class
class Box:
    def __init__(self, x, y, closed_image_path, open_image_path):
        self.x = x
        self.y = y
        self.closed_image = pygame.image.load(closed_image_path)  # Load the closed image
        self.open_image = pygame.image.load(open_image_path)      # Load the open image
        self.current_image = self.closed_image                   # Set the initial state to closed
        self.rect = self.closed_image.get_rect(topleft=(x, y))   # Define the rectangle
        self.is_open = False                                     # Initial state is closed

    def draw(self, screen):
        screen.blit(self.current_image, (self.x, self.y))

    def toggle(self):
        if self.is_open:
            self.current_image = self.closed_image
            self.is_open = False
        else:
            self.current_image = self.open_image
            self.is_open = True
            




