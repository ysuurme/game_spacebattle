# Based on 'Pygame in 90 minutes - For beginners' by Tech With Tim (https://www.youtube.com/watch?v=jO6qQDNa2UY&t=1824s)

import pygame
from spacebattle.config import WIDTH, HEIGHT, FPS
from spacebattle.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Battle!')  # todo implement AI


def main():  # todo implement sounds for game start, hit, game won etc.
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    player = game.player1
                    game.shoot(player)

                if event.key == pygame.K_RCTRL:
                    player = game.player2
                    game.shoot(player)

        keys_pressed = pygame.key.get_pressed()
        game.move(keys_pressed)

        game.update()

    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
