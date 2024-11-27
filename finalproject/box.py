import pygame

# Define the Box class
class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.closed_image = pygame.image.load("picture/box_close.png")  # Load the closed image
        self.open_image = pygame.image.load("picture/box_open.png")      # Load the open image
        self.closed_image = pygame.transform.scale(self.closed_image, (70, 70))
        self.open_image = pygame.transform.scale(self.open_image, (70, 70))
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
            




