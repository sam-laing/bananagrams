import numpy as np
import pygame
import sys
import colors 
import resources as res

class Board:
    def __init__(self, pos):
        self.board = [[None for _ in range(15)] for _ in range(15)]





    def draw(self, scrn, ms):
        '''
        Draws the scrabble board along with all the tiles.
        If tile is none, draw bonus
        if not, draw tiles (draw tile first, then bonus)
        If there is an active moveset, draws it as well
        '''
        for x in range(len(self.board)):
            # Draw the board (bonus or bust)
            for y in range(len(self.board[x])):
                if self.board[x][y] is None:
                    # Draw the bonus if there is no tile
                    scrn.blit(res.board[self.bonus[x][y]], (x * 50, y * 50))
                else:
                    # Draw the tile otherwise
                    scrn.blit(res.board[self.board[x][y]], (x * 50, y * 50))

        for x, y, l in ms.m:
            scrn.blit(res.board[l], (x * 50, y * 50))

        # Draw the lines between the board
        for i in range(15):
            pygame.draw.aaline(scrn,
                               colors.BLACK,
                               (0, i * 50),
                               (800, i * 50))
            pygame.draw.aaline(scrn,
                               colors.BLACK,
                               (i * 50, 0),
                               (i * 50, 800))

    def verify_board(self):
        pass

    def play_move(self, tile):
        pass

if __name__ == "__main__":
    print("hello")


    
    
   

