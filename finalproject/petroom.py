import pygame
import game
import game1
import globalv

def petroom(gamename, x, y, player):
    pygame.init()
 
    print("pet: ", globalv.get_dog, globalv.get_cat)
    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Pet Room")
    clock = pygame.time.Clock()

    bgpic = pygame.image.load("picture/petroom.png")
    original_width, original_height = bgpic.get_width(), bgpic.get_height()
    bgpic = pygame.transform.scale(bgpic, (width, height))
    scale_width = width / original_width
    scale_height = height / original_height

    dog = pygame.image.load("picture/dog.ico")
    dog = pygame.transform.scale(dog, (160*scale_width, 160*scale_height))
    dog_rect = dog.get_rect()
    dog_rect.x, dog_rect.y = width/2, height/2

    cat = pygame.image.load("picture/cat.png")
    cat = pygame.transform.scale(cat, (150*scale_width, 150*scale_height))
    cat_rect = cat.get_rect()
    cat_rect.x, cat_rect.y = width/2, height/2

    return_font = pygame.font.SysFont("Arial", 40, bold=True)
    return_button = pygame.Rect(1150, 800, 170, 72)
    button_text = return_font.render("Return", True, (0, 0, 0))

    while True:
        screen.blit(bgpic, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), return_button.inflate(8, 8))
        pygame.draw.rect(screen, (255, 255, 255), return_button)
        screen.blit(button_text, (return_button.x + 20, return_button.y + 12))

        if globalv.get_dog:
            screen.blit(dog, dog_rect)
        if globalv.get_cat:
            screen.blit(cat, cat_rect)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(event.pos):
                    if gamename == "game1":
                        game1.game1(player, x, y)
                    elif gamename == "game":
                        game.game(player, x, y)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    petroom("game", 550, 220, "hero0")