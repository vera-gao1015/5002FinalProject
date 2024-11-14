import pygame
pygame.init()
#testing
# 设置窗口尺寸
width,height = 1600, 900
pygame.display.set_mode((width,height))
screen = pygame.display.get_surface()
begin = pygame.image.load("picture/begin.png")
begin = pygame.transform.scale(begin,(width,height))
screen.blit(begin,(0,0))

font_button = pygame.font.SysFont("Arial", 40, bold=True)

# 按钮矩形
newgame_button = pygame.Rect(680, 480, 300, 72)  # 按钮位置和大小

homepage_running = True
while homepage_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if newgame_button.collidepoint(event.pos):  # 检查是否点击了“选择玩家角色”按钮
                homepage_running = False  # 退出首页循环，进入角色选择界面


    # 绘制“选择玩家角色”按钮
    pygame.draw.rect(screen, (0, 0, 0), newgame_button.inflate(8, 8))
    pygame.draw.rect(screen, (255, 255, 255), newgame_button)
    button_text = font_button.render("New Game", True, (0, 0, 0))
    screen.blit(button_text, (newgame_button.x + 50, newgame_button.y + 12))

    pygame.display.update()


pygame.display.set_caption("Choose Your Player")
choose = pygame.image.load("picture/choose.png")
choose = pygame.transform.scale(choose,(width,height))

# 加载角色图片
player1_image = pygame.image.load("picture/hero.png")
player2_image = pygame.image.load("picture/hero1.png")
player3_image = pygame.image.load("picture/hero2.png")
player4_image = pygame.image.load("picture/hero3.png")
player5_image = pygame.image.load("picture/hero4.png")

# 缩放图片大小
player1_image = pygame.transform.scale(player1_image, (200, 200))
player2_image = pygame.transform.scale(player2_image, (200, 200))
player3_image = pygame.transform.scale(player3_image, (200, 200))
player4_image = pygame.transform.scale(player4_image, (200, 200))
player5_image = pygame.transform.scale(player5_image, (200, 200))


# 定义角色选择框的矩形
player1_rect = pygame.Rect(250, 250, 200, 200)  # 玩家 1 的位置
player2_rect = pygame.Rect(550, 250, 200, 200)  # 玩家 2 的位置
player3_rect = pygame.Rect(100, 550, 200, 200)  # 玩家 3 的位置
player4_rect = pygame.Rect(400, 550, 200, 200)  # 玩家 4 的位置
player5_rect = pygame.Rect(700, 550, 200, 200)  # 玩家 5 的位置


# 游戏主循环标志
running = True
character_selected = None

# 角色选择界面逻辑
while running:
    screen.blit(choose,(0,0))
    font = pygame.font.SysFont("Arial", 80)
    text = font.render("Choose Your Player", True, (255, 255, 255))
    font1 = pygame.font.SysFont("Arial", 50)
    text1 = font1.render("Siyu", True, (255, 255, 255))
    text2 = font1.render("Vera", True, (255, 255, 255))
    text3 = font1.render("Gloria", True, (255, 255, 255))
    text4 = font1.render("Crystal", True, (255, 255, 255))
    text5 = font1.render("Vivi", True, (255, 255, 255))
    screen.blit(text, (150, 100))  # 显示标题
    screen.blit(text1, (300, 450))  # 显示标题
    screen.blit(text2, (610, 450))  # 显示标题
    screen.blit(text3, (130, 750))  # 显示标题
    screen.blit(text4, (420, 750))  # 显示标题
    screen.blit(text5, (770, 750))  # 显示标题

    # 绘制角色图片
    screen.blit(player1_image, player1_rect)
    screen.blit(player2_image, player2_rect)
    screen.blit(player3_image, player3_rect)
    screen.blit(player4_image, player4_rect)
    screen.blit(player5_image, player5_rect)

    # 绘制边框
    pygame.draw.rect(screen, (255, 255, 255), player1_rect, 5)
    pygame.draw.rect(screen, (255, 255, 255), player2_rect, 5)
    pygame.draw.rect(screen, (255, 255, 255), player3_rect, 5)
    pygame.draw.rect(screen, (255, 255, 255), player4_rect, 5)
    pygame.draw.rect(screen, (255, 255, 255), player5_rect, 5)

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player1_rect.collidepoint(event.pos):  # 判断是否点击玩家 1
                character_selected = "hero"
                running = False  # 退出选择界面
            if player2_rect.collidepoint(event.pos):  # 判断是否点击玩家 2
                character_selected = "hero1"
                running = False
            if player3_rect.collidepoint(event.pos):  # 判断是否点击玩家 3
                character_selected = "hero2"
                running = False
            if player4_rect.collidepoint(event.pos):  # 判断是否点击玩家 2
                character_selected = "hero3"
                running = False
            if player5_rect.collidepoint(event.pos):  # 判断是否点击玩家 2
                character_selected = "hero4"
                running = False

        pygame.display.update()

# 加载选定角色进入游戏
if character_selected == "hero":
    hero_image = player1_image
elif character_selected == "hero1":
    hero_image = player2_image
elif character_selected == "hero2":
    hero_image = player3_image
elif character_selected == "hero3":
    hero_image = player4_image
elif character_selected == "hero4":
    hero_image = player5_image

# 初始化主游戏逻辑

width,height = 1600, 900
pygame.display.set_mode((width,height))
screen = pygame.display.get_surface()

bgpic = pygame.image.load("picture/map.jpg")
bgpic = pygame.transform.scale(bgpic,(width,height))


hero_image = pygame.transform.scale(hero_image, (100, 100))
hero = pygame.sprite.Sprite()
hero.image = hero_image
hero.rect = hero.image.get_rect()
hero.rect.x, hero.rect.y = width / 2, height / 2

player_group = pygame.sprite.Group()
player_group.add(hero)

# 主游戏循环
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

    screen.blit(bgpic,(0,0))
    player_group.draw(screen)

    pygame.display.update()
