import pygame
import globalv
import ending
import random

def battle(gameversion, player, x, y):
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Final Battle")
    clock = pygame.time.Clock()

    bgpic = pygame.image.load("picture/battle_bg.jpg")
    bgpic = pygame.transform.scale(bgpic, (width, height))

    boss = pygame.image.load("picture/dragon.png")
    boss = pygame.transform.scale(boss, (300, 300))
    boss_rect = boss.get_rect()
    boss_rect.x, boss_rect.y = 1200, 580

    playerbullet = pygame.image.load("picture/bullet.png")
    playerbullet = pygame.transform.scale(playerbullet, (50, 50))
    playerbullet_rect = playerbullet.get_rect()
    player_bullet = []

    bossbullet = pygame.image.load("picture/bullet.png")
    bossbullet = pygame.transform.scale(bossbullet, (50, 50))
    bossbullet_rect = bossbullet.get_rect()
    boss_bullet = []

    dog = pygame.image.load("picture/dog.ico")
    dog = pygame.transform.scale(dog, (100, 100))
    dog_rect = dog.get_rect()
    dog_rect.x, dog_rect.y = 750, 680

    cat = pygame.image.load("picture/cat.png")
    cat = pygame.transform.scale(cat, (100, 100))
    cat_rect = cat.get_rect()
    cat_rect.x, cat_rect.y = 750, 680

    address = "picture/" + player + ".png" 
    hero_image = pygame.transform.scale(pygame.image.load(address), (150, 150))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = 50, 700
    player_group = pygame.sprite.Group()
    player_group.add(hero)

    player_health = 100
    boss_health = 100
    flag_shoot = True
    flag_jump = False
    jump = 0
    flag_win = False

    while True:
        screen.blit(bgpic, (0, 0))
        screen.blit(boss, boss_rect)
        player_group.draw(screen)

        font = pygame.font.SysFont("Arial", 40, bold=True)
        text1 = font.render(str(player_health), True, (255, 255, 255))
        text2 = font.render(str(boss_health), True, (255, 255, 255))
        screen.blit(text1, (hero.rect.x - 40, hero.rect.y - 35)) 
        screen.blit(text2, (boss_rect.x - 50, boss_rect.y - 35)) 

        pygame.draw.rect(screen, (0, 255, 0), (hero.rect.x + 30, hero.rect.y - 20, player_health * 1.5, 10))  # Green health bar for player
        pygame.draw.rect(screen, (255, 0, 0), (boss_rect.x + 20, boss_rect.y - 20, boss_health * 1.5, 10))  # Red health bar for monster

        if globalv.get_dog:
            screen.blit(dog, dog_rect)
        if globalv.get_cat:
            screen.blit(cat, cat_rect)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flag_win:
                    if return_button.collidepoint(event.pos):
                        ending.ending()

                if try_button.collidepoint(event.pos):
                    battle(gameversion, player, x, y)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not flag_jump:
            flag_jump = True
            jump = 20
        
        if flag_jump:
            if jump >= -20:
                if jump > 0:
                    hero.rect.y -= jump
                else:
                    hero.rect.y -= jump
                jump -= 1
            else:
                flag_jump = False
                hero.rect.y = 700


        if keys[pygame.K_LEFT] and hero.rect.x > 0:
            hero.rect.x -= 5
        if keys[pygame.K_RIGHT] and hero.rect.x + hero.rect.width < 700:
            hero.rect.x += 5

        if keys[pygame.K_SPACE] and flag_shoot:
            playerbullet_rect.x, playerbullet_rect.y = hero.rect.x, hero.rect.y + 50
            player_bullet.append(playerbullet_rect)
            flag_shoot = False
        
        if not keys[pygame.K_SPACE]:
            flag_shoot = True
        
        if random.randint(0, 25) == 5:
            bossbullet_rect.x, bossbullet_rect.y = boss_rect.x, boss_rect.y + 120
            boss_bullet.append(bossbullet_rect)
        
        for bullet in player_bullet:
            screen.blit(playerbullet, bullet)

        for bullet in boss_bullet:
            screen.blit(bossbullet, bullet)

        for bullet in player_bullet[:]:
            bullet.x += 10
            if bullet.colliderect(boss_rect): 
                player_bullet.remove(bullet)
                boss_health -= 5
            elif bullet.x > width:  
                player_bullet.remove(bullet)

        for bullet in boss_bullet[:]:
            bullet.x -= 10
            if bullet.colliderect(hero.rect):  
                boss_bullet.remove(bullet)
                player_health -= 5
            elif bullet.x < 0:  
                boss_bullet.remove(bullet)
        
        if player_health <= 0:
            screen.fill((0, 0, 0))
            lose = pygame.image.load("picture/lose.jpg")
            lose = pygame.transform.scale(lose, (1000, 500))
            screen.blit(lose, (320, 25))

            text4 = font.render("Try again", True, (0, 0, 0))
            try_button = pygame.Rect(680, 500, 300, 72)
            pygame.draw.rect(screen, (0, 0, 0), try_button.inflate(8, 8))
            pygame.draw.rect(screen, (255, 255, 255), try_button)
            screen.blit(text4, (try_button.x + 55, try_button.y + 12))

        
        if boss_health <= 90:
            flag_win = True
            screen.fill((0, 0, 0))
            win = pygame.image.load("picture/win.jpg")
            win = pygame.transform.scale(win, (1000, 500))
            screen.blit(win, (320, 25))
            text5 = font.render("Return", True, (0, 0, 0))
            return_button = pygame.Rect(680, 500, 300, 72)
            pygame.draw.rect(screen, (0, 0, 0), return_button.inflate(8, 8))
            pygame.draw.rect(screen, (255, 255, 255), return_button)
            screen.blit(text5, (return_button.x + 80, return_button.y + 12))

            if globalv.get_dog:
                screen.blit(dog, (30, 700))
            if globalv.get_cat:
                screen.blit(cat, (30, 700))
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    battle("game", "hero0", 50, 700)