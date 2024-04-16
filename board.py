from cell import Cell
from sudokugenerator import generate_sudoku

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None
        # Selects removed cells according to the difficulty level
        if difficulty == 0:
            removed_cells = 30
        elif difficulty == 1:
            removed_cells = 40
        else:
            removed_cells = 50

        self.board = generate_sudoku(9, removed_cells, self.cells) # Not sure if we can add another parameter (self.cells)
        
    def draw(self):
        for i in range(len(self.cells)):
            self.cells[i].draw()

    def select(self, row, col):
        index = row * 9 + col
        self.selected_cell = index

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        if self.selected_cell and self.selected_cell.value == 0:
            if self.generator.is_valid(self.selected_cell.row, self.selected_cell.col, value):
                self.selected_cell.set_cell_value(value)
                self.update_board()

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False     
        return True
        #Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set_cell_value(self.board[i][j])
        #Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell.value == 0:
                    return i, j
        return None
        #Finds an empty cell and returns its row and col as a tuple (x, y).
        
    def check_board(self):
        return self.generator.check_solution(self.board)
        #Check whether the Sudoku board is solved correctly. 