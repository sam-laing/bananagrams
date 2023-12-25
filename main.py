import pygame
import sys

# Constants
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 15
TILE_SIZE = WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Tile(pygame.sprite.Sprite):
    def __init__(self, letter, row, col):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)  # Placeholder color for the tile
        self.rect = self.image.get_rect(topleft=(col * TILE_SIZE, row * TILE_SIZE))
        self.letter = letter

class Board:
    def __init__(self):
        self.board_data = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def draw(self, screen):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(
                    screen,
                    color,
                    (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                )

    def place_tile(self, row, col, tile):
        if self.is_valid_move(row, col):
            self.board_data[row][col] = tile
            return True
        else:
            return False

    def is_valid_move(self, row, col):
        # Add your custom logic for checking if the move is valid
        return self.board_data[row][col] is None

# Initialize Pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrabble Board")

# Create a Scrabble board
scrabble_board = Board()

# Create a tile to be placed
sample_tile = Tile("A", 0, 0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = event.pos
                row = mouse_y // TILE_SIZE
                col = mouse_x // TILE_SIZE

                if scrabble_board.place_tile(row, col, sample_tile):
                    print(f"Tile placed at row {row}, col {col}")

    # Draw the board
    scrabble_board.draw(screen)

    # Draw the sample tile
    screen.blit(sample_tile.image, sample_tile.rect)

    # Update the display
    pygame.display.flip()
