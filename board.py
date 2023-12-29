import numpy as np
import pygame
import sys
import colors 
import resources as res
import helpers as h


#FONT = pygame.font.Font(None, 36)
class BoardClass:
    def __init__(self):
        self.board = [[" " for _ in range(h.GRID_SIZE)] for _ in range(h.GRID_SIZE)]


    def verify_board(self):
        pass

    def play_move(self, tile):
        pass

if __name__ == "__main__":

    screen = pygame.display.set_mode((h.WIDTH, h.HEIGHT))
    b = BoardClass()
    b.draw_board(screen)


    
    
   

