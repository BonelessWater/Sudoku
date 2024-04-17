# Import new files here
from sudokugenerator import SudokuGenerator
from cell import Cell
from board import Board
from button import Button

# We will use pygame to display and interact with the board
import pygame

def main():
    pygame.init()

    easyButton = Button("EasyButton.png", 0, 900, 300, 100) # Button class is created
    normalButton = Button("NormalButton.png", 300, 900, 300, 100) # Button class is created
    hardButton = Button("HardButton.png", 600, 900, 300, 100) # Button class is created

    # CONSTANTS: 
    background_colour = (255, 255, 255) 

    width = 700  # in pixels (subject to change)
    height = 800  # in pixels (subject to change)
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption('Sudoku')

    screen.fill(background_colour)

    difficulty = 'easy'
    removed_cells = {'easy': 30, 'medium': 40, 'hard': 50}[difficulty]
    board = Board(width, height, screen, difficulty, removed_cells)


    button_width = width // 3
    button_height = height // 9
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
                    # removed_cells = {'easy': 30}
                    board = Board(width, height, screen, difficulty, removed_cells)
                    print("Easy button clicked!")
                    board.draw()
                elif normalButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 'medium'
                    # removed_cells = {'easy': 40}
                    board = Board(width, height, screen, difficulty, removed_cells)
                    print("Normal button clicked!")
                elif hardButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 'hard'
                    # removed_cells = {'easy': 50}
                    board = Board(width, height, screen, difficulty, removed_cells)
                    print("Hard button clicked!")
        if menu:
            easyButton.draw(screen)
            normalButton.draw(screen)
            hardButton.draw(screen)
        else:
            board.draw()
            # This should be the location of the game screen

        # Update the display using flip 
        pygame.display.flip()

    
    ### Pseudo code ###


    # Three main buttons:
    # If at ANY time user presses reset:
        # board returns to its initial state (keep a variable of the boards initial state for this purpose)
    # If at ANY time user presses restart:
        # User will return to the main menu
    # If at ANY time user presses Exit:
        # the program terminates
        # pygame.quit()
    


    # If user clicks on empty box:
        # sketch box

    # If user highlights a sketched box and presses enter:
        # user sumbits guess

if __name__ == "__main__":
    main()