from cell import Cell
from sudokugenerator import generate_sudoku
import pygame


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None
        # self.generator = SudokuGenerator(9, self.difficulty_to_removed_cells(difficulty))
        # self.board = self.generator.get_board()

        # Selects removed cells according to the difficulty level
        if difficulty == 0:
            removed_cells = 30
        elif difficulty == 1:
            removed_cells = 40
        else:
            removed_cells = 50

        self.board = generate_sudoku(9, removed_cells, self.cells) # Not sure if we can add another parameter (self.cells)

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
                                     (i * bs_dimensions + k * ss_dimensions,
                                      j * bs_dimensions + l * ss_dimensions,
                                      ss_dimensions, ss_dimensions), ss_line_width)


        # Why is this here?? lol
            # for i in range(len(self.cells)):
                # self.cells[i].draw()


    def select(self, row, col):
        index = row * 9 + col
        self.selected_cell = index

    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // (self.width // 9)
            col = x // (self.width // 9)
            return row, col
        else:
            return None

    def clear(self):

        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        """Places a number in the selected cell if it's valid according to Sudoku rules."""
        if self.selected_cell and self.selected_cell.value == 0:
            row, col = self.selected_cell.row, self.selected_cell.col
            if self.generator.is_valid(row, col, value):
                self.selected_cell.set_cell_value(value)
                self.update_board()

    def is_full(self):
        """Returns True if all cells in the board are filled, False if any are zero (empty)."""
        return all(cell.value != 0 for row in self.cells for cell in row)

    def update_board(self):
        """Synchronizes the GUI display with the internal board state."""
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set_cell_value(self.generator.board[i][j])

    def find_empty(self):
        """Finds and returns the coordinates of the first empty cell found, or None if full."""
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell.value == 0:
                    return (i, j)
        return None
        
    def check_board(self):
        """Checks if the board is correctly solved."""
        for i in range(9):
            row = [self.cells[i][j].value for j in range(9)]
            column = [self.cells[j][i].value for j in range(9)]
            box_row = (i // 3) * 3
            box_col = (i % 3) * 3
            box = [self.cells[box_row + x][box_col + y].value for x in range(3) for y in range(3)]
            if not (self.is_group_valid(row) and self.is_group_valid(column) and self.is_group_valid(box)):
                return False
        return True

    def is_group_valid(self, group):
        """Helper method to check if a group (row, column, or box) contains no duplicates and includes 1-9."""
        filtered = [num for num in group if num != 0]
        return len(filtered) == 9 and len(set(filtered)) == 9