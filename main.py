import pygame
from game import Game

def start():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    running = True

    game = Game()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.update()
                if event.key == pygame.K_e:
                    game.toggle_edit_mode()
            if event.type == pygame.MOUSEBUTTONDOWN and game.in_edit_mode():
                game.place_cell()

        screen.fill("black")
        game.render(screen)

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    start()
