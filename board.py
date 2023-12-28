import numpy as np
import pygame
import sys
import colors 
import resources as res
import helpers as h


#FONT = pygame.font.Font(None, 36)
class BoardClass:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]


    def verify_board(self):
        pass

    def play_move(self, tile):
        pass

if __name__ == "__main__":

    screen = pygame.display.set_mode((h.WIDTH, h.HEIGHT))
    b = BoardClass()
    b.draw_board(screen)


    
    
   

