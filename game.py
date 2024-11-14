import pygame
import chooseplayer

def game(player):
    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()

    bgpic = pygame.image.load("picture/map.jpg")
    bgpic = pygame.transform.scale(bgpic, (width, height))

    address = "picture/" + player + ".png" 
    hero_image = pygame.transform.scale(pygame.image.load(address), (100, 100))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = width / 2, height / 2

    player_group = pygame.sprite.Group()
    player_group.add(hero)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and hero.rect.y + hero.rect.height < height:
            hero.rect.y += 10
        if keys[pygame.K_UP] and hero.rect.y > 0:
            hero.rect.y -= 10
        if keys[pygame.K_LEFT] and hero.rect.x > 0:
            hero.rect.x -= 10
        if keys[pygame.K_RIGHT] and hero.rect.x + hero.rect.width < width:
            hero.rect.x += 10

        screen.blit(bgpic, (0, 0))
        player_group.draw(screen)

        pygame.display.update()

if __name__ == "__main__":
    player = chooseplayer.chooseplayer()
    game(player)