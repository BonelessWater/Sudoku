# Import new files here
from sudokugenerator import SudokuGenerator
from cell import Cell
from board import Board
from button import Button

# We will use pygame to display and interact with the board
import pygame

def main():

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
                    difficulty = 0
                    board = Board(width, height, screen, difficulty)
                    print("Easy button clicked!")
                    board.draw()
                elif normalButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 1
                    board = Board(width, height, screen, difficulty)
                    print("Normal button clicked!")
                elif hardButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 2
                    board = Board(width, height, screen, difficulty)
                    print("Hard button clicked!")
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