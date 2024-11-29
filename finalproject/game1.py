import pygame
import game
import chooseplayer
import petroom
import globalv
import gameevent
from box import Box

def game1(player, x, y):
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
    hero.rect.x, hero.rect.y = x, y

    player_group = pygame.sprite.Group()
    player_group.add(hero)

    def checkobstacle(x, y):
        # 用于计算一个新的矩形位置，表示原始矩形 (hero.rect) 按照指定的偏移量 (x 和 y) 移动后的结果。
        # 它不会改变原始矩形的位置，而是返回一个新的 pygame.Rect 对象
        new = hero.rect.move(x, y)
        obstacles = [pygame.Rect(2, -26, 77, 667),
                     pygame.Rect(70, 1, 352, 61),
                     pygame.Rect(419, 0, 273, 126),
                     pygame.Rect(871, 0, 716, 124),
                     pygame.Rect(1521, 117, 74, 539),
                     pygame.Rect(899, 609, 435, 47),
                     pygame.Rect(1025, 534, 308, 78),
                     pygame.Rect(960, 572, 106, 51),
                     pygame.Rect(920, 293, 286, 121),
                     pygame.Rect(1292, 462, 237, 58),
                     pygame.Rect(1293, 513, 40, 33),
                     pygame.Rect(1335, 419, 230, 61),
                     pygame.Rect(75, 172, 133, 431),
                     pygame.Rect(183, 250, 136, 234),
                     pygame.Rect(190, 211, 68, 52),
                     pygame.Rect(302, 421, 370, 34),
                     pygame.Rect(466, 444, 203, 70),
                     pygame.Rect(551, 495, 118, 107),
                     pygame.Rect(425, 575, 248, 32),
                     pygame.Rect(7, 573, 324, 32),
                     pygame.Rect(170, 422, 84, 175),
                     pygame.Rect(-5, 768, 91, 140),
                     pygame.Rect(36, 828, 692, 61),
                     pygame.Rect(483, 766, 82, 98),
                     pygame.Rect(872, 765, 377, 124),
                     pygame.Rect(1177, 853, 419, 52),
                     pygame.Rect(1356, 763, 239, 136),
                     pygame.Rect(873, 839, 355, 88),
                     pygame.Rect(1229, 834, 187, 29),
                     pygame.Rect(275, 495, 70, 70),
                     pygame.Rect(1450,330, 70, 70),
                     pygame.Rect(1280,760, 70, 70),
                     pygame.Rect(405, 760, 70, 70),
                     pygame.Rect(360, 60, 70, 70),
                    ]
        for i in obstacles:
            # pygame.draw.rect(screen, (255, 255, 255), i, 5)
            # pygame.display.update()
            if new.colliderect(i):
                return False
        return True
    
    list_coordinates_box = [(275, 495),(1450,330),(1280,760),(405, 760),(360, 60)]
    
    boxes = []
    for box in list_coordinates_box:
        box = Box(box[0], box[1])
        boxes.append(box)
    
    def checkbox():
        #new = hero.rect.move(5, 5)
        for box in boxes:
            if hero.rect.inflate(10, 10).colliderect(box.rect):
                return box
        return None
    
    while True:
        screen.blit(bgpic, (0, 0))
        player_group.draw(screen)
        for box in boxes:
            box.draw(screen)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                  # Interact with the box
                    return_box = checkbox()
                    if return_box:              # Player near the box
                        game_event = return_box.toggle()
                        print(game_event)
                        gameevent.event("game1", game_event, player, hero.rect.x, hero.rect.y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and hero.rect.y + hero.rect.height < height and checkobstacle(0, 5):
            hero.rect.y += 5
        if keys[pygame.K_UP] and hero.rect.y > 0 and checkobstacle(0, -5):
            hero.rect.y -= 5
        if keys[pygame.K_LEFT] and hero.rect.x > 0 and checkobstacle(-5, 0):
            hero.rect.x -= 5
        if keys[pygame.K_RIGHT] and hero.rect.x + hero.rect.width < width and checkobstacle(5, 0):
            hero.rect.x += 5
        if hero.rect.x > 720*scale_width and 460*scale_height < hero.rect.y < 539*scale_height:
            game.game(player, 42, 672)

        if keys[pygame.K_ESCAPE]:
            chooseplayer.chooseplayer()
        if keys[pygame.K_TAB]:
            petroom.petroom("game1", hero.rect.x, hero.rect.y, player)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game1("hero0", 1500, 680)