import pygame

from .config import BACKGROUND, BORDER, BORDER_WIDTH, WIDTH, HEIGHT, COLORS,\
    P1_SPACESHIP, P2_SPACESHIP, SHIP_WIDTH, SHIP_HEIGHT, SHIP_SPEED, BLT_WIDTH, BLT_HEIGHT,BLT_SPEED, MAX_BLTS


class Game:
    def __init__(self, win):
        self.win = win
        self.player1 = None
        self.player2 = None
        self.init_players()

    def update(self):
        self.win.blit(BACKGROUND, (0, 0))
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

    def handle_bullets(self, bullets):
        for bullet in bullets:
            bullet.x += BLT_SPEED
            if self.player1.colliderect(bullet):
                print('Player 1 hit!')
                # pygame.event.post(pygame.event.Event(P1_SPACESHIP_HIT))
                self.bullets.remove(bullet)
            if self.player2.colliderect(bullet):
                print('Player 2 hit!')
                # pygame.event.post(pygame.event.Event(P1_SPACESHIP_HIT))
                self.bullets.remove(bullet)
            if bullet.x < 0:
                self.bullets.remove(bullet)
            elif bullet.x > WIDTH:
                self.bullets.remove(bullet)

    def draw_bullets(self):
        for bullet in self.player1.bullets:
            pygame.draw.rect(self.win, COLORS['BLUE'], bullet)
        for bullet in self.player2.bullets:
            pygame.draw.rect(self.win, COLORS['YELLOW'], bullet)


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
        self.hit = pygame.USEREVENT +1
        self.hull = pygame.Rect(x, y, SHIP_WIDTH, SHIP_HEIGHT)

    def shoot(self):
        if len(self.bullets) < self.ammo:
            self.bullets.append(Bullet(self))
            self.handle_bullet(self.bullets)


class Player2(Spaceship):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.spaceship = P2_SPACESHIP
        self.hit = pygame.USEREVENT + 2
        self.hull = pygame.Rect(x, y, SHIP_WIDTH, SHIP_HEIGHT)

    def shoot(self):
        if len(self.bullets) < self.ammo:
            self.ammo -= 1
            self.bullets.append(Bullet(self))


class Bullet:
    def __init__(self, spaceship):
        self.spaceship = spaceship
        self.x = spaceship.x  # todo if player 1 bullet x is x + spaceship width
        self.y = spaceship.y
        self.BLT_WIDTH = BLT_WIDTH
        self.BLT_HEIGHT = BLT_HEIGHT
        self.BLT_SPEED = +BLT_SPEED  # todo reverse bullet for player 2
        self.BLT_SPEED = -BLT_SPEED

        self.bullet = pygame.Rect(self.x + SHIP_WIDTH, self.y + SHIP_HEIGHT//2, self.BLT_WIDTH, self.BLT_HEIGHT)
