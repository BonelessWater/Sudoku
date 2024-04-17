from cell import Cell
from sudokugenerator import generate_sudoku
import pygame

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.generator = generate_sudoku(9, {'easy': 30, 'medium': 40, 'hard': 50}[difficulty])
        self.cells = [[Cell(self.generator[i][j], i, j, screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None

        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("arial", 11)

        

    def draw(self):
         # Let bs = big square and let ss = small square
        bs_dimensions = self.width // 3
        ss_dimensions = bs_dimensions // 3
        bs_line_width = 3
        ss_line_width = 1

        # PyGame states: rect(surface, color, rect, width=0,
        # border_radius=0, border_top_left_radius=-1,
        # border_top_right_radius=-1, border_bottom_left_radius=-1,
        # border_bottom_right_radius=-1)

        # Bigger Squares
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(self.screen, (0, 0, 0),(i * bs_dimensions, j * bs_dimensions, bs_dimensions, bs_dimensions), bs_line_width)
                for k in range(3):
                    for l in range(3):
                        pygame.draw.rect(self.screen, (0, 0, 0), (i * bs_dimensions + k * ss_dimensions, j * bs_dimensions + l * ss_dimensions, ss_dimensions, ss_dimensions), ss_line_width)

        # Smaller Squares
        for k in range(3):
            for l in range(3):
                pygame.draw.rect(self.screen, (0, 0, 0), (
                i * bs_dimensions + k * ss_dimensions,
                j * bs_dimensions + l * ss_dimensions, ss_dimensions,
                ss_dimensions), ss_line_width);

        for row in self.cells:
             for cell in row:
                 cell.draw()
        # for row in range(9):
        #     for col in range(9):
        #         self.cells[row][col].draw()
        
    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // (self.width // 9)
            col = x // (self.width // 9)
            return row, col
        else:
            return None

    def clear(self, x, y):
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_cell_value(0)
            self.update_board()
        pass

    def sketch(self, value):
        if self.selected_cell and 0 < value <= 9:
            self.selected_cell.set_sketched_value(value)
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
        #Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        """
            Synchronizes the GUI representation of each cell with the underlying data structure of the board.
            This method is typically called after a value is placed to ensure the display matches the data.
            """
        for row in self.cells:
            for cell in row:
                cell.set_cell_value(cell.value)

        # for i in range(9):
        #     for j in range(9):
        #         self.cells[i][j].set_cell_value(self.board[i][j])
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
                    return (i, j)
        return None
        #Finds an empty cell and returns its row and col as a tuple (x, y).
        
    def check_board(self):
        """Checks if the board is correctly solved."""
        for i in range(9):
            row = [cell.value for cell in self.cells[i]]
            # row = [self.cells[i][j].value for j in range(9)]
            column = [self.cells[j][i].value for j in range(9)]
            box_row = (i // 3) * 3
            box_col = (i % 3) * 3
            box = [self.cells[box_row + x][box_col + y].value for x in range(3) for y in range(3)]
            if not (self.is_group_valid(row) and self.is_group_valid(column) and self.is_group_valid(box)):
                return False
        return True

    def is_group_valid(self, group):
        """Helper method to check if a group (row, column, or box) contains no duplicates and includes 1-9."""
        return len(set(group)) == 9 and all(group)
        # filtered = [num for num in group if num != 0]
        # return len(filtered) == 9 and len(set(filtered)) == 9