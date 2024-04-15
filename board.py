from sudokugenerator import SudokuGenerator
from cell import Cell


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
        row, col = y // 60, x // 60
        if 0 <= row < 9 and 0 <= col < 9:
            self.select(row, col)
        pass

    def clear(self, x, y):
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_sketched_value(0)
        pass

    def sketch(self, value):
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_sketched_value(value)
        pass

    def place_number(self, value):
        if self.selected_cell and self.selected_cell.value == 0:
            if self.generator.is_valid(self.selected_cell.row, self.selected_cell.col, value):
                self.selected_cell.set_cell_value(value)
                self.update_board()
        pass

    def is_full(self):
        return all(cell.value != 0 for row in self.cells for cell in row)
        pass
        #Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].value = self.board[i][j]
        pass
        #Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return i, j
        return None
        pass
        #Finds an empty cell and returns its row and col as a tuple (x, y).
        
    def check_board(self):
        for i in range(9):
            if not self.check_row(i) or not self.check_col(i) or not self.check_box(i // 3 * 3, i % 3 * 3):
                return False
        return True
        pass
        #Check whether the Sudoku board is solved correctly. 