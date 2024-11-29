import pygame
import game
import game1
import dialogue
import petroom
import chiefroom
import globalv
import battle1
from box import Box


def event(gameversion, gameevent, player, x, y):
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("New Game")
    clock = pygame.time.Clock()

    bgpic = pygame.image.load("picture/map.jpg")
    original_width, original_height = bgpic.get_width(), bgpic.get_height()
    bgpic = pygame.transform.scale(bgpic, (width, height))
    scale_width = width / original_width
    scale_height = height / original_height

    bgpic1 = pygame.image.load("picture/map1.jpg")
    original_width, original_height = bgpic1.get_width(), bgpic1.get_height()
    bgpic1 = pygame.transform.scale(bgpic1, (width, height))
   
    dog = pygame.image.load("picture/dog.ico")
    dog = pygame.transform.scale(dog, (30*scale_width, 30*scale_height))
    dog_rect = dog.get_rect()
    dog_rect.x, dog_rect.y = 270*scale_width, 205*scale_height

    cat = pygame.image.load("picture/cat.png")
    cat = pygame.transform.scale(cat, (40*scale_width, 40*scale_height))
    cat_rect = cat.get_rect()
    cat_rect.x, cat_rect.y = 600*scale_width, 430*scale_height
    
    npc = [{"name": "dog", "image": dog, "rect": dog_rect},
           {"name": "cat", "image": cat, "rect": cat_rect},
            ]
    
    dialogue_blank = pygame.image.load("picture/dialogue_blank.png")
    dialogue_blank = pygame.transform.scale(dialogue_blank, (width-55, 200))
    dialogue_blank_rect = dialogue_blank.get_rect()
    dialogue_blank_rect.x, dialogue_blank_rect.y = 30, 400

    boss = pygame.image.load("picture/boss.png")
    boss = pygame.transform.scale(boss, (150, 150))

    box1 = pygame.image.load("picture/box_open.png")
    box1 = pygame.transform.scale(box1, (100, 100))
    
    address = "picture/" + player + ".png" 
    hero_image = pygame.transform.scale(pygame.image.load(address), (55, 55))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = x, y
    player_group = pygame.sprite.Group()
    player_group.add(hero)

    font1 = pygame.font.SysFont("Arial", 30)
    text1 = font1.render("You have met the monster, please defeat it!", True, (255, 255, 255))
    text2 = font1.render("Press return to the battle……", True, (255, 255, 255))
    text3 = font1.render("Unfortunately, there's nothing in here……", True, (255, 255, 255))
    text4 = font1.render("Press return to the game……", True, (255, 255, 255))
    text5 = font1.render("The box has already opened……", True, (255, 255, 255))

    while True:
        if gameversion == "game":
            screen.blit(bgpic, (0, 0))
            player_group.draw(screen)
            list_coordinates_boxgame = [(35, 520),(1285,100),(1450,760),(790, 500),(360, 200),(1500, 370),(850, 180)]
    
            boxesgame = []
            for box in list_coordinates_boxgame:
                box = Box(box[0], box[1])
                boxesgame.append(box)
            for box in boxesgame:
                box.draw(screen) 
        
            if globalv.flag_dog:
                screen.blit(npc[0]["image"], npc[0]["rect"])
            if globalv.flag_cat:
                screen.blit(npc[1]["image"], npc[1]["rect"])

        elif gameversion == "game1":
            screen.blit(bgpic1, (0, 0))
            player_group.draw(screen)
            list_coordinates_boxgame1 = [(275, 495),(1450,330),(1280,760),(405, 760),(360, 60)]

            boxesgame1 = []
            for box in list_coordinates_boxgame1:
                box = Box(box[0], box[1])
                boxesgame1.append(box)
            for box in boxesgame1:
                box.draw(screen) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        if gameevent == "battle":
            screen.blit(dialogue_blank, dialogue_blank_rect)
            screen.blit(text1, (320, 470))
            screen.blit(text2, (1000, 540))
            screen.blit(boss, (150, 420))

            if keys[pygame.K_RETURN]:
                battle1.battle(player, x, y)
        elif gameevent == "nothing":
            screen.blit(dialogue_blank, dialogue_blank_rect)
            screen.blit(box1, (150, 450))
            screen.blit(text3, (320, 470))
            screen.blit(text4, (1000, 540))
            if keys[pygame.K_RETURN]:
                if gameversion == "game":
                    game.game(player, x, y)
                elif gameversion == "game1":
                    game1.game1(player, x, y)
        elif gameevent == "open":
            screen.blit(dialogue_blank, dialogue_blank_rect)
            screen.blit(box1, (150, 450))
            screen.blit(text5, (320, 470))
            screen.blit(text4, (1000, 540))
            if keys[pygame.K_RETURN]:
                if gameversion == "game":
                    game.game(player, x, y)
                elif gameversion == "game1":
                    game1.game1(player, x, y)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    event("game", "battle", "hero0", 42, 672)