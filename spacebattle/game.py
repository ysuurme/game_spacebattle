import pygame

from .config import BACKGROUND, BORDER, BORDER_WIDTH, WIDTH, HEIGHT, COLORS,\
    P1_SPACESHIP, P2_SPACESHIP, SHIP_WIDTH, SHIP_HEIGHT, SHIP_SPEED, BLT_WIDTH, BLT_HEIGHT, BLT_SPEED, BLT_DAMAGE,\
    MAX_BLTS, P1_HIT, P2_HIT, FONT_HEALTH, FONT_WINNER, SOUND_BLT_FIRE, SOUND_BLT_HIT


def spaceship_hit(player):
    player.health -= BLT_DAMAGE
    SOUND_BLT_HIT.play()


class Game:
    def __init__(self, win):
        self.win = win
        self.game_over = False
        self.player1 = None
        self.player2 = None
        self.init_players()
        self.bullets = []

    def update(self):
        self.win.blit(BACKGROUND, (0, 0))
        self.draw_game()
        self.blit_spaceships()
        self.draw_bullets()
        self.handle_bullets()
        self.winner()
        pygame.display.update()

    def draw_game(self):
        pygame.draw.rect(self.win, COLORS['BLACK'], BORDER)  # draw middle border
        p1_health = FONT_HEALTH.render(f"P1 Health: {self.player1.health}", 1, COLORS['WHITE'])
        p2_health = FONT_HEALTH.render(f"P2 Health: {self.player2.health}", 1, COLORS['WHITE'])
        self.win.blit(p1_health, (10, 10))
        self.win.blit(p2_health, (WIDTH - p2_health.get_width() - 10, 10))

    def init_players(self):
        self.player1 = Player1(200, 250)
        self.player2 = Player2(800, 250)

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.player1.hull.x - SHIP_SPEED > 0:  # P1 left
            self.player1.hull.move_ip(-SHIP_SPEED, 0)
        if keys_pressed[pygame.K_w] and self.player1.hull.y - SHIP_SPEED > 0:  # P1 up
            self.player1.hull.move_ip(0, -SHIP_SPEED)
        if keys_pressed[pygame.K_d] and self.player1.hull.x + SHIP_WIDTH + SHIP_SPEED < BORDER.x:  # P1 right
            self.player1.hull.move_ip(SHIP_SPEED, 0)
        if keys_pressed[pygame.K_s] and self.player1.hull.y + SHIP_HEIGHT + SHIP_SPEED < HEIGHT:  # P1 down
            self.player1.hull.move_ip(0, SHIP_SPEED)

        if keys_pressed[pygame.K_LEFT] and self.player2.hull.x - BORDER_WIDTH*2 + SHIP_SPEED > BORDER.x:  # P2 left
            self.player2.hull.move_ip(-SHIP_SPEED, 0)
        if keys_pressed[pygame.K_UP] and self.player2.hull.y - SHIP_SPEED > 0:  # P2 up
            self.player2.hull.move_ip(0, -SHIP_SPEED)
        if keys_pressed[pygame.K_RIGHT] and self.player2.hull.x + SHIP_WIDTH + SHIP_SPEED < WIDTH:  # P2 right
            self.player2.hull.move_ip(SHIP_SPEED, 0)
        if keys_pressed[pygame.K_DOWN] and self.player2.hull.y + SHIP_HEIGHT + SHIP_SPEED < HEIGHT:  # P2 down
            self.player2.hull.move_ip(0, SHIP_SPEED)

    def shoot(self, player):
        if player.ammo >= MAX_BLTS:
            bullet = Bullet(player)  # Create bullet
            SOUND_BLT_FIRE.play()
            self.bullets.append(bullet)
        else:
            print(f'Player: {type(player).__name__} is out of ammo!')

    def handle_bullets(self):
        for b in self.bullets:
            b.shape.move_ip(b.BLT_SPEED, 0)
            if self.player1.hull.colliderect(b.shape):
                pygame.event.post(pygame.event.Event(P1_HIT))
                self.bullets.remove(b)
            elif self.player2.hull.colliderect(b.shape):
                pygame.event.post(pygame.event.Event(P2_HIT))
                self.bullets.remove(b)
            elif b.x < 0:
                self.bullets.remove(b)
            elif b.x > WIDTH:
                self.bullets.remove(b)

    def draw_bullets(self):
        for b in self.bullets:
            if b.player == 'Player1':
                color = COLORS['GREEN']
            elif b.player == 'Player2':
                color = COLORS['YELLOW']
            else:
                color = COLORS['WHITE']
            pygame.draw.rect(self.win, color, b.shape)

    def blit_spaceships(self):
        self.win.blit(self.player1.spaceship, (self.player1.hull.x, self.player1.hull.y))
        self.win.blit(self.player2.spaceship, (self.player2.hull.x, self.player2.hull.y))

    def winner(self):
        winner_text = ""
        if self.player1.health <= 0:
            winner_text = FONT_WINNER.render("Player 2 has won the game!", 1, COLORS['YELLOW'])
            self.game_over = True
        elif self.player2.health <= 0:
            winner_text = FONT_WINNER.render("Player 1 has won the game!", 1, COLORS['GREEN'])
            self.game_over = True
        if self.game_over:
            self.win.blit(winner_text, (WIDTH/2 - winner_text.get_width()/2, HEIGHT/2 - winner_text.get_height()/2))


class Spaceship:
    def __init__(self):
        self.health = 100
        self.ammo = MAX_BLTS


class Player1(Spaceship):
    def __init__(self, x, y):
        super().__init__()
        self.spaceship = P1_SPACESHIP
        self.hull = pygame.Rect(x, y, SHIP_WIDTH, SHIP_HEIGHT)


class Player2(Spaceship):
    def __init__(self, x, y):
        super().__init__()
        self.spaceship = P2_SPACESHIP
        self.hit = pygame.USEREVENT + 2
        self.hull = pygame.Rect(x, y, SHIP_WIDTH, SHIP_HEIGHT)


class Bullet:
    def __init__(self, player):
        if type(player).__name__ == 'Player1':
            self.player = 'Player1'
            self.x = player.hull.x + SHIP_WIDTH  # Player 1 shoots from origin + ship width
            self.BLT_SPEED = BLT_SPEED  # Player1 shoots to the right

        if type(player).__name__ == 'Player2':
            self.player = 'Player2'
            self.x = player.hull.x - BLT_WIDTH  # Player 2 shoots from origin - bullet width
            self.BLT_SPEED = -BLT_SPEED  # Player2 shoots to the left

        self.y = player.hull.y + SHIP_HEIGHT // 2
        self.BLT_WIDTH = BLT_WIDTH
        self.BLT_HEIGHT = BLT_HEIGHT
        self.shape = pygame.Rect(self.x, self.y, self.BLT_WIDTH, self.BLT_HEIGHT)
