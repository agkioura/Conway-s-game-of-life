import pygame
from pygame import Rect, Surface

from enum import Enum

WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
LINE_COLOR = (255, 0, 0)

class State(Enum):
    DEAD = 0
    ALIVE = 1,

class Game:

    def __init__(self) -> None:
        self.world_width = 20
        self.world_height = 20

        self.board = [[State.DEAD for i in range(self.world_width)] for j in range(self.world_height)]

        self.board[self.world_height // 2][self.world_width // 2] = State.ALIVE
        self.board[self.world_height // 2][self.world_width // 2 + 1] = State.ALIVE
        self.board[self.world_height // 2][self.world_width // 2 + 2] = State.ALIVE

    def change_state(self, i, j, board) -> State:
        neighbour_cell_count = 0
        for dy in range(i - 1, i + 2):
            for dx in range(j - 1, j + 2):
                if dx >= self.world_width or dx < 0:
                    continue
                if dy >= self.world_height or dy < 0:
                    continue
                if dx == j and dy == i:
                    continue
                if board[dy][dx] == State.ALIVE:
                    neighbour_cell_count += 1

        match board[i][j]:
            case State.ALIVE:
                if neighbour_cell_count == 2 or neighbour_cell_count == 3:
                    return State.ALIVE
                return State.DEAD
            case State.DEAD:
                if neighbour_cell_count == 3:
                    return State.ALIVE
        return State.DEAD

    def update(self) -> None:
        board_copy = [row[:] for row in self.board]

        for i in range(self.world_height):
            for j in range(self.world_width):
                self.board[i][j] = self.change_state(i, j, board_copy)

    def render(self, surface: Surface) -> None:
        cell_width = surface.get_size()[0] / self.world_width
        cell_height = surface.get_size()[1]/ self.world_height

        for i in range(self.world_height):
            for j in range(self.world_width):
                cell = Rect((j * cell_width, i * cell_height), (cell_width, cell_height))
                color = WHITE if self.board[i][j] == State.ALIVE else BLACK
                pygame.draw.rect(surface, color, cell)
