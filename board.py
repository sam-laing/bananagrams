import numpy as np
import pygame
import sys

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def draw(self, screen):
        for row in range(self.size):
            for col in range(self.size):
                pygame.draw.rect(
                    screen,
                    pygame.Color("White"),
                    (col * 50, row * 50, 50, 50),
                )
                pygame.draw.rect(
                    screen,
                    pygame.Color("Black"),
                    (col * 50, row * 50, 50, 50),
                    2,
                )

    def verify_board(self):
        pass

    def play_move(self, tile):
        pass

if __name__ == "__main__":
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 600, 600
    BOARD_SIZE = 15
    TILE_SIZE = WIDTH // BOARD_SIZE

    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Scrabble Board")

    # Initialize the board
    board = Board(BOARD_SIZE)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        board.draw(screen)
        pygame.display.flip()


    
    
   

