import pygame
from settings import *
#----------------------fuction for players tank , defining turrets positins and wheels dimensions------------
def tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x - 27, y - 2),
                       (x - 26, y - 5),
                       (x - 25, y - 8),
                       (x - 23, y - 12),
                       (x - 20, y - 14),
                       (x - 18, y - 15),
                       (x - 15, y - 17),
                       (x - 13, y - 19),
                       (x - 11, y - 21)
                       ]

    pygame.draw.circle(gameDisplay, blue, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, blue, (x - tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, blue, (x, y), possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 15, y + 20), wheelWidth)

    return possibleTurrets[turPos]

#----------------------fuction for computers tank , defining turrets positins and wheels dimensions------------
def enemy_tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x + 27, y - 2),
                       (x + 26, y - 5),
                       (x + 25, y - 8),
                       (x + 23, y - 12),
                       (x + 20, y - 14),
                       (x + 18, y - 15),
                       (x + 15, y - 17),
                       (x + 13, y - 19),
                       (x + 11, y - 21)
                       ]

    pygame.draw.circle(gameDisplay, blue, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, blue, (x - tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, blue, (x, y), possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 15, y + 20), wheelWidth)

    return possibleTurrets[turPos]
