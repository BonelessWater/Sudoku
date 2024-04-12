

class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        # Row length is always 9
        self.row_length = removed_cells
        self.removed_cells = removed_cells

    def get_board(self):
        # Literally jsut returns the board
        pass

    def print_board(self):
        pass
        #prints the board

    def valid_in_row(self, row, num):
        # Returns boolean; returns true if a number is valid in its given row
        pass

    def valid_in_col(self, col, num):
        # Returns boolean; returns true if a number is valid in its given col
        pass

    def valid_in_box(self, row_start, col_start, num):
        pass

    def is_valid(self, row, col, num):
        # returns boolean; returns true if a number is valid in its col, row and respective 3x3 box
        pass

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        pass

    def fill_remaining(self, row, col):
        pass

    def fill_values(self):
        pass

    def remove_cells(self):
        pass

    def generate_sudoku(size, removed):
        pass