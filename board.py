from cell import Cell
from sudokugenerator import SudokuGenerator
import pygame


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None
        # self.generator = SudokuGenerator(9, self.difficulty_to_removed_cells(difficulty))
        # self.board = self.generator.get_board()
        pass

    def draw(self):
        # Let bs = big square and let ss = small square
        total_squares = 9
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
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (i * bs_dimensions, j * bs_dimensions, bs_dimensions, bs_dimensions),
                                 bs_line_width)

            # Smaller Squares
                for k in range(3):
                    for l in range(3):
                        pygame.draw.rect(self.screen, (0, 0, 0),
                                     (i * bs_dimensions + k * ss_dimensions, j * bs_dimensions + l * ss_dimensions, ss_dimensions, ss_dimensions), ss_line_width)

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
        if self.selected_cell and self.selected_cell.value == 0:
            if self.generator.is_valid(self.selected_cell.row, self.selected_cell.col, value):
                self.selected_cell.set_cell_value(value)
                self.update_board()
        pass

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True
        pass
        # Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set_cell_value(self.board[i][j])
        pass
        # Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell.value == 0:
                    return i, j
        return None
        pass
        # Finds an empty cell and returns its row and col as a tuple (x, y).
        
    def check_board(self):
        return self.generator.check_solution(self.board)
        pass
        # Check whether the Sudoku board is solved correctly.