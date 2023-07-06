import pygame
import sys

#PyGame Setup
pygame.init()
clock = pygame.time.Clock()

#Game Setup and Running Variable
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1200
GameIsRunning = True
MainMenuIsOpen = True
GameIsOpen = False
SettingsAreOpen = False
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
MainMenuFont = pygame.font.Font("VCR.ttf", 50)
TitleFont = pygame.font.Font("VCR.ttf", 80)

#Postion Tuples
quitButtonPosition = (200, 900)
quitButtonTextPosition = (270, 975)
settingsButtonPosition = (200, 600)
settingsButtonTextPosition = (280, 675)
playButtonPosition = (200, 300)
playButtonTextPosition = (335, 375)
titleTextPosition = (150, 100)

#Scale Tuples
quitButtonScale = (400, 200)
settingsButtonScale = (400, 200)
playButtonScale = (400, 200)

#Surfaces
quitGameText = MainMenuFont.render("Quit Game", False, "black")
settingsGameText = MainMenuFont.render("Settings", False, "black")
playGameText = MainMenuFont.render("Play", False, "black")
titleText = TitleFont.render("Square Game", False, "white")

#Geometry
quitButtonGeometry = pygame.Rect(quitButtonPosition, quitButtonScale)
settingsButtonGeometry = pygame.Rect(settingsButtonPosition, settingsButtonScale)
playButtonGeometry = pygame.Rect(playButtonPosition, playButtonScale)

#Movement Variables

#Texture Importing
quitButtonTexture = pygame.image.load("quitButton.png")
settingsButtonTexture = pygame.image.load("settingsButton.png")
playButtonTexture = pygame.image.load("playButton.png")
menuBg = pygame.image.load("menuScreen.png")

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
    
    #Background Texture
    screen.blit(menuBg, (0, 0))
    
    #Textures, Rendering, and FPS Limiter
    screen.blit(quitButtonTexture, quitButtonPosition)
    screen.blit(quitGameText, quitButtonTextPosition)
    screen.blit(settingsButtonTexture, settingsButtonPosition)
    screen.blit(settingsGameText, settingsButtonTextPosition)
    screen.blit(playButtonTexture, playButtonPosition)
    screen.blit(playGameText, playButtonTextPosition)
    screen.blit(titleText, titleTextPosition)
    pygame.display.flip()
    clock.tick(60)

#Quitting
pygame.quit()
sys.exit()