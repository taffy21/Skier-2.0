import pygame

class Skier(pygame.sprite.Sprite):
    """creates an instance of a skier"""
    def __init__(self, window, imageList, WIDTH, HEIGHT):
        super().__init__()
        self.window = window
        self.imageList = imageList
        self.direction = 2
        self.image = pygame.image.load(self.imageList[self.direction])
        self.rect = self.image.get_rect(midtop = (WIDTH//2, HEIGHT//20))    

             
    def moveSkier(self, event):                 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction -= 1           
                if self.direction >= 0:
                    self.image = pygame.image.load(self.imageList[self.direction])
                else:
                    self.direction = 0
            if event.key == pygame.K_RIGHT:
                self.direction += 1 
                if self.direction <= 4:          
                    self.image = pygame.image.load(self.imageList[self.direction])
                else:
                    self.direction = 4                      
    
    def skierFall(self):
        self.direction = 5
        self.image = pygame.image.load(self.imageList[self.direction])

    def skierStartPos(self):
        self.direction = 2
        self.image = pygame.image.load(self.imageList[self.direction])

    def draw(self):
        self.window.blit(self.image, self.rect)