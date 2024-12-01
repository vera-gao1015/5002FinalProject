import pygame
import begin
from box import Box

def ending():
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Happy Ending")
    clock = pygame.time.Clock()

    bgpic = pygame.image.load("picture/map1.jpg")
    bgpic = pygame.transform.scale(bgpic, (width, height))

    tornado = pygame.image.load("picture/tornado.png")
    tornado = pygame.transform.scale(tornado, (150, 120))

    chief = pygame.image.load("picture/chief.png")
    chief = pygame.transform.scale(chief, (170, 170))

    dialogue_blank = pygame.image.load("picture/dialogue_blank.png")
    dialogue_blank = pygame.transform.scale(dialogue_blank, (width-55, 300))

    font1 = pygame.font.SysFont("Arial", 30)
    text1 = font1.render("Congratulations! You defeated the dragon and rescued the village chief!", True, (255, 255, 255))
    text2 = font1.render("The village chief and villagers gave you an ancient letter about a hidden treasure.", True, (255, 255, 255))
    text3 = font1.render("At dawn, you set off on a new adventure, ready for unknown challenges……", True, (255, 255, 255))
    text4 = font1.render("Press 'ESC' to the begin page……", True, (255, 255, 255))
    list_coordinates_box = [(275, 495),(1450,330),(1280,760),(405, 760),(360, 60)]
    
    boxes = []
    for box in list_coordinates_box:
        box = Box(box[0], box[1])
        boxes.append(box)
    
    while True:
        screen.blit(bgpic, (0, 0))

        for box in boxes:
            box.draw(screen)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            begin.begin()

        screen.blit(dialogue_blank, (30, 350))
        screen.blit(chief, (150, 400))
        screen.blit(text1, (320, 390))
        screen.blit(text2, (320, 450))
        screen.blit(text3, (320, 490))
        screen.blit(text4, (1000, 570))
                    
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    ending()