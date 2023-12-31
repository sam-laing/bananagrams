class Tile:
    def __init__(self, letter, rect, dragging=False):
        self.letter = letter
        self.rect = rect
        self.dragging = dragging
        self.img = None
    
    def __repr__(self) -> str:
        return self.letter 
    
if __name__ == "__main__":
    mini_board = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(Tile("A", (0,0)))
        mini_board.append(row)
    print(mini_board)



