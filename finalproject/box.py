import pygame
import globalv

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = (x, y)
        self.closed_image = pygame.image.load("finalproject/picture/box_close.png")  
        self.open_image = pygame.image.load("finalproject/picture/box_open.png")      
        self.closed_image = pygame.transform.scale(self.closed_image, (70, 70))
        self.open_image = pygame.transform.scale(self.open_image, (70, 70))
        self.current_image = self.closed_image                  
        self.rect = self.closed_image.get_rect(topleft=(x, y))   
        state = globalv.box_states.get(self.id, {"is_open" : False})
        self.is_open = state["is_open"]
        self.current_image = self.open_image if self.is_open else self.closed_image

    def draw(self, screen):
        screen.blit(self.current_image, (self.x, self.y))

    def toggle(self):
        if self.is_open:
            return "open"

        else:
            self.current_image = self.open_image
            self.is_open = True
            globalv.box_states[self.id] = {"is_open" : True}
            return self.event()
    
    def event(self):
        events = ["question","battle","battle","nothing","clue","question","nothing", "question","nothing","battle","clue","question"]
        game_event = events[globalv.box_count]
        globalv.box_count += 1
        return game_event

        
            




