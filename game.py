#Modules
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
speed = 0.5
offScreen = (1000, 20000)

#Fonts
smallFont = pygame.font.Font("VCR.ttf", 30)
MainMenuFont = pygame.font.Font("VCR.ttf", 50)
TitleFont = pygame.font.Font("VCR.ttf", 80)

#Variables
GreenButton = "Play"
YellowButton = "Settings"
RedButton = "Exit Game"

#Postion Tuples
quitButtonPosition = (200, 900)
settingsButtonPosition = (200, 600)
playButtonPosition = (200, 300)
titleTextPosition = (150, 100)
playButtonTextPosition = (335, 375)
settingsButtonTextPosition = (280, 675)
quitButtonTextPosition = (270, 975)
speedTextPosition = (315, 1030)

#Scale Tuples
quitButtonScale = (400, 200)
settingsButtonScale = (400, 200)
playButtonScale = (400, 200)

#Text
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
    #Loopable Menu Text
    speedTextVariable = ("Speed:" + str(speed))
    quitGameText = MainMenuFont.render(RedButton, False, "black")
    settingsGameText = MainMenuFont.render(YellowButton, False, "black")
    playGameText = MainMenuFont.render(GreenButton, False, "black")
    speedText = smallFont.render(speedTextVariable, False, "black")
    
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
        #Main Menu Checks
        if event.type == pygame.KEYDOWN and MainMenuIsOpen == True and SettingsAreOpen == False and GameIsOpen == False:
            if event.key == pygame.K_ESCAPE:
                GameIsRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and MainMenuIsOpen == True and SettingsAreOpen == False and GameIsOpen == False:
            if quitButtonGeometry.collidepoint(MousePosition):
                GameIsRunning = False
            if settingsButtonGeometry.collidepoint(MousePosition):
                SettingsAreOpen = True
                MainMenuIsOpen = False
                GameIsOpen = False
                GreenButton = "Speed Up"
                YellowButton = "Speed Down"
                RedButton = "Exit"
                playButtonTextPosition = (280, 375)
                settingsButtonTextPosition = (255, 675)
                quitButtonTextPosition = (340, 975)
                speed+=0.5
            if playButtonGeometry.collidepoint(MousePosition):
                SettingsAreOpen = False
                GameIsOpen = True
                MainMenuIsOpen = False
        if event.type == pygame.MOUSEBUTTONDOWN and MainMenuIsOpen == False and SettingsAreOpen == True and GameIsOpen == False:
            if quitButtonGeometry.collidepoint(MousePosition):
                MainMenuIsOpen = True
                SettingsAreOpen = False
                GameIsOpen = False
                GreenButton = "Play"
                YellowButton = "Settings"
                RedButton = "Exit Game"
                playButtonTextPosition = (335, 375)
                settingsButtonTextPosition = (280, 675)
                quitButtonTextPosition = (270, 975)
            if playButtonGeometry.collidepoint(MousePosition):
                speed += 0.5
                if speed > 10:
                    speed = 10
                print(speed)
            if settingsButtonGeometry.collidepoint(MousePosition):
                speed -= 0.5
                if speed < 0.5:
                    speed = 0.5
                print(speed)
        if event.type == pygame.KEYDOWN and MainMenuIsOpen == False and SettingsAreOpen == False and GameIsOpen == True:
            if event.key == pygame.K_ESCAPE:
                MainMenuIsOpen = True
                SettingsAreOpen = False
                GameIsOpen = False
            
    #Background Texture
    screen.blit(menuBg, (0, 0))
    #Textures, Rendering, and FPS Limiter
    if MainMenuIsOpen == True or SettingsAreOpen == True:
        screen.blit(quitButtonTexture, quitButtonPosition)
        screen.blit(quitGameText, quitButtonTextPosition)
        screen.blit(settingsButtonTexture, settingsButtonPosition)
        screen.blit(settingsGameText, settingsButtonTextPosition)
        screen.blit(playButtonTexture, playButtonPosition)
        screen.blit(playGameText, playButtonTextPosition)
        screen.blit(titleText, titleTextPosition)
    else:
        screen.blit(quitButtonTexture, offScreen)
        screen.blit(quitGameText, offScreen)
        screen.blit(settingsButtonTexture, offScreen)
        screen.blit(settingsGameText, offScreen)
        screen.blit(playButtonTexture, offScreen)
        screen.blit(playGameText, offScreen)
        screen.blit(titleText, offScreen)
    if SettingsAreOpen == True:
        screen.blit(speedText, speedTextPosition)
    else:
        screen.blit(speedText, offScreen)
    if GameIsOpen == True:
        pass
    else:
        pass
    pygame.display.flip()
    clock.tick(60)

#Quitting
pygame.quit()
sys.exit()