import pygame
import game
import game1
import petroom
import globalv

def clueroom(gameversion, player, x, y):
    pygame.init()

    width, height = 1600, 900
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Clue Room")
    clock = pygame.time.Clock()

    bgpic = pygame.image.load("picture/clueroom.png")
    bgpic = pygame.transform.scale(bgpic, (width, height))

    font1 = pygame.font.SysFont("Arial", 30)
    
    while True:
        screen.blit(bgpic, (0, 0))

        for i in globalv.get_clues:
            text1 = font1.render(i, True, (0, 0, 0))
            clue_button = pygame.Rect(100, 60 + globalv.get_clues.index(i) * 85, 1400, 60)
            pygame.draw.rect(screen, (0, 0, 0), clue_button.inflate(8, 8))
            pygame.draw.rect(screen, (255, 255, 255), clue_button)
            screen.blit(text1, (clue_button.x + (clue_button.width - text1.get_width()) // 2, clue_button.y + (clue_button.height - text1.get_height()) // 2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            petroom.petroom(gameversion, x, y, player)

        if keys[pygame.K_RETURN]:
            if gameversion == "game1":
                game1.game1(player, x, y)
            elif gameversion == "game":
                game.game(player, x, y)
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    clueroom("game", "hero0", 100, 100)
        



