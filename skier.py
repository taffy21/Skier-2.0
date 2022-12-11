import pygame

class Skier:
    """creates an instance of a skier"""
    def __init__(self, window, imageList, WIDTH, HEIGHT):
        self.window = window
        self.imageList = imageList
        self.image = pygame.image.load(self.imageList[0])
        self.rect = self.image.get_rect(midtop = (WIDTH//2, HEIGHT//20))      
        self.direction = 0  
    
    def moveLeft(self):
        self.direction += 1
        if self.direction == 0:
            self.image = pygame.image.load(self.imageList[0])
        if self.direction == 1:
            self.image = pygame.image.load(self.imageList[1])
        if self.direction == 2:
            self.image = pygame.image.load(self.imageList[2])   
    
    def moveRight(self):
        self.direction -= 1
        if self.direction == 0:
            self.image = pygame.image.load(self.imageList[0])
        if self.direction == -1:
            self.image = pygame.image.load(self.imageList[3])
        if self.direction == -2:
            self.image = pygame.image.load(self.imageList[4])
      

    def draw(self):
        self.window.blit(self.image, self.rect)