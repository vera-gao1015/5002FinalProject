import pygame
import game
import game1
import random
import clueroom
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

    dog = pygame.image.load("picture/dog.png")
    dog = pygame.transform.scale(dog, (45*scale_width, 45*scale_height))
    dog_rect = dog.get_rect()
    dog_rect.x, dog_rect.y = 260*scale_width, 190*scale_height

    cat = pygame.image.load("picture/cat.png")
    cat = pygame.transform.scale(cat, (40*scale_width, 60*scale_height))
    cat_rect = cat.get_rect()
    cat_rect.x, cat_rect.y = 610*scale_width, 430*scale_height
    
    npc = [{"name": "dog", "image": dog, "rect": dog_rect},
           {"name": "cat", "image": cat, "rect": cat_rect},
            ]
    
    dialogue_blank = pygame.image.load("picture/dialogue_blank.png")
    dialogue_blank = pygame.transform.scale(dialogue_blank, (width-55, 220))
    dialogue_blank_rect = dialogue_blank.get_rect()
    dialogue_blank_rect.x, dialogue_blank_rect.y = 30, 400

    boss = pygame.image.load("picture/boss.png")
    boss = pygame.transform.scale(boss, (150, 150))

    box1 = pygame.image.load("picture/box_open.png")
    box1 = pygame.transform.scale(box1, (100, 100))

    question = pygame.image.load("picture/question.png")
    question = pygame.transform.scale(question, (100, 100))

    wrong = pygame.image.load("picture/wrong.png")
    wrong = pygame.transform.scale(wrong, (30, 30))

    right = pygame.image.load("picture/right.png")
    right = pygame.transform.scale(right, (30, 30))

    clue = pygame.image.load("picture/clue.png")
    clue = pygame.transform.scale(clue, (150, 150))
    
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
    text4 = font1.render("Press return to the game / shift to the clue room", True, (255, 255, 255))
    text5 = font1.render("The box has already opened……", True, (255, 255, 255))
    text6 = font1.render("You need to correctly answer the following question to get the clue.", True, (255, 255, 255))
    text7 = font1.render("Press return to the question……", True, (255, 255, 255))
    text8 = font1.render("Please try again……", True, (255, 255, 255))
    text9 = font1.render("You got a new clue!", True, (255, 255, 255))

    Flag_question = False
    answered = False
    correct = False
    question_selected = False
    clue_selected = False

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
                battle1.battle(gameversion, player, x, y)

        elif gameevent == "nothing":
            screen.blit(dialogue_blank, dialogue_blank_rect)
            screen.blit(box1, (150, 450))
            screen.blit(text3, (320, 470))
            screen.blit(text4, (830, 540))
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    clueroom.clueroom(gameversion, player, x, y)
            if keys[pygame.K_RETURN]:
                if gameversion == "game":
                    game.game(player, x, y)
                elif gameversion == "game1":
                    game1.game1(player, x, y)

        elif gameevent == "open":
            screen.blit(dialogue_blank, dialogue_blank_rect)
            screen.blit(box1, (150, 450))
            screen.blit(text5, (320, 470))
            screen.blit(text4, (830, 540))
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    clueroom.clueroom(gameversion, player, x, y)
            if keys[pygame.K_RETURN]:
                if gameversion == "game":
                    game.game(player, x, y)
                elif gameversion == "game1":
                    game1.game1(player, x, y)

        elif gameevent == "question":
            screen.blit(dialogue_blank, dialogue_blank_rect)
            screen.blit(text6, (320, 470))
            screen.blit(text7, (1000, 540))
            screen.blit(question, (150, 450))
            if keys[pygame.K_RETURN]:
                Flag_question = True
            if Flag_question:
                screen.blit(dialogue_blank, dialogue_blank_rect)
                screen.blit(question, (150, 450))

                if not question_selected:
                    question_now = random.choice(globalv.questions)
                    while question_now["state"] == True:
                        question_now = random.choice(globalv.questions)
                    question_selected = True

                text_question = font1.render(question_now["question"], True, (255, 255, 255))
                screen.blit(text_question, (270, 420))
                for i in question_now["options"]:
                    text_option = font1.render(i, True, (255, 255, 255))
                    screen.blit(text_option, (270, 455 + question_now["options"].index(i) * 35))

                if keys[pygame.K_a]:
                    answered = True
                    correct = question_now["answer"] == "A"  
                    press = "A"
                elif keys[pygame.K_b]:
                    answered = True
                    correct = question_now["answer"] == "B"
                    press = "B"
                elif keys[pygame.K_c]:
                    answered = True
                    correct = question_now["answer"] == "C"
                    press = "C"
                elif keys[pygame.K_d]:
                    answered = True
                    correct = question_now["answer"] == "D"
                    press = "D"

                if answered and correct:
                    screen.blit(right, (270, 465 + (ord(press) - ord("A") ) * 35))
                    screen.blit(text4, (830, 560))
                    if not clue_selected:
                        clue_now = random.choice(globalv.question_clues)
                        
                        while clue_now["state"] == True:
                            clue_now = random.choice(globalv.question_clues)
                        clue_selected = True

                        globalv.get_clues.append(clue_now["clue"])
                        print(globalv.get_clues)
                        clue_now["state"] = True
                        print(clue_now)
                    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                        clueroom.clueroom(gameversion, player, x, y)
                    if keys[pygame.K_RETURN]:
                        question_now["state"] = True
                        if gameversion == "game":
                            game.game(player, x, y)
                        elif gameversion == "game1":
                            game1.game1(player, x, y)

                elif answered and not correct:
                    screen.blit(wrong, (270, 455 + (ord(press) - ord("A") ) * 35))
                    screen.blit(text8, (1000, 540))

        elif gameevent == "clue":
            screen.blit(dialogue_blank, dialogue_blank_rect)
            screen.blit(clue, (150, 430))
            screen.blit(text9, (320, 470))
            screen.blit(text4, (830, 560))
            if not clue_selected:
                clue_now = random.choice(globalv.question_clues)
                        
                while clue_now["state"] == True:
                    clue_now = random.choice(globalv.question_clues)
                clue_selected = True

                globalv.get_clues.append(clue_now["clue"])
                print(globalv.get_clues)
                clue_now["state"] = True
                print(clue_now)
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                clueroom.clueroom(gameversion, player, x, y)
            if keys[pygame.K_RETURN]:
                if gameversion == "game":
                    game.game(player, x, y)
                elif gameversion == "game1":
                    game1.game1(player, x, y)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    event("game", "question", "hero0", 42, 672)