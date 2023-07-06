import pygame
import sys

#PyGame Setup
pygame.init()
clock = pygame.time.Clock()

#Game Setup and Running Variable
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
GameIsRunning = True
MainMenuIsOpen = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Postion Tuples
quitButtonPosition = (200, 200)

#Geometry
quitButtonGeometry = pygame.Rect(quitButtonPosition, (400, 200))

#Movement Variables

#Texture Importing
quitButtonTexture = pygame.image.load('quitButton.png')

#Game Loop
while GameIsRunning:
    #Gets Mouse Position
    MousePosition = pygame.mouse.get_pos()
    
    #Screen Refresh
    screen.fill("white")
    
    #Draw Geometry
    
    #Event Handler
    for event in pygame.event.get():
        #Quit Game Using Toolbar
        if event.type == pygame.QUIT:
            GameIsRunning = False
        #Main Menu Quit Game Checks
        if event.type == pygame.KEYDOWN and MainMenuIsOpen == True:
            if event.key == pygame.K_ESCAPE:
                GameIsRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and MainMenuIsOpen == True:
            if quitButtonGeometry.collidepoint(MousePosition):
                GameIsRunning = False
    
    #Textures, Rendering, and FPS Limiter
    screen.blit(quitButtonTexture, quitButtonPosition)
    pygame.display.flip()
    clock.tick(60)

#Quitting
pygame.quit()
sys.exit()