import pygame
import chooseplayer
import game1
import dialogue
import petroom
import chiefroom
import globalv
from box import Box
import gameevent 
import clueroom

def game(player, x, y):
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
    
    dog = pygame.image.load("picture/dog.png")
    dog = pygame.transform.scale(dog, (45*scale_width, 45*scale_height))
    dog_rect = dog.get_rect()
    dog_rect.x, dog_rect.y = 260*scale_width, 190*scale_height

    cat = pygame.image.load("picture/cat.png")
    cat = pygame.transform.scale(cat, (40*scale_width, 60*scale_height))
    cat_rect = cat.get_rect()
    cat_rect.x, cat_rect.y = 600*scale_width, 430*scale_height

    npc = [{"name": "dog", "image": dog, "rect": dog_rect},
           {"name": "cat", "image": cat, "rect": cat_rect},
           {"name": "chiefroom", "image": None, "rect": (206*scale_width, 213*scale_height, 60*scale_width, 45*scale_height)},
            ]

    address = "picture/" + player + ".png" 
    hero_image = pygame.transform.scale(pygame.image.load(address), (55, 55))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = x, y
    player_group = pygame.sprite.Group()
    player_group.add(hero)

    tornado = pygame.image.load("picture/tornado.png")
    tornado = pygame.transform.scale(tornado, (150, 120))

    dialogue_blank = pygame.image.load("picture/dialogue_blank.png")
    dialogue_blank = pygame.transform.scale(dialogue_blank, (width-55, 220))

    font1 = pygame.font.SysFont("Arial", 30)
    text1 = font1.render("It seems something has appeared at the far left of the road...", True, (255, 255, 255))

    def checknpc(x, y):
        new = hero.rect.move(x, y)
        for i in npc:
            if new.colliderect(i["rect"]):
                if i["name"] == "dog":
                    return "dog"
                if i["name"] == "cat":
                    return "cat"
                if i["name"] == "chiefroom":
                    return "chiefroom"
        return False
    
    def checkobstacle(x, y):
        # 用于计算一个新的矩形位置，表示原始矩形 (hero.rect) 按照指定的偏移量 (x 和 y) 移动后的结果。
        # 它不会改变原始矩形的位置，而是返回一个新的 pygame.Rect 对象
        new = hero.rect.move(x, y)
        obstacles = [pygame.Rect(10*scale_width, 10*scale_height, 187*scale_width, 391*scale_height),
                     pygame.Rect((187+10)*scale_width, 10*scale_height, 189*scale_width, 73*scale_height),
                     pygame.Rect((187+189+10)*scale_width, 10*scale_height, 113*scale_width, 37*scale_height),
                     pygame.Rect((187+93+143+127+10)*scale_width, 10*scale_height, 178*scale_width, 112*scale_height),
                     pygame.Rect((187+93+143+127+10)*scale_width, (112+52+10)*scale_height, 45*scale_width, 110*scale_height),
                     pygame.Rect((187+93+143+295+10)*scale_width, 112*scale_height, 25*scale_width, 52*scale_height),
                     pygame.Rect((187+93+143+295+10)*scale_width, (112+80+10)*scale_height, 25*scale_width, 52*scale_height),
                     pygame.Rect((187+93+143+127+42+10)*scale_width, (112+210+10)*scale_height, 146*scale_width, 210*scale_height),
                     pygame.Rect((187+93+143+295+10)*scale_width, (391+145+10)*scale_height, 25*scale_width, 52*scale_height),
                     pygame.Rect((177+10)*scale_width, (391+145+52+10)*scale_height, 495*scale_width, 38*scale_height),
                     pygame.Rect((177+115+10)*scale_width, (391+145+10)*scale_height, 40*scale_width, 52*scale_height),
                     pygame.Rect(10*scale_width, (391+145+10)*scale_height, 177*scale_width, 81*scale_height),
                     pygame.Rect((140+10)*scale_width, (391+10)*scale_height, 183*scale_width, 45*scale_height),
                     pygame.Rect((187+10)*scale_width, (391-73+20)*scale_height, 136*scale_width, 73*scale_height),
                     pygame.Rect((187+136+42+10)*scale_width, (391-73+20)*scale_height, 116*scale_width, 128*scale_height),
                     pygame.Rect((187+136+42+42+10)*scale_width, (73+67+81+20)*scale_height, 40*scale_width, 52*scale_height),
                     pygame.Rect((187+51+10)*scale_width, (73+67+81+10)*scale_height, 85*scale_width, 60*scale_height),
                     pygame.Rect((187+93+10)*scale_width, (73+67+10)*scale_height, 143*scale_width, 81*scale_height),
                     pygame.Rect(35, 520, 70, 70),
                     pygame.Rect(1285,100, 70, 70),
                     pygame.Rect(1450,760, 70, 70),
                     pygame.Rect(790, 500, 70, 70),
                     pygame.Rect(360, 200, 70, 70),
                     pygame.Rect(1500, 370, 70, 70),
                     pygame.Rect(850, 180, 70, 70),
                    ]
        for i in obstacles:
            if new.colliderect(i):
                return False
        return True

    def checkbox():
        for box in boxes:
            if hero.rect.inflate(10, 10).colliderect(box.rect):
                return box
        return None
            
    while True:
        screen.blit(bgpic, (0, 0))
        player_group.draw(screen)
        list_coordinates_box = [(35, 520),(1285,120),(1450,760),(790, 500),(360, 200),(1500, 370),(850, 180)]
    
        boxes = []
        for box in list_coordinates_box:
            box = Box(box[0], box[1])
            boxes.append(box)
        for box in boxes:
            box.draw(screen) 
        
        if globalv.flag_dog:
            screen.blit(npc[0]["image"], npc[0]["rect"])
        if globalv.flag_cat:
            screen.blit(npc[1]["image"], npc[1]["rect"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                 
                    return_box = checkbox()
                    if return_box:             
                        game_event = return_box.toggle()
                        print(game_event)
                        gameevent.event("game", game_event, player, hero.rect.x, hero.rect.y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and hero.rect.y + hero.rect.height < height and checkobstacle(0, 5):
            hero.rect.y += 5
        if keys[pygame.K_UP] and hero.rect.y > 0 and checkobstacle(0, -5):
            hero.rect.y -= 5
        if keys[pygame.K_LEFT] and hero.rect.x > 0 and checkobstacle(-5, 0):
            hero.rect.x -= 5
        if keys[pygame.K_RIGHT] and hero.rect.x + hero.rect.width < width and checkobstacle(5, 0):
            hero.rect.x += 5
        if hero.rect.x < 10*scale_width and 460*scale_height < hero.rect.y < 539*scale_height:
            game1.game1(player, 1500, 680)
        if globalv.flag_dog:
            if (checknpc(0, 5)=="dog") or (checknpc(0, -5)=="dog") or (checknpc(5, 0)=="dog") or (checknpc(-5, 0)=="dog"):  
                dialogue.dialogue(player, hero.rect.x, hero.rect.y, "dog")
        if globalv.flag_cat:    
            if (checknpc(0, 5)=="cat") or (checknpc(0, -5)=="cat") or (checknpc(5, 0)=="cat") or (checknpc(-5, 0)=="cat"):
                dialogue.dialogue(player, hero.rect.x, hero.rect.y, "cat")
        if (checknpc(0, 5)=="chiefroom") or (checknpc(0, -5)=="chiefroom") or (checknpc(5, 0)=="chiefroom") or (checknpc(-5, 0)=="chiefroom"):  
                chiefroom.chiefroom(480, 220, player)
        if keys[pygame.K_ESCAPE]:
            chooseplayer.chooseplayer()
        if keys[pygame.K_TAB]:
            petroom.petroom("game", hero.rect.x, hero.rect.y, player)
        if keys[pygame.K_LSHIFT]:
            clueroom.clueroom("game", player, hero.rect.x, hero.rect.y)
        
        if globalv.box_count == 12 and globalv.flag_see:
            screen.blit(dialogue_blank, (30, 400))
            screen.blit(tornado, (150, 450))
            screen.blit(text1, (350, 490))
            if keys[pygame.K_DOWN] or keys[pygame.K_UP] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                globalv.flag_see = False
            
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game("hero0",42, 672)