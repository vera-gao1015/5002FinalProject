import pygame
import game
import chooseplayer
import petroom
import globalv


blocked_cells = {
    (12, 4), (15, 21), (23, 4), (7, 17), (34, 1), (16, 29), (36, 7), (27, 4), (28, 3),(31, 29), (28, 12), (2, 2), (5, 19), (30, 18), (6, 2), (29, 4),
    (21, 0), (26, 14), (7, 10), (33, 29), (6, 20), (4, 2), (34, 3), (36, 0), (16, 31), (22, 10), (36, 9), (3, 6), (31, 22), (8, 2), (36, 18), 
    (12, 18), (14, 15), (28, 14), (12, 27), (23, 27), (5, 21), (11, 16), (24, 10), (10, 20), (24, 19), (15, 16), (21, 2), (7, 12), (10, 29), (13, 28), 
    (25, 27), (7, 21), (22, 3), (36, 2), (31, 15), (36, 11), (29, 27), (22, 21), (36, 20), (12, 20), (23, 20), (30, 4), (15, 0), (33, 15), (13, 21), (15, 18), 
    (7, 14), (1, 28), (36, 4), (27, 1), (28, 0), (22, 14), (36, 13), (29, 29), (5, 7), (23, 22), (1, 3), (15, 2), (32, 18), (27, 22), (10, 15), (25, 4), 
    (24, 14), (32, 27), (16, 1), (1, 21), (25, 22), (7, 16), (34, 0), (2, 29),(36, 6), (29, 22), (31, 19), (34, 18), (28, 2), (12, 15), (6, 29), (5, 9), 
    (28, 11), (21, 27), (11, 4), (14, 21), (3, 21), (5, 18), (4, 29), (36, 27), (1, 5), (15, 4), (26, 4), (8, 29), (7, 9), (30, 29), (33, 28), (35, 15), 
    (34, 2), (16, 30), (21, 11), (5, 2), (31, 21), (28, 4), (22, 27), (21, 29), (32, 4), (2, 6), (30, 22), (7, 2), (35, 18), (11, 18), (7, 11), (0, 27), 
    (11, 27), (34, 4), (22, 2), (21, 13), (26, 27), (23, 10), (4, 6), (21, 22), (9, 2), (12, 19), (22, 20), (21, 31), (27, 10), (10, 3), (36, 22), (27, 19), 
    (8, 15), (28, 27), (25, 10), (10, 21), (11, 20), (25, 19), (11, 29), (22, 4), (15, 20), (6, 17), (31, 16), (29, 19), (15, 29), (12, 21), (27, 3), (36, 15), 
    (34, 27), (13, 4), (1, 2), (24, 4), (30, 17), (28, 29), (0, 22), (32, 29), (26, 22), (3, 2), (31, 18), (23, 14), (36, 8), (27, 14), (28, 13), (1, 4), 
    (5, 20), (28, 22), (33, 18), (30, 19), (11, 15), (5, 29), (25, 14), (16, 2), (2, 21), (21, 1), (15, 15), (13, 27), (24, 27), (14, 4), (6, 21), (7, 20),
    (35, 27), (31, 20), (36, 1), (21, 10), (7, 29), (21, 28), (36, 10), (4, 21), (36, 19), (1, 6), (11, 17), (32, 15), (9, 29), (31, 4), (24, 20), (15, 17), 
    (7, 13), (1, 27), (13, 29), (21, 12), (36, 3), (27, 0), (21, 30), (34, 15), (36, 12), (22, 22), (10, 2), (36, 21), (33, 4), (27, 27), (15, 1), (11, 28), 
    (26, 10), (24, 22), (15, 19), (26, 19), (7, 15), (1, 29), (21, 14), (4, 7), (36, 5), (27, 2), (28, 1), (36, 14), (5, 8), (28, 10), (10, 4), (5, 17), 
    (30, 16), (28, 19), (9, 15), (3, 29), (14, 29),(28, 28), (11, 21), (15, 3), (13, 15), (6, 9), (33, 27), (1, 22)}
cell_size = 20

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
    # scale_width = width / original_width
    # scale_height = height / original_height

    address = "picture/" + player + ".png" 
    hero_image = pygame.transform.scale(pygame.image.load(address), (55, 55))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = x, y

    player_group = pygame.sprite.Group()
    player_group.add(hero)

    def checkblocked(x, y):
        """检查目标位置是否在阻挡单元格中"""
        grid_x = int(x // cell_size)  # transfer 网络坐标
        grid_y = int(y // cell_size)  
        return (grid_x, grid_y) not in blocked_cells
    
    # def checkobstacle(x, y):
    #     # 用于计算一个新的矩形位置，表示原始矩形 (hero.rect) 按照指定的偏移量 (x 和 y) 移动后的结果。
    #     # 它不会改变原始矩形的位置，而是返回一个新的 pygame.Rect 对象
    #     new = hero.rect.move(x, y)
    #     obstacles = [pygame.Rect(10*scale_width, 10*scale_height, 187*scale_width, 391*scale_height)
    #                 ]
    #     for i in obstacles:
    #         # pygame.draw.rect(screen, (255, 255, 255), i, 5)
    #         # pygame.display.update()
    #         if new.colliderect(i):
    #             return False
    #     return True
 
            
    while True:
        screen.blit(bgpic, (0, 0))
        player_group.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_DOWN] and hero.rect.y + hero.rect.height < height and checkblocked(hero.rect.x, hero.rect.y + 5):
            hero.rect.y += 5
        if keys[pygame.K_UP] and hero.rect.y > 0 and checkblocked(hero.rect.x, hero.rect.y - 5):
            hero.rect.y -= 5
        if keys[pygame.K_LEFT] and hero.rect.x > 0 and checkblocked(hero.rect.x - 5, hero.rect.y):
            hero.rect.x -= 5
        if keys[pygame.K_RIGHT] and hero.rect.x + hero.rect.width < width and checkblocked(hero.rect.x + 5, hero.rect.y):
            hero.rect.x += 5
            
        if hero.rect.x > 720 and 460 < hero.rect.y < 539:
            game.game(player, 42, 672)
            
        # if hero.rect.x > 720*scale_width and 460*scale_height < hero.rect.y < 539*scale_height:
            game.game(player, 42, 672)

        if keys[pygame.K_ESCAPE]:
            chooseplayer.chooseplayer()
        if keys[pygame.K_TAB]:
            petroom.petroom("game1", hero.rect.x, hero.rect.y, player)
        pygame.display.update()
        clock.tick(60)
    
    
    print(f"Checking grid position: ({grid_x}, {grid_y})")

if __name__ == "__main__":
    game1("hero0", 1500, 680)