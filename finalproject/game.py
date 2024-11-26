import pygame
from box import Box
import chooseplayer
import game1_with_blocked_area as game1
import dialogue
import petroom
import chiefroom
import globalv


list_coordinates_box = [
    (827, 340),
    (1460, 190),
    (1302,830),
    (430, 780),
    (400, 160) 
    
]



def game(player, x, y):
    path_box_closed = "picture/box_close.png"
    path_box_open = "picture/box_open.png"
    
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
    # print(scale_width, scale_height)
    dog = pygame.image.load("picture/dog.ico")
    dog = pygame.transform.scale(dog, (30*scale_width, 30*scale_height))
    dog_rect = dog.get_rect()
    dog_rect.x, dog_rect.y = 270*scale_width, 205*scale_height

    cat = pygame.image.load("picture/cat.png")
    cat = pygame.transform.scale(cat, (40*scale_width, 40*scale_height))
    cat_rect = cat.get_rect()
    cat_rect.x, cat_rect.y = 600*scale_width, 430*scale_height

    # Create a box on the map
    list_boxes = [Box(coords[0], coords[1], path_box_closed, path_box_open) for coords in list_coordinates_box]
    
    
    
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
    
    # Font for displaying coordinates
    font = pygame.font.SysFont("Arial", 24, bold=True)




    player_group = pygame.sprite.Group()
    player_group.add(hero)

    def checknpc(x, y):
        new = hero.rect.move(x, y)
        for i in npc:
            # pygame.draw.rect(screen, (255, 255, 255), i["rect"], 5)
            # pygame.display.update()
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
                    ]
        for i in obstacles:
            # pygame.draw.rect(screen, (255, 255, 255), i, 5)
            # pygame.display.update()
            if new.colliderect(i):
                return False
        return True
            
    while True: 
        screen.blit(bgpic, (0, 0))
        # Draw all boxes
        for box in list_boxes:
            box.draw(screen)  
        player_group.draw(screen)
        
        
        # Display player coordinates
        grid_x, grid_y = hero.rect.x, hero.rect.y
        coordinates_text = f"({grid_x}, {grid_y})"
        text_surface = font.render(coordinates_text, True, (255, 255, 255))  # White text
        text_x = hero.rect.x + (hero.rect.width - text_surface.get_width()) // 2
        text_y = hero.rect.y - text_surface.get_height() - 5  # Position above the player
        screen.blit(text_surface, (text_x, text_y))
        
        if globalv.flag_dog:
            screen.blit(npc[0]["image"], npc[0]["rect"])
        if globalv.flag_cat:
            screen.blit(npc[1]["image"], npc[1]["rect"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                  # Interact with the box
                    for box in list_boxes:
                        if hero.rect.colliderect(box.rect):              # Player near the box
                            box.toggle()

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
            
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game("hero0",42, 672)