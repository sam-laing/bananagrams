import helpers as h
import random
import pygame
from tile import Tile


class PublicDeck:
    def __init__(self, num_players):
        '''
        -> pile is a list of the availible tiles in the game
        initialized with the standard distribution of tiles and shuffled
        after grabbing tiles, they are deleted from the public deck
        -> num_players is the number of players in the game
        (this affects peels and dumps depending on remaining tiles)
        '''
        self.pile = []
        self.num_players = num_players
        for letter, freq in h.DISTRIBUTION.items():
            self.pile.extend(list(letter * freq))

        random.shuffle(self.pile)
            
    def grab(self, num):
        '''
        Params:
            num: the number of tiles to grab
        Actions:
            grabs the desired number of tiles from pile
            (one for each player for a peel and 3 for a dump)
        Returns:    
            the grabbed tiles or none if there are not enough tiles
        '''
        if len(self.pile) < num:
            return None
        else:
            grabbed = self.pile[-num:]
            del self.pile[-num:]
            return grabbed

class Player:
    def __init__(self, public_deck):
        init_deck = public_deck.grab(h.INITIAL_DECK_SIZE)
        self.deck = init_deck
        self.add_tile_sprites()

    def peel(self, public_deck):
        '''
        grabs a tile from public_deck.pile and adds it to the player's deck
        '''
        if len(public_deck.pile) < 1:
            return None
        else:
            ret = public_deck.pile[-1]
            del public_deck.pile[-1]
            self.deck.append(ret)

            self.add_tile_sprites()

    def dump(self, tile, public_deck):
        '''
        exchange current tile for 3 new tiles
        reshuffle the public deck afterwards
        '''
        if len(public_deck.pile) < 3:
            return None
        else:
            self.deck.remove(tile)
            ret = public_deck.grab(3)
            self.deck.extend(ret)
            self.add_tile_sprites()
            random.shuffle(self.deck)

    def add_tile_sprites(self):
        '''  
        given the player deck (as a list of strings), 
        convert each letter into 
        ''' 
        self.rack = []
        for i, letter in enumerate(self.deck):
            rect = pygame.Rect(i * h.TILE_SIZE, h.HEIGHT - h.TILE_SIZE, h.TILE_SIZE, h.TILE_SIZE)
            self.rack.append(Tile(letter, rect))






if __name__ == "__main__":
    pile = PublicDeck(2)

    print("the len is", len(pile.pile))
    deck1 = Player(pile)
    for i in range(10):
        print(len(deck1.deck) + len(pile.pile))
        deck1.peel(pile)
        print(len(deck1.deck) + len(pile.pile))

    #print(deck.deck)
