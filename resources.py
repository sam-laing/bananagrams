import pygame
import colors
import helpers



Scrabble_Tile_Font = "Futura40"
Tile_Size = (50, 50)


class ResourceManager:
    def __init__(self):
        self.fonts = {}
        self.tiles = {}

        self.init_tiles("./res/imgs/tile_resources.png")

    def init_tiles(self, fn):
        '''
        initialize self.tiles directory for lookup
        '''
        # loading tiles 
        self.tiles_map = pygame.image.load(fn)

        # load fonts
   
        # loading playable tiles



        pass

    def init_fonts(self):
        '''
        loads fonts into memory 
        '''
        for key, file, sizes in fonts_config:
            for size in sizes:
                self.fonts[key + str(size)] = pygame.font.Font("./res/fonts/" + file, size)