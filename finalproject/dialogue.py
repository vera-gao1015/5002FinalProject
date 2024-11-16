import pygame
import game
import globalv

def dialogue(player, x, y, npcname):
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
    
    dialogue_dog = pygame.image.load("picture/dialogue_dog.png")
    dialogue_dog = pygame.transform.scale(dialogue_dog, (width-55, 200))
    dialogue_dog_rect = dialogue_dog.get_rect()
    dialogue_dog_rect.x, dialogue_dog_rect.y = 30, 400

    dialogue_cat = pygame.image.load("picture/dialogue_cat.png")
    dialogue_cat = pygame.transform.scale(dialogue_cat, (width-55, 200))
    dialogue_cat_rect = dialogue_cat.get_rect()
    dialogue_cat_rect.x, dialogue_cat_rect.y = 30, 400

    dialogue_blank = pygame.image.load("picture/dialogue_blank.png")
    dialogue_blank = pygame.transform.scale(dialogue_blank, (width-55, 200))
    dialogue_blank_rect = dialogue_dog.get_rect()
    dialogue_blank_rect.x, dialogue_blank_rect.y = 30, 400

    address = "picture/" + player + ".png" 
    hero_image = pygame.transform.scale(pygame.image.load(address), (55, 55))
    hero = pygame.sprite.Sprite()
    hero.image = hero_image
    hero.rect = hero.image.get_rect()
    hero.rect.x, hero.rect.y = x, y

    player_group = pygame.sprite.Group()
    player_group.add(hero)

    player_name = ["Siyu", "Vera", "Gloria", "Crystal", "Vivi"]
    font1 = pygame.font.SysFont("Arial", 30)

    dialogue_index = 0  # 初始化对话索引
    dialogues_dog = [
        ["Hi "+ player_name[int(player[-1])] +",", "I'm the little dog from Brave Village. You're the first warrior to come here, ", "and I've been waiting for you for so long! ", "Our village chief has gone missing. Can you help me find him?"],
        ["Oh, poor village, what happened here? ", "When did the village chief go missing?"],
        ["It was about a month ago.", "The village chief went out and never came back.", "I've heard that things have been restless around here lately,", "with monsters showing up frequently……"],
        ["Monsters? Perfect, I've been looking for a challenge. ", "Let me help you!"],
        ["Thank you so much! Take me with you! ", "I know this area really well, and I have some surprising abilities!"],
        ["OK! Let's go!"],
        ["Wait, let’s check out the village chief’s house first!"]
    ]
    dialogues_cat = [
        ["Hi "+ player_name[int(player[-1])] +",", "I'm the little cat from Brave Village. You're the first warrior to come here, ", "and I've been waiting for you for so long! ", "Our village chief has gone missing. Can you help me find him?"],
        ["Oh, poor village, what happened here? ", "When did the village chief go missing?"],
        ["It was about a month ago.", "The village chief went out and never came back.", "I've heard that things have been restless around here lately,", "with monsters showing up frequently……"],
        ["Monsters? Perfect, I've been looking for a challenge. ", "Let me help you!"],
        ["Thank you so much! Take me with you! ", "I know this area really well, and I have some surprising abilities!"],
        ["OK! Let's go!"],
        ["Wait, let’s check out the village chief’s house first!"]
    ]
    text4 = font1.render("You're not the one I'm looking for……", True, (255, 255, 255))
 

    while True:
        screen.blit(bgpic, (0, 0))
        player_group.draw(screen)

        if globalv.flag_dog:
            screen.blit(npc[0]["image"], npc[0]["rect"])
        if globalv.flag_cat:
            screen.blit(npc[1]["image"], npc[1]["rect"])

        if npcname == "dog":
            flag = True
            if dialogue_index % 2 == 0 and flag:
                screen.blit(dialogue_dog, dialogue_dog_rect)
            elif dialogue_index % 2 != 0 and flag:
                screen.blit(dialogue_blank, dialogue_blank_rect)
                newhero = pygame.transform.scale(hero.image, (150, 150))
                screen.blit(newhero, (150, 420))
        
            dialogue_now = dialogues_dog[dialogue_index]  # 获取当前对话
            for i in range(len(dialogue_now)):  # 遍历当前对话的每一行
                text = font1.render(dialogue_now[i], True, (255, 255, 255))  # 将每一行渲染为文本
              
                if player[-1] == "0" or player[-1] == "3" or player[-1] == "4":
                    screen.blit(text, (320, 425 + i * 40))
                    flag = True
                else:
                    flag =False
                    screen.blit(dialogue_dog, dialogue_dog_rect)
                    screen.blit(text4, (320, 490))
                    break
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    if not flag:
                        globalv.flag_dog = False
                        print(globalv.flag_dog, globalv.flag_cat)
                        game.game(player, x-10, y-10, globalv.flag_dog, globalv.flag_cat)
                    else:
                        dialogue_index += 1
                        if dialogue_index >= len(dialogues_dog): 
                            globalv.flag_dog = False 
                            print(globalv.flag_dog, globalv.flag_cat)
                            game.game(player, x-10, y-10, globalv.flag_dog, globalv.flag_cat)
        
        elif npcname == "cat":
            flag = True
            if dialogue_index % 2 == 0 and flag:
                screen.blit(dialogue_cat, dialogue_cat_rect)
            elif dialogue_index % 2 != 0 and flag:
                screen.blit(dialogue_blank, dialogue_blank_rect)
                newhero = pygame.transform.scale(hero.image, (150, 150))
                screen.blit(newhero, (150, 420))
        
            dialogue_now = dialogues_cat[dialogue_index]  # 获取当前对话
            for i in range(len(dialogue_now)):  # 遍历当前对话的每一行
                text = font1.render(dialogue_now[i], True, (255, 255, 255))  # 将每一行渲染为文本
              
                if player[-1] == "1" or player[-1] == "2":
                    screen.blit(text, (320, 425 + i * 40))
                    flag = True
                else:
                    flag =False
                    screen.blit(dialogue_cat, dialogue_cat_rect)
                    screen.blit(text4, (320, 490))
                    break

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    if not flag:
                        globalv.flag_cat = False
                        print(globalv.flag_dog, globalv.flag_cat)
                        game.game(player, x-10, y,globalv.flag_dog, globalv.flag_cat)
                        
                    else:
                        dialogue_index += 1
                        if dialogue_index >= len(dialogues_cat):
                            globalv.flag_cat = False 
                            print(globalv.flag_dog, globalv.flag_cat) 
                            game.game(player, x-10, y-10,globalv.flag_dog, globalv.flag_cat)
                            
        
        pygame.display.update()
        clock.tick(40)

if __name__ == "__main__":
    dialogue("hero0",550,220,"dog")