# Import new files here
from sudokugenerator import SudokuGenerator
from cell import Cell
from board import Board
from button import Button

# We will use pygame to display and interact with the board
import pygame

def main():
    pygame.init()
    pygame.font.init()

    # CONSTANTS: 
    background_colour = (255, 255, 255) 

    width = 700  # in pixels (subject to change)
    height = 800  # in pixels (subject to change)
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption('Sudoku')

    screen.fill(background_colour)

    button_width = screen.get_width() // 3
    button_height = screen.get_height() // 9
    button_y_location = height - button_height
    
    easyButton = Button("EasyButton.png", 0, button_y_location, button_width, button_height)
    normalButton = Button("NormalButton.png", button_width, button_y_location, button_width, button_height)
    hardButton = Button("HardButton.png", 2 * button_width, button_y_location, button_width, button_height)

    # Game status will switch to false when the user wins or loses
    game_status = menu = True
    while game_status:
        for event in pygame.event.get(): 
      
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                game_status = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = pygame.mouse.get_pos()
                if easyButton.is_clicked(mouse_pos) and menu: # The menu variable will become false when user selects a difficulty
                    menu = False
                    difficulty = 'easy'
                    board = Board(width, height, screen, difficulty)
                    print("Easy button clicked!")
                    board.draw()
                elif normalButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 'medium'
                    board = Board(width, height, screen, difficulty)
                    print("Normal button clicked!")
                elif hardButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 'hard'
                    board = Board(width, height, screen, difficulty)
                    print("Hard button clicked!")

                # Code based on TA help ----
                elif event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    screen.fill((255, 255, 255))

                    # NOTE: THIS IS WHERE WE WILL REPLACE THE BUTTONS WITH RESET, QUIT, ETC.
                    easyButton.draw(screen)
                    normalButton.draw(screen)
                    hardButton.draw(screen)

                    if board.click(x, y) is not None:
                        x, y = board.click(x, y)
                        for row in range(9):
                            for col in range(9):
                                if (row, col) != (x, y):
                                    board.cells[row][col].selected = False
                            board.cells[x][y].selected = True
                        board.draw()



        if menu:
            easyButton.draw(screen)
            normalButton.draw(screen)
            hardButton.draw(screen)
        else:
            board.draw()

            # Add additional buttons here:

            # These buttons should change the value of Menu to False or close the game

        # Update the display using flip 
        pygame.display.flip()

    

if __name__ == "__main__":
    main()