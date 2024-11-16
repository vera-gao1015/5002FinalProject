import pygame
import random

def show_end_screen(screen, width, height, message, font):
    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Render the message
    text_surface = font.render(message, True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 - 100))
    screen.blit(text_surface, text_rect)

    # Define buttons
    retry_button = pygame.Rect(width // 2 - 150, height // 2, 300, 70)
    quit_button = pygame.Rect(width // 2 - 150, height // 2 + 100, 300, 70)

    # Draw buttons
    pygame.draw.rect(screen, (0, 128, 0), retry_button)  # Green for retry
    pygame.draw.rect(screen, (128, 0, 0), quit_button)  # Red for quit

    # Add text to buttons
    button_font = pygame.font.SysFont("Arial", 30)
    retry_text = button_font.render("Retry", True, (255, 255, 255))
    quit_text = button_font.render("Quit", True, (255, 255, 255))
    screen.blit(retry_text, (retry_button.x + 90, retry_button.y + 20))
    screen.blit(quit_text, (quit_button.x + 100, quit_button.y + 20))

    pygame.display.flip()

    # Wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(event.pos):
                    return "retry"
                elif quit_button.collidepoint(event.pos):
                    return "quit"


def battle(player="hero"):
    pygame.init()  # Initialize all Pygame modules, including fonts

    # File paths for images
    path_bg = "picture/map.jpg"
    path_player_img = f"picture/{player}.png"
    path_monster_img = "picture/hero2.png"

    # Screen dimensions and initialization
    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()

    # Background image
    bgpic = pygame.image.load(path_bg)
    bgpic = pygame.transform.scale(bgpic, (width, height))

    # Load player and monster images
    player_image = pygame.transform.scale(pygame.image.load(path_player_img), (150, 150))
    monster_image = pygame.transform.scale(pygame.image.load(path_monster_img), (150, 150))

    # Player and monster positions
    player_rect = player_image.get_rect()
    player_rect.x, player_rect.y = 100, height - 200

    monster_rect = monster_image.get_rect()
    monster_rect.x, monster_rect.y = width - 250, height - 200

    # Bullets
    player_bullets = []
    monster_bullets = []

    # Health
    player_health = 100
    monster_health = 100

    # Fonts
    font = pygame.font.SysFont("Arial", 40)

    # Shooting state
    can_shoot = True  # Player can shoot initially

    # Game Loop
    clock = pygame.time.Clock()
    running = True
    player_jump = False
    monster_jump = False
    jump_count = 0
    monster_jump_chance = 0.3  # Monster jump probability when attacked

    while running:
        screen.blit(bgpic, (0, 0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:  # Detect when SPACE is released
                if event.key == pygame.K_SPACE:
                    can_shoot = True

        keys = pygame.key.get_pressed()

        # Player controls
        if keys[pygame.K_SPACE] and can_shoot:  # Shoot only if can_shoot is True
            player_bullets.append(pygame.Rect(player_rect.centerx, player_rect.y, 10, 10))
            can_shoot = False  # Reset can_shoot until SPACE is released

        if keys[pygame.K_UP] and not player_jump:  # Jump
            player_jump = True
            jump_count = 20

        # Player Jumping
        if player_jump:
            if jump_count >= -20:
                direction = 1 if jump_count > 0 else -1
                player_rect.y -= (jump_count ** 2) * 0.1 * direction
                jump_count -= 1
            else:
                player_jump = False
                player_rect.y = height - 200

        # Monster random shooting
        if random.randint(1, 50) == 1:  # Random chance to shoot
            monster_bullets.append(pygame.Rect(monster_rect.centerx, monster_rect.y, 10, 10))

        # Monster Jumping to Avoid Bullets
        if any(bullet.colliderect(monster_rect) for bullet in player_bullets) and random.random() < monster_jump_chance:
            monster_jump = True
            jump_count = 20

        if monster_jump:
            if jump_count >= -20:
                direction = 1 if jump_count > 0 else -1
                monster_rect.y -= (jump_count ** 2) * 0.1 * direction
                jump_count -= 1
            else:
                monster_jump = False
                monster_rect.y = height - 200

        # Move Bullets
        for bullet in player_bullets[:]:
            bullet.x += 15
            if bullet.colliderect(monster_rect):  # Hit monster
                player_bullets.remove(bullet)
                monster_health -= 10
            elif bullet.x > width:  # Out of bounds
                player_bullets.remove(bullet)

        for bullet in monster_bullets[:]:
            bullet.x -= 15
            if bullet.colliderect(player_rect):  # Hit player
                monster_bullets.remove(bullet)
                player_health -= 10
            elif bullet.x < 0:  # Out of bounds
                monster_bullets.remove(bullet)

        # Draw bullets
        for bullet in player_bullets:
            pygame.draw.rect(screen, (255, 255, 0), bullet)  # Yellow bullets for player

        for bullet in monster_bullets:
            pygame.draw.rect(screen, (255, 0, 0), bullet)  # Red bullets for monster

        # Draw player and monster
        screen.blit(player_image, player_rect)
        screen.blit(monster_image, monster_rect)

        # Draw health bars
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(50, 50, player_health * 2, 20))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(width - 250, 50, monster_health * 2, 20))

        # Display health text
        player_health_text = font.render(f"Player HP: {player_health}", True, (255, 255, 255))
        monster_health_text = font.render(f"Monster HP: {monster_health}", True, (255, 255, 255))
        screen.blit(player_health_text, (50, 10))
        screen.blit(monster_health_text, (width - 250, 10))

        # Check for win/loss
        if player_health <= 0:
            result = show_end_screen(screen, width, height, "You Lost!", font)
            if result == "retry":
                battle(player)  # Restart the game
            else:
                pygame.quit()
                exit()
        if monster_health <= 0:
            result = show_end_screen(screen, width, height, "You Won!", font)
            if result == "retry":
                battle(player)  # Restart the game
            else:
                pygame.quit()
                exit()

        pygame.display.flip()
        clock.tick(60)

# Entry point
if __name__ == "__main__":
    battle()
