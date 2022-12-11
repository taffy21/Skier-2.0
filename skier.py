import pygame

class Skier:
    """creates an instance of a skier"""
    def __init__(self, window, imageList, WIDTH, HEIGHT):
        self.window = window
        self.imageList = imageList
        self.direction = 2
        self.image = pygame.image.load(self.imageList[self.direction])
        self.rect = self.image.get_rect(midtop = (WIDTH//2, HEIGHT//20))    

             
    def moveSkier(self, event):                 #TODO: FIND A WAY TO ENSURE THAT THE MAX & MIN VALUES ARE 4 AND 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction -= 1           
                self.image = pygame.image.load(self.imageList[self.direction])
                if self.direction < 0:
                    self.direction = 0
            if event.key == pygame.K_RIGHT:
                self.direction += 1           
                self.image = pygame.image.load(self.imageList[self.direction])
                if self.direction > 4:
                    self.direction = 4
                      

    def draw(self):
        self.window.blit(self.image, self.rect)