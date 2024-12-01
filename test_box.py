import pygame
from box import Box

# Main function
def testbox():
    pygame.init()

    # Screen settings
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Test Map with Boxes")

    # Load background image
    bgpic = pygame.image.load("picture/map1.jpg")
    bgpic = pygame.transform.scale(bgpic, (width, height))

    # Create a Box object
    box1 = Box(300, 300, "picture/box_close.png", "picture/box_open.png")  # Box 1
    box2 = Box(500, 400, "picture/box_close.png", "picture/box_open.png")  # Box 2

    # Player settings
    player_image = pygame.image.load("picture/hero0.png")  # Load player image
    player_image = pygame.transform.scale(player_image, (50, 50))
    player_rect = player_image.get_rect(topleft=(50, 50))

    # Game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.blit(bgpic, (0, 0))  # Draw background

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Check if the player is near box1 or box2 and toggle
                    if player_rect.colliderect(box1.rect):
                        box1.toggle()
                    if player_rect.colliderect(box2.rect):
                        box2.toggle()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_rect.y -= 5
        if keys[pygame.K_DOWN]:
            player_rect.y += 5
        if keys[pygame.K_LEFT]:
            player_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            player_rect.x += 5

        # Draw boxes and player
        box1.draw(screen)
        box2.draw(screen)
        screen.blit(player_image, player_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    testbox()
