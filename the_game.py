import pygame 
from board import BoardClass
import resources as res
import colors
import helpers as h
from deck import PublicDeck, Player
from tile import Tile 



pygame.init()
FONT = pygame.font.Font(None, 36)
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((h.WIDTH, h.HEIGHT))
        pygame.display.set_caption("Bananagrams")

        self.board_class = BoardClass()
        self.selected_tile = None
        self.public_deck = PublicDeck(1)
        self.player = Player(self.public_deck)
        # add a button to peel
        # add a button to dump
        
        # adding a peel button 
        self.peel_button_x_pos = 17 * h.TILE_SIZE 
        self.peel_button_y_pos = 17 * h.TILE_SIZE
        self.peel_button_width = h.WIDTH - self.peel_button_x_pos
        self.peel_button_height = (h.HEIGHT - self.peel_button_y_pos) / 2

        # adding a dump button
        self.dump_button_x_pos = h.GRID_SIZE * h.TILE_SIZE
        self.dump_button_y_pos = h.GRID_SIZE * h.TILE_SIZE + self.peel_button_height
        self.dump_button_width = h.WIDTH - self.dump_button_x_pos
        self.dump_button_height = (h.HEIGHT - self.peel_button_y_pos) / 2

        self.running = True
        while self.running:
            self.handle_events()
            self.draw_board()
            self.draw_peel_button()
            self.draw_dump_button()
            self.draw_player_deck()


            pygame.display.flip()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_down(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_up()

    def handle_mouse_down(self, mouse_pos):
        # Check if a tile on the rack is clicked
        for tile in self.player.rack:
            if tile.rect.collidepoint(mouse_pos):
                tile.dragging = not tile.dragging
                if tile.dragging:
                    self.selected_tile = tile
                else:
                    self.selected_tile = None
                return



        # Check if a tile on the board is clicked
        for row in range(h.GRID_SIZE):
            for col in range(h.GRID_SIZE):
                tile_rect = pygame.Rect(col * h.TILE_SIZE, row * h.TILE_SIZE, h.TILE_SIZE, h.TILE_SIZE)
                if self.board_class.board[row][col] != ' ' and tile_rect.collidepoint(mouse_pos):
                    # Place the selected tile back into the rack
                    letter = self.board_class.board[row][col]
                    rect = pygame.Rect(len(self.player.rack) * h.TILE_SIZE, h.HEIGHT - h.TILE_SIZE, h.TILE_SIZE, h.TILE_SIZE)
                    self.selected_tile = Tile(letter, rect, dragging = True)
                    self.player.deck.append(self.selected_tile.letter)
                    self.player.add_tile_sprites()
                    self.board_class.board[row][col] = ' '  # Remove the tile from the board
                    return
        
        if pygame.Rect(self.peel_button_x_pos, self.peel_button_y_pos, self.peel_button_width, self.peel_button_height).collidepoint(mouse_pos):
            self.player.peel()
            print(f"number of tiles in the deck: {len(self.player.rack)}")
            return
        


        # need to add dump logic here... more complicated

    def handle_mouse_motion(self, mouse_pos):
        # Move the selected tile with the mouse
        if self.selected_tile and self.selected_tile.dragging:
            self.selected_tile.rect.x, self.selected_tile.rect.y = mouse_pos

    def handle_mouse_up(self):
        # Drop the selected tile onto the board
        if self.selected_tile:
            for row in range(h.GRID_SIZE):
                for col in range(h.GRID_SIZE):
                    if self.board_class.board[row][col] == ' ' and self.selected_tile.rect.colliderect(pygame.Rect(col * h.TILE_SIZE, row * h.TILE_SIZE, h.TILE_SIZE, h.TILE_SIZE)):
                        self.board_class.board[row][col] = self.selected_tile.letter
                        self.selected_tile.dragging = False
                        self.player.deck.remove(self.selected_tile.letter)
                        self.player.add_tile_sprites()
                        self.selected_tile = None
                        return
            # If not dropped on the board, return it to the rack
            self.selected_tile.dragging = False
            self.selected_tile = None

    def draw_peel_button(self):
        pygame.draw.rect(
            self.screen, colors.GREEN, 
            pygame.rect.Rect(
                self.peel_button_x_pos, self.peel_button_y_pos, 
                self.peel_button_width, self.peel_button_height
            )
        )
        text = FONT.render("PEEL!", True, colors.BLACK)
        self.screen.blit(text, (self.peel_button_x_pos + 10, self.peel_button_y_pos + 10))
    
    def draw_dump_button(self):
        pygame.draw.rect(
            self.screen, colors.RED, 
            pygame.rect.Rect(self.dump_button_x_pos, self.dump_button_y_pos, 
                             self.dump_button_width, self.dump_button_height
            )
        )

        text = FONT.render("DUMP!", True, colors.BLACK)
        self.screen.blit(text, (self.dump_button_x_pos + 10, self.dump_button_y_pos + 10))

    def draw_player_deck(self):
        for i, tile in enumerate(self.player.rack):
            pygame.draw.rect(self.screen, colors.GRAY, tile.rect, 1)
            text = FONT.render(tile.letter, True, colors.BLACK)
            self.screen.blit(text, (tile.rect.x + h.TILE_SIZE // 3 , tile.rect.y + h.TILE_SIZE // 6))

    def draw_board(self):
        self.screen.fill(colors.WHITE)

        for row in range(h.GRID_SIZE):
            for col in range(h.GRID_SIZE):
                pygame.draw.rect(self.screen, colors.GRAY, (col * h.TILE_SIZE, row * h.TILE_SIZE, h.TILE_SIZE, h.TILE_SIZE), 1)
                text = FONT.render(self.board_class.board[row][col], True, colors.BLACK)
                self.screen.blit(text, (col * h.TILE_SIZE + h.TILE_SIZE // 3, row * h.TILE_SIZE + h.TILE_SIZE // 3))



    
if __name__ == "__main__":  
    g = Game()
