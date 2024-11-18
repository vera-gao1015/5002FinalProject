import pygame
import chooseplayer

def begin():
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Begin")
    clock = pygame.time.Clock()
    begin = pygame.image.load("picture/begin.png")
    begin = pygame.transform.scale(begin, (width, height))
    

    newgame_font = pygame.font.SysFont("Arial", 40, bold=True)
    newgame_button = pygame.Rect(680, 480, 300, 72)
    button_text = newgame_font.render("New Game", True, (0, 0, 0))
    
    while True:
        screen.blit(begin, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), newgame_button.inflate(8, 8))
        pygame.draw.rect(screen, (255, 255, 255), newgame_button)
        screen.blit(button_text, (newgame_button.x + 50, newgame_button.y + 12))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if newgame_button.collidepoint(event.pos):
                    chooseplayer.chooseplayer()



        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    begin()