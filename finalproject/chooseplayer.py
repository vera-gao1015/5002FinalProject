import pygame
import game

def chooseplayer():
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Choose Your Player")
    choose = pygame.image.load("picture/choose.png")
    choose = pygame.transform.scale(choose, (width, height))

    player1_image = pygame.image.load("picture/hero.png")
    player2_image = pygame.image.load("picture/hero1.png")
    player3_image = pygame.image.load("picture/hero2.png")
    player4_image = pygame.image.load("picture/hero3.png")
    player5_image = pygame.image.load("picture/hero4.png")

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

    running = True

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
                    player = "hero"
                    running = False  # 退出选择界面
                if player2_rect.collidepoint(event.pos):  # 判断是否点击玩家 2
                    player = "hero1"
                    running = False
                if player3_rect.collidepoint(event.pos):  # 判断是否点击玩家 3
                    player = "hero2"
                    running = False
                if player4_rect.collidepoint(event.pos):  # 判断是否点击玩家 2
                    player = "hero3"
                    running = False
                if player5_rect.collidepoint(event.pos):  # 判断是否点击玩家 2
                    player = "hero4"
                    running = False

        pygame.display.update()
        clock.tick(40)
    game.game(player)

if __name__ == "__main__":
    chooseplayer()