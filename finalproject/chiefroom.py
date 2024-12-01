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
    bgpic = pygame.transform.scale(bgpic, (width, height))

    address = "picture/" + player + ".png" 
    hero_image = pygame.transform.scale(pygame.image.load(address), (150, 150))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = 782, 700
    player_group = pygame.sprite.Group()
    player_group.add(hero)

    dialogue_blank = pygame.image.load("picture/dialogue_blank.png")
    dialogue_blank = pygame.transform.scale(dialogue_blank, (width-55, 220))

    house = pygame.image.load("picture/house.png")
    house = pygame.transform.scale(house, (150, 150))

    clue = pygame.image.load("picture/clue.png")
    clue = pygame.transform.scale(clue, (150, 150))

    font1 = pygame.font.SysFont("Arial", 30)
    text1 = font1.render("Look around, there might be some clues...", True, (255, 255, 255))
    text2 = font1.render("On the table lies a letter that reads, 'A dragon has appeared in the village.'", True, (255, 255, 255))
    flag_enter = True

    def checkdoor(x, y):
        new = hero.rect.move(x, y)
        door = pygame.Rect(690, 850, 240, 70)
        if new.colliderect(door):
            return True
        return False
    
    def checkobstacle(x, y): 
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
    
    def checkdesk(x, y):
        new = hero.rect.move(x, y)
        desk = pygame.Rect(0, 380, 550, 333)
        if new.colliderect(desk):
            return True
        return False
    

    while True:
        screen.blit(bgpic, (0, 0))
        player_group.draw(screen)

        if flag_enter:
            screen.blit(dialogue_blank, (30, 400))
            screen.blit(house, (200, 430))
            screen.blit(text1, (500, 490))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and hero.rect.y + hero.rect.height < height and checkobstacle(0, 5):
            flag_enter = False
            hero.rect.y += 5
        if keys[pygame.K_UP] and hero.rect.y > 0 and checkobstacle(0, -5):
            flag_enter = False
            hero.rect.y -= 5
        if keys[pygame.K_LEFT] and hero.rect.x > 0 and checkobstacle(-5, 0):
            flag_enter = False
            hero.rect.x -= 5
        if keys[pygame.K_RIGHT] and hero.rect.x + hero.rect.width < width and checkobstacle(5, 0):
            flag_enter = False
            hero.rect.x += 5
        if checkdoor(5, 0) and checkdoor(0, 5) and checkdoor(-5, 0) and checkdoor(0, -5):
            game.game(player, x , y - 10)
        if checkdesk(5, 0) and checkdesk(0, 5) and checkdesk(-5, 0) and checkdesk(0, -5):
            screen.blit(dialogue_blank, (30, 400))
            screen.blit(clue, (150, 430))
            screen.blit(text2, (350, 490))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    chiefroom(475, 220, "hero0")