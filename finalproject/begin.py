import pygame
import chooseplayer

def begin():
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    begin = pygame.image.load("picture/begin.png")
    begin = pygame.transform.scale(begin, (width, height))
    screen.blit(begin, (0, 0))

    font_button = pygame.font.SysFont("Arial", 40, bold=True)
    newgame_button = pygame.Rect(680, 480, 300, 72)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if newgame_button.collidepoint(event.pos):
                    running = False
                    chooseplayer.chooseplayer()

        pygame.draw.rect(screen, (0, 0, 0), newgame_button.inflate(8, 8))
        pygame.draw.rect(screen, (255, 255, 255), newgame_button)
        button_text = font_button.render("New Game", True, (0, 0, 0))
        screen.blit(button_text, (newgame_button.x + 50, newgame_button.y + 12))

        pygame.display.update()

if __name__ == "__main__":
    begin()