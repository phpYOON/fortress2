import pygame




pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

#fire_sound = pygame.mixer.Sound("1.mp3")
#explosion_sound = pygame.mixer.Sound("1.mp3")

#pygame.mixer.music.load("1.mp3")
#pygame.mixer.music.play(-1)


pygame.display.set_caption('Tanks - Brought To You By code-projects.org')

icon = pygame.image.load("ic.jpg")
pygame.display.set_icon(icon)
#----------------------------------------colors----------------------------------------------
wheat=(245,222,179)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0,0,255)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

#--------------------------------for picking current time for the frames per second----------------------
clock = pygame.time.Clock()
#--------------------------------geometry of tank and its turret------------------------------------------
tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

ground_height = 35
#--------------------------------------------fonts with size, for text_object function----------------
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("Yu Mincho Demibold", 85)
vsmallfont = pygame.font.SysFont("Yu Mincho Demibold", 25)

#--------------------------------------------defining score function----------------------------------
def score(score):
    text = smallfont.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0, 0])

#---defining function to get the fonts and sizes assigned with them by size names by default size="small"--
def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "vsmall":
        textSurface = vsmallfont.render(text, True, color)

    return textSurface, textSurface.get_rect()

#---------------------fuction for texts that has to appear over button----------------------------------------
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="vsmall"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)

#--------------------fuction for texts that has to appear over screen----------------------------------------
def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)
