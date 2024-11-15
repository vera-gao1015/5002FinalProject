import pygame
import game

def game1(player):
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("New Game")
    clock = pygame.time.Clock()

    bgpic = pygame.image.load("picture/map1.jpg")
    original_width, original_height = bgpic.get_width(), bgpic.get_height()
    bgpic = pygame.transform.scale(bgpic, (width, height))
    
    scale_width = width / original_width
    scale_height = height / original_height

    address = "picture/" + player + ".png" 
    hero_image = pygame.transform.scale(pygame.image.load(address), (55, 55))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = 710*scale_width, 480*scale_height

    player_group = pygame.sprite.Group()
    player_group.add(hero)
    def checkobstacle(x, y):
        # 用于计算一个新的矩形位置，表示原始矩形 (hero.rect) 按照指定的偏移量 (x 和 y) 移动后的结果。
        # 它不会改变原始矩形的位置，而是返回一个新的 pygame.Rect 对象
        new = hero.rect.move(x, y)
        obstacles = [pygame.Rect(10*scale_width, 10*scale_height, 187*scale_width, 391*scale_height)
                    ]
        for i in obstacles:
            # pygame.draw.rect(screen, (255, 255, 255), i, 5)
            # pygame.display.update()
            if new.colliderect(i):
                return False
        return True
 
            
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and hero.rect.y + hero.rect.height < height and checkobstacle(0, 10):
            hero.rect.y += 10
        if keys[pygame.K_UP] and hero.rect.y > 0 and checkobstacle(0, -10):
            hero.rect.y -= 10
        if keys[pygame.K_LEFT] and hero.rect.x > 0 and checkobstacle(-10, 0):
            hero.rect.x -= 10
        if keys[pygame.K_RIGHT] and hero.rect.x + hero.rect.width < width and checkobstacle(10, 0):
            hero.rect.x += 10
        if hero.rect.x > 720*scale_width and 460*scale_height < hero.rect.y < 539*scale_height:
            game.game(player)
        screen.blit(bgpic, (0, 0))
        player_group.draw(screen)

        pygame.display.update()
        clock.tick(40)

if __name__ == "__main__":
    game1("hero")