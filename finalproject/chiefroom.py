import pygame
import game

def chiefroom(x, y, player):
    pygame.init()
 
    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Chief Room")
    clock = pygame.time.Clock()

    bgpic = pygame.image.load("picture/chiefroom.png")
    original_width, original_height = bgpic.get_width(), bgpic.get_height()
    bgpic = pygame.transform.scale(bgpic, (width, height))

    address = "picture/" + player + ".png" 
    hero_image = pygame.transform.scale(pygame.image.load(address), (150, 150))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = 782, 700
    player_group = pygame.sprite.Group()
    player_group.add(hero)

    def checkdoor(x, y):
        new = hero.rect.move(x, y)
        door = pygame.Rect(690, 850, 240, 70)
        if new.colliderect(door):
            return True
        return False
    
    def checkobstacle(x, y):
        # 用于计算一个新的矩形位置，表示原始矩形 (hero.rect) 按照指定的偏移量 (x 和 y) 移动后的结果。
        # 它不会改变原始矩形的位置，而是返回一个新的 pygame.Rect 对象
        
        new = hero.rect.move(x, y)
        obstacles = [pygame.Rect(300, 760, 1100, 100),
                     pygame.Rect(500, 673, 750, 80),
                     pygame.Rect(600, 565, 600, 119),
                     pygame.Rect(826, 550, 176, 80),
                    ]

        for i in obstacles:
            if new.colliderect(i):
                return True
        return False

    while True:
        screen.blit(bgpic, (0, 0))
        player_group.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and hero.rect.y + hero.rect.height < height and checkobstacle(0, 5):
            hero.rect.y += 5
        if keys[pygame.K_UP] and hero.rect.y > 0 and checkobstacle(0, -5):
            hero.rect.y -= 5
        if keys[pygame.K_LEFT] and hero.rect.x > 0 and checkobstacle(-5, 0):
            hero.rect.x -= 5
        if keys[pygame.K_RIGHT] and hero.rect.x + hero.rect.width < width and checkobstacle(5, 0):
            hero.rect.x += 5
        if checkdoor(5, 0) and checkdoor(0, 5) and checkdoor(-5, 0) and checkdoor(0, -5):
            game.game(player, x , y - 10)



        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    chiefroom(475, 220, "hero0")