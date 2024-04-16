class Cell:

    def __init__(self, value, row, col, screen):

        self.sketched_value = -1 # Initially set to negative one because this is an invalid number in the real game
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value 
        # I dont understand why the pdf tells us to take in a value.
        # My intuition tells me that it should just use the sketched value 
        # because the user has to set a sketched value before permanently setting it.

    def set_sketched_value(self, value):
        self.sketched_value = value
    
    def draw(self):
        # width and height of the cell is determined by the screen information
        width = self.screen.get_width()
        height = self.screen.get_height()

        # Must use row and column index to position the cell (cedric plis clutch up)