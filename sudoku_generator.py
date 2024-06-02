import random

class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.board = [[0] * row_length for _ in range(row_length)]
        self.row_length = row_length
        self.removed_cells = removed_cells # (int) depends on difficulty
        self.box_length = 3

    def get_board(self):
        return(self.board)

    def print_board(self):
        print(self.board)

    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    # IMPORTANT: this function takes in the column index, not the column number itself
    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    # IMPORTANT: this function takes in the col and row start index, not the col and row start number itself
    def valid_in_box(self, cell_row, cell_col, num):
        
        row_start = (cell_row // 3) * 3
        col_start = (cell_col // 3) * 3
    
        for row in range(self.box_length):
            for col in range(self.box_length):
                if num == self.board[row + row_start][col + col_start]:
                    return False # Number is not valid if it appears in the same column
        return True
    
    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num)
    
    def fill_box(self, row_start, col_start):
        nums = [1,2,3,4,5,6,7,8,9]
        # This randomizes the order of the list of numbers; in order to reduce unecessary work.
        random.shuffle(nums) 

        for row in range(row_start, 3 + row_start):
            for col in range(col_start, 3 + col_start):
                number = nums.pop(0) # pop(0) removes the value in the first index and returns that value
                self.board[row][col] = number

    def fill_diagonal(self):

        self.fill_box(0,0)
        self.fill_box(3,3)
        self.fill_box(6,6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)


    def remove_cells(self):
        numbers = [i for i in range(81)]
        random.shuffle(numbers)

        for i in range(self.removed_cells):
                
            # Converts index to row and col
            col = numbers[i] % 9
            row = numbers[i] // 9

            self.board[row][col] = 0


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
