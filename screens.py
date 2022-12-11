import pygame
import cfg

class OpeningScreen:
    """creates the opening screen"""
    def __init__(self, window, text, fontSize, WIDTH, HEIGHT):
        pygame.font.init()
        self.window = window
        self.text = text
        self.fontSize = fontSize
        self.font = pygame.font.SysFont("Arial", self.fontSize)
        self.fontname = self.font.render(self.text, True, cfg.RED)
        self.rect = self.fontname.get_rect(midtop = (WIDTH//2, HEIGHT//4))

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                return True

    def draw(self):
        self.window.blit(self.fontname, self.rect)
