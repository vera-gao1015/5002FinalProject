import pygame
import json
import game
import chooseplayer
import petroom
from tools.draw_blocked_area import check_blocked, load_blocked_areas, draw_blocked_areas
from box import Box  # Import the Box class

list_coordinates_box = [
    (285, 495),
    (1460,380),
    (1220,800),
    (445, 800),
    (390, 90) 
    
]

def game1(player, x, y):
    path_blocked_areas = 'tools/blocked_areas_map1.json'
    path_bg = "picture/map1.jpg"
    path_hero = f"picture/{player}.png"
    path_box_closed = "picture/box_close.png"
    path_box_open = "picture/box_open.png"
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("New Game")
    clock = pygame.time.Clock()

    # Load background and player image
    bgpic = pygame.image.load(path_bg)
    bgpic = pygame.transform.scale(bgpic, (width, height))
    
    # Create a box on the map
    list_boxes = [Box(coords[0], coords[1], path_box_closed, path_box_open) for coords in list_coordinates_box]
    
    # Create the hero on the map
    hero_image = pygame.transform.scale(pygame.image.load(path_hero), (55, 55))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = x, y

    # Font for displaying coordinates
    font = pygame.font.SysFont("Arial", 24, bold=True)



    # Load blocked areas
    blocked_areas = load_blocked_areas(path_blocked_areas)

    player_group = pygame.sprite.Group()
    player_group.add(hero)

    while True:
        screen.blit(bgpic, (0, 0))  # Draw background
       
        # Draw all boxes
        for box in list_boxes:
            box.draw(screen)  
        player_group.draw(screen)  # Draw player

        # Display player coordinates
        grid_x, grid_y = hero.rect.x, hero.rect.y
        coordinates_text = f"({grid_x}, {grid_y})"
        text_surface = font.render(coordinates_text, True, (255, 255, 255))  # White text
        text_x = hero.rect.x + (hero.rect.width - text_surface.get_width()) // 2
        text_y = hero.rect.y - text_surface.get_height() - 5  # Position above the player
        screen.blit(text_surface, (text_x, text_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                  # Interact with the box
                    for box in list_boxes:
                         
                        if hero.rect.colliderect(box.rect):              # Player near the box
                            box.toggle()

        keys = pygame.key.get_pressed()

        # Player movement
        move_step = 5
        if keys[pygame.K_DOWN] and hero.rect.bottom < height and not check_blocked(hero, blocked_areas, hero.rect.x, hero.rect.y + move_step):
            hero.rect.y += move_step
        if keys[pygame.K_UP] and hero.rect.top > 0 and not check_blocked(hero, blocked_areas, hero.rect.x, hero.rect.y - move_step):
            hero.rect.y -= move_step
        if keys[pygame.K_LEFT] and hero.rect.left > 0 and not check_blocked(hero, blocked_areas, hero.rect.x - move_step, hero.rect.y):
            hero.rect.x -= move_step
        if keys[pygame.K_RIGHT] and hero.rect.right < width and not check_blocked(hero, blocked_areas, hero.rect.x + move_step, hero.rect.y):
            hero.rect.x += move_step

        # Map transition (example placeholder)
        if hero.rect.x > 1520 and 660 < hero.rect.y < 705:
            print(hero.rect.x, hero.rect.y)
            game.game(player, 42, 672)

        # Other game features
        if keys[pygame.K_ESCAPE]:
            chooseplayer.chooseplayer()
        if keys[pygame.K_TAB]:
            petroom.petroom("game1", hero.rect.x, hero.rect.y, player)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    game1("hero0", 1500, 680)
