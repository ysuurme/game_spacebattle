import pygame

from .config import BORDER, BORDER_WIDTH, WIDTH, HEIGHT, COLORS,\
    P1_SPACESHIP, P2_SPACESHIP, SHIP_WIDTH, SHIP_HEIGHT, SHIP_SPEED, BLT_WIDTH, BLT_HEIGHT, MAX_BLTS


class Game:
    def __init__(self, win):
        self.win = win
        self.player1 = None
        self.player2 = None
        self.init_players()

    def update(self):
        self.win.fill(COLORS['WHITE'])
        self.draw_border()
        self.blit_spaceships()
        pygame.display.update()

    def init_players(self):
        self.player1 = Player1(200, 250)
        self.player2 = Player2(800, 250)

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.player1.x - SHIP_SPEED > 0:  # P1 left
            self.player1.x -= SHIP_SPEED
        if keys_pressed[pygame.K_w] and self.player1.y - SHIP_SPEED > 0:  # P1 up
            self.player1.y -= SHIP_SPEED
        if keys_pressed[pygame.K_d] and self.player1.x + SHIP_WIDTH + SHIP_SPEED < BORDER.x:  # P1 right
            self.player1.x += SHIP_SPEED
        if keys_pressed[pygame.K_s] and self.player1.y + SHIP_HEIGHT + SHIP_SPEED < HEIGHT:  # P1 down
            self.player1.y += SHIP_SPEED

        if keys_pressed[pygame.K_LEFT] and self.player2.x - BORDER_WIDTH*2 + SHIP_SPEED > BORDER.x:  # P2 left
            self.player2.x -= SHIP_SPEED
        if keys_pressed[pygame.K_UP] and self.player2.y - SHIP_SPEED > 0:  # P2 up
            self.player2.y -= SHIP_SPEED
        if keys_pressed[pygame.K_RIGHT] and self.player2.x + SHIP_WIDTH + SHIP_SPEED < WIDTH:  # P2 right
            self.player2.x += SHIP_SPEED
        if keys_pressed[pygame.K_DOWN] and self.player2.y + SHIP_HEIGHT + SHIP_SPEED < HEIGHT:  # P2 down
            self.player2.y += SHIP_SPEED

    def shoot_bullet(self):
        if event.key == pygame.K_LCTRL:
            self.player1.shoot()

        if event.key == pygame.K_RCTRL:
            self.player2.shoot()

    def blit_spaceships(self):
        self.win.blit(self.player1.spaceship, (self.player1.x, self.player1.y))
        self.win.blit(self.player2.spaceship, (self.player2.x, self.player2.y))

    def draw_border(self):
        pygame.draw.rect(self.win, COLORS['BLACK'], BORDER)


class Spaceship:
    def __init__(self):
        self.health = 100
        self.bullets = []
        self.ammo = MAX_BLTS


class Player1(Spaceship):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.spaceship = P1_SPACESHIP
        self.hull = pygame.Rect(x, y, SHIP_WIDTH, SHIP_HEIGHT)

    def shoot(self):
        if len(self.bullets) < self.ammo:
            self.bullets.append(Bullet(self.x + SHIP_WIDTH, self.y + SHIP_HEIGHT/2 - BLT_HEIGHT/2, BLT_WIDTH, BLT_HEIGHT))


class Player2(Spaceship):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.spaceship = P2_SPACESHIP
        self.hull = pygame.Rect(x, y, SHIP_WIDTH, SHIP_HEIGHT)

    def shoot(self):
        if len(self.bullets) < self.ammo:
            self.bullets.append(Bullet(self.x, self.y + SHIP_HEIGHT/2 - BLT_HEIGHT/2, BLT_WIDTH, BLT_HEIGHT))

class Bullet:
    def __init__(self, x, y, w, h):
        self.bullet = pygame.Rect(x, y)

