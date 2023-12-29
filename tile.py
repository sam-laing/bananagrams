class Tile:
    def __init__(self, letter, rect):
        self.letter = letter
        self.rect = rect
        self.dragging = False
        self.img = None
    
    def __repr__(self) -> str:
        return self.letter 
    
if __name__ == "__main__":
    t = Tile("A", (0,0))
    print(t)



