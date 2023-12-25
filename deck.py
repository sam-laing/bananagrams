import helpers 
import random


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
        for letter, freq in helpers.DISTRIBUTION.items():
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
        
        
        

    
    
        

### Review inheritance, this seems messy

class PlayerDeck:
    def __init__(self, public_deck):
        init_deck = public_deck.grab(helpers.INITIAL_DECK_SIZE)
        self.deck = init_deck

    def peel(self, public_deck):
        '''
        grabs the desired number of tiles from public_deck
        one for each player for a peel and 3 for a dump
        '''
        if len(public_deck.pile) < 1:
            return None
        else:
            ret = public_deck.pile[-1]
            self.deck.append(ret)

    def dump(self, tile, public_deck):
        '''
        exchange current tile for 3 new tiles
        reshuffle the public deck afterwards
        '''
        if len(public_deck.pile) < 3:
            return tile
        else:
            self.deck.remove(tile)
            ret = public_deck.grab(3)
            self.deck.append(ret)
            random.shuffle(self.deck)




pile = PublicDeck(2)

print("the len is", len(pile.pile))
deck1 = PlayerDeck(pile)
print(len(deck1.deck))
deck1.peel(public_deck=pile)
print(len(deck1.deck))
print(len(pile.pile))
deck1.dump(deck1.deck[0], public_deck=pile)
print(len(deck1.deck))
print(len(pile.pile))

#print(deck.deck)
