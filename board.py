
class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None
        self.generator = SudokuGenerator(9, self.difficulty_to_removed_cells(difficulty))
        self.board = self.generator.get_board()
        pass

    def draw(self):
        pass

    def select(self, row, col):
        pass

    def click(self, row, col):
        pass

    def clear(self, x, y):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def is_full(self):
        pass
        #Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        pass
        #Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        pass
        #Finds an empty cell and returns its row and col as a tuple (x, y).
        
    def check_board(self):
        pass
        #Check whether the Sudoku board is solved correctly. 