import pygame

# constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = ( 125, 125, 125)
TEAL = (0, 128, 128)
RED = (255, 100, 0)

# Size
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

# frame
FPS = 30

# text

class Text:
    '''create an instance of a font object'''
    def __init__(self, window, text, loc):
        pygame.font.init()
        self.window = window
        self.text = text
        self.loc = loc
        self.font = pygame.font.SysFont("Arial", 30)
        self.display = self.font.render(self.text, True, TEAL)
        self.rect = self.display.get_rect()

    def update(self, text):
        self.display = self.font.render(text, True, TEAL)

    def draw(self):
        self.window.blit(self.display, self.loc)