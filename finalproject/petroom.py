import pygame
import game
import game1
import globalv

def petroom(gameversion, x, y, player):
    pygame.init()
 
    print("pet: ", globalv.get_dog, globalv.get_cat)
    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Pet Room")
    clock = pygame.time.Clock()

    bgpic = pygame.image.load("finalproject/picture/petroom.png")
    original_width, original_height = bgpic.get_width(), bgpic.get_height()
    bgpic = pygame.transform.scale(bgpic, (width, height))
    scale_width = width / original_width
    scale_height = height / original_height

    dog = pygame.image.load("finalproject/picture/dog.png")
    dog = pygame.transform.scale(dog, (250*scale_width, 250*scale_height))
    dog_rect = dog.get_rect()
    dog_rect.x, dog_rect.y = width/2, height/2

    cat = pygame.image.load("finalproject/picture/cat.png")
    cat = pygame.transform.scale(cat, (300*scale_width, 300*scale_height))
    cat_rect = cat.get_rect()
    cat_rect.x, cat_rect.y = width/2, height/2

    while True:
        screen.blit(bgpic, (0, 0))

        if globalv.get_dog:
            screen.blit(dog, dog_rect)
        if globalv.get_cat:
            screen.blit(cat, cat_rect)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if gameversion == "game1":
                game1.game1(player, x, y)
            elif gameversion == "game":
                game.game(player, x, y)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    petroom("game", 550, 200, "hero0")