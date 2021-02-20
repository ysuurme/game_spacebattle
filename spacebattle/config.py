# Configuration file holding constant values used throughout the project.
import pygame

# pygame window:
WIDTH, HEIGHT = 1000, 500
FPS = 60
BORDER_WIDTH = 10
BORDER = pygame.Rect((WIDTH-BORDER_WIDTH)/2, 0, BORDER_WIDTH, HEIGHT)


# Game colors:
COLORS = {
    "BLACK": (0, 0, 0),
    "GREY": (128, 128, 128),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "WHITE": (255, 255, 255)
    }

# Game assets
SHIP_WIDTH = 60
SHIP_HEIGHT = 60
SHIP_SPEED = 5

P1_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets/spaceShipBlue.png'),
                                                          (SHIP_WIDTH, SHIP_HEIGHT)), 270)
P2_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets/spaceShipOrange.png'),
                                                              (SHIP_WIDTH, SHIP_HEIGHT)), 90)

BLT_WIDTH = 10
BLT_HEIGHT = 4
MAX_BLTS = 5