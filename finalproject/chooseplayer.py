import pygame
import game
import globalv

def chooseplayer():
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Choose Your Player")
    choose = pygame.image.load("picture/choose.png")
    choose = pygame.transform.scale(choose, (width, height))

    player1_image = pygame.image.load("picture/hero0.png")
    player2_image = pygame.image.load("picture/hero1.png")
    player3_image = pygame.image.load("picture/hero2.png")
    player4_image = pygame.image.load("picture/hero3.png")
    player5_image = pygame.image.load("picture/hero4.png")

    player_image = [player1_image, player2_image, player3_image, player4_image, player5_image]
    
    player1_rect = pygame.Rect(250, 250, 200, 200)  
    player2_rect = pygame.Rect(550, 250, 200, 200)  
    player3_rect = pygame.Rect(100, 550, 200, 200)  
    player4_rect = pygame.Rect(400, 550, 200, 200)  
    player5_rect = pygame.Rect(700, 550, 200, 200)  

    player_rect = [player1_rect, player2_rect, player3_rect, player4_rect, player5_rect]
    
    font = pygame.font.SysFont("Arial", 80)
    text = font.render("Choose Your Player", True, (255, 255, 255))
    font1 = pygame.font.SysFont("Arial", 50)
    text1 = font1.render("Siyu", True, (255, 255, 255))
    text2 = font1.render("Vera", True, (255, 255, 255))
    text3 = font1.render("Gloria", True, (255, 255, 255))
    text4 = font1.render("Crystal", True, (255, 255, 255))
    text5 = font1.render("Vivi", True, (255, 255, 255))
    
    globalv.flag_dog = True
    globalv.flag_cat = True
    globalv.get_dog = False
    globalv.get_cat = False

    while True:
        screen.blit(choose,(0, 0))
        screen.blit(text, (150, 100))  
        screen.blit(text1, (300, 450)) 
        screen.blit(text2, (610, 450))  
        screen.blit(text3, (130, 750))  
        screen.blit(text4, (420, 750))  
        screen.blit(text5, (770, 750))  

        for i in range(len(player_image)):
            screen.blit(player_image[i], player_rect[i])

        for i in player_rect:
            pygame.draw.rect(screen, (255, 255, 255), i, 5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            for i in range(len(player_rect)):
                if player_rect[i].collidepoint(pygame.mouse.get_pos()):
                    player_image[i] = pygame.transform.scale(player_image[i], (205, 205))
                else:
                    player_image[i] = pygame.transform.scale(player_image[i], (200, 200))
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(player_rect)):
                    if player_rect[i].collidepoint(event.pos):
                        player = "hero" + str(i)
                        game.game(player, 42, 672)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    chooseplayer()