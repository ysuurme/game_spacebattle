import pygame

from .config import COLORS, P1_SPACESHIP, P2_SPACESHIP, SHIP_WIDTH, SHIP_HEIGHT, SHIP_SPEED


class Game:
    def __init__(self, win):
        self.win = win
        self.player1 = None
        self.player2 = None
        self.init_players()

    def update(self):
        self.win.fill(COLORS['WHITE'])
        self.blit_spaceships()
        pygame.display.update()

    def init_players(self):
        self.player1 = Player1(200, 250)
        self.player2 = Player2(800, 250)

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_a]:  # P1 left
            self.player1.x -= SHIP_SPEED
        if keys_pressed[pygame.K_w]:  # P1 up
            self.player1.y -= SHIP_SPEED
        if keys_pressed[pygame.K_d]:  # P1 right
            self.player1.x += SHIP_SPEED
        if keys_pressed[pygame.K_s]:  # P1 down
            self.player1.y += SHIP_SPEED

        if keys_pressed[pygame.K_LEFT]:  # P2 left
            self.player2.x -= SHIP_SPEED
        if keys_pressed[pygame.K_UP]:  # P2 up
            self.player2.y -= SHIP_SPEED
        if keys_pressed[pygame.K_RIGHT]:  # P2 right
            self.player2.x += SHIP_SPEED
        if keys_pressed[pygame.K_DOWN]:  # P2 down
            self.player2.y += SHIP_SPEED

    def blit_spaceships(self):
        self.win.blit(self.player1.spaceship, (self.player1.x, self.player1.y))
        self.win.blit(self.player2.spaceship, (self.player2.x, self.player2.y))


class Spaceship:
    def __init__(self):
        self.health = 100


class Player1(Spaceship):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.spaceship = P1_SPACESHIP
        self.hull = pygame.Rect(x, y, SHIP_WIDTH, SHIP_HEIGHT)


class Player2(Spaceship):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.spaceship = P2_SPACESHIP
        self.hull = pygame.Rect(x, y, SHIP_WIDTH, SHIP_HEIGHT)
