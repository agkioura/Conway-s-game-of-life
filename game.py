import pygame
from pygame import Rect, Surface

WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)

class Game:

    def __init__(self) -> None:
        self.world_width = 20
        self.world_height = 20

        self.board = [[0 for i in range(self.world_width)] for j in range(self.world_height)]

        self.board[self.world_width // 2 - 1][self.world_height // 2 - 1] = 1

    def render(self, surface: Surface) -> None:
        cell_width = surface.get_size()[0] / self.world_width
        cell_height = surface.get_size()[1]/ self.world_height
        for i in range(self.world_height):
            for j in range(self.world_width):
                cell = Rect((i * cell_width, j * cell_height), (cell_width, cell_height))
                color = WHITE if self.board[i][j] == 1 else BLACK
                pygame.draw.rect(surface, color, cell)
