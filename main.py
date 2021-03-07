# Inspired by 'Pygame in 90 minutes - For beginners' by Tech With Tim
# (https://www.youtube.com/watch?v=jO6qQDNa2UY&t=1824s)

import pygame
from spacebattle.config import WIDTH, HEIGHT, FPS, P1_HIT, P2_HIT
from spacebattle.game import Game, spaceship_hit

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Battle!')  # todo implement AI


def main():  # todo implement sounds for game start, game won
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    game.shoot(game.player1)

                if event.key == pygame.K_RCTRL:
                    game.shoot(game.player2)

            if event.type == P1_HIT:
                spaceship_hit(game.player1)

            if event.type == P2_HIT:
                spaceship_hit(game.player2)

        keys_pressed = pygame.key.get_pressed()
        game.move(keys_pressed)

        game.update()
        if game.game_over:
            pygame.time.delay(5000)
            break

    main()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
