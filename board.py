from cell import Cell
from sudokugenerator import SudokuGenerator

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.generator = SudokuGenerator(9, {'easy': 20, 'medium': 40, 'hard': 60}[difficulty])
        self.cells = [[Cell(self.generator.board[i][j], i, j, screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None
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
        """
            Places a number into the currently selected cell if the placement is valid according to Sudoku rules.
            It verifies that placing the value does not violate any constraints in the row, column, or box.

            Args:
            value (int): The value to be placed in the selected cell.

            """
        if self.selected_cell and self.selected_cell.value == 0:
            if self.generator.is_valid(self.selected_cell.row, self.selected_cell.col, value):
                self.selected_cell.set_cell_value(value)
                self.update_board()
        pass

    def is_full(self):
        """
            Determines whether all cells in the board are filled (i.e., no cells have a value of 0).

            Returns:
            bool: True if all cells are filled, False otherwise.
            """
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True
        pass
        #Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        """
            Synchronizes the GUI representation of each cell with the underlying data structure of the board.
            This method is typically called after a value is placed to ensure the display matches the data.
            """
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set_cell_value(self.board[i][j])
        pass
        #Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        """
            Finds the first empty cell in the board and returns its location.

            Returns:
            tuple or None: Returns the row and column as a tuple (row, col) of the first empty cell found, or None if all cells are filled.
            """
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell.value == 0:
                    return i, j
        return None
        pass
        #Finds an empty cell and returns its row and col as a tuple (x, y).
        
    def check_board(self):
        """
            Checks if the current board setup is a correct solution according to Sudoku rules.
            It ensures that each row, column, and 3x3 box contains all numbers from 1 to 9 without any repetitions.

            Returns:
            bool: True if the board is correctly solved, False otherwise.
            """
        return self.generator.check_solution(self.board)
        pass
        #Check whether the Sudoku board is solved correctly. 