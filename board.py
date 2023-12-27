import numpy as np
import pygame
import sys
import colors 
import resources as res
import helpers as h

class Board:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]

    def draw_board(self, screen):
        screen.fill(colors.WHITE)

        for row in range(h.GRID_SIZE):
            for col in range(h.GRID_SIZE):
                pygame.draw.rect(screen, colors.GRAY, (col * h.TILE_SIZE, row * h.TILE_SIZE, h.TILE_SIZE, h.TILE_SIZE), 1)
                text = h.FONT.render(self.board[row][col], True, colors.BLACK)
                screen.blit(text, (col * h.TILE_SIZE + h.TILE_SIZE // 3, row * h.TILE_SIZE + h.TILE_SIZE // 3)) 

    def verify_board(self):
        pass

    def play_move(self, tile):
        pass

if __name__ == "__main__":

    screen = pygame.display.set_mode((h.WIDTH, h.HEIGHT))
    b = Board()
    b.draw_board(screen)


    
    
   

