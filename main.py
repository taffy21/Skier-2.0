import pygame
import cfg
import sys
import obstacles
import skier
import screens

# Initialisation

pygame.init()
window = pygame.display.set_mode(cfg.SIZE)
pygame.display.set_caption("Skier")
clock = pygame.time.Clock()

# Assets
treeImg = "tree.png"
flagImg = "flag.png"

imgList = [r"C:\Users\tbepe\OneDrive - OPHID\Desktop\Data Analytics\Python Projects\VSCODE FILES\skier\skier_left2.png", 
r"C:\Users\tbepe\OneDrive - OPHID\Desktop\Data Analytics\Python Projects\VSCODE FILES\skier\skier_left1.png", 
r"C:\Users\tbepe\OneDrive - OPHID\Desktop\Data Analytics\Python Projects\VSCODE FILES\skier\skier_forward.png",
r"C:\Users\tbepe\OneDrive - OPHID\Desktop\Data Analytics\Python Projects\VSCODE FILES\skier\skier_right1.png", 
r"C:\Users\tbepe\OneDrive - OPHID\Desktop\Data Analytics\Python Projects\VSCODE FILES\skier\skier_right2.png", 
"skier_fall.png"]


# Variables
openingScreen = screens.OpeningScreen(window, "SKIER GAME", 40, cfg.WIDTH, cfg.HEIGHT)
openingScreen2 = screens.OpeningScreen(window, "Press 'S' to Start!!!", 40, cfg.WIDTH, 1000)

# obstacle
trees = []
for i in range(20):
    tree = obstacles.Obstacle(window, treeImg, (40, 40))
    if tree not in trees:
        trees.append(tree)

flags = []
for i in range(10):
    flag = obstacles.Obstacle(window, flagImg, (25, 25))
    if flag not in flags:
        flags.append(flag)

treeSprite = pygame.sprite.Group()
treeSprite.add(trees)

flagSpriteGroup = pygame.sprite.Group()
flagSpriteGroup.add(flags)

# skier
player = skier.Skier(window, imgList, cfg.WIDTH, cfg.HEIGHT)
playerSprite = pygame.sprite.Group()
playerSprite.add(player)


# initial screen 
screen = "One"

# text 
score = 0
scoretext = cfg.Text(window, f"Score: {score}", (10, 10))

# Loops
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if openingScreen.handleEvent(event):
            screen = "Two"

        if player.moveSkier(event):
            pass

    window.fill(cfg.WHITE)
    
    if screen == "One":
        openingScreen.draw()
        openingScreen2.draw()        

    if screen == "Two":

        treeSprite.draw(window)

        flagSpriteGroup.draw(window)

        playerSprite.draw(window)

        scoretext.draw()

        treeSprite.update()

        flagSpriteGroup.update()  

        flagCapture = pygame.sprite.spritecollide(player, flagSpriteGroup, True, False)

        treeCollide = pygame.sprite.spritecollide(player, treeSprite, True, False)

        if flagCapture:
            score += 10
            scoretext.update(f"Score: {score}")

        if treeCollide:                #TODO: AFTER COLLISION, RETURN SKIER TO UPRIGHT POSITION
            player.skierFall()
            pygame.time.delay(500)
            #player.skierStartPos()
        
    pygame.display.update()

    clock.tick(cfg.FPS)

