# Import new files here
from sudokugenerator import SudokuGenerator
from cell import Cell
from board import Board
from button import Button

# We will use pygame to display and interact with the board
import pygame


pygame.init()
pygame.font.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)
GRAY = (200, 200, 200)

def draw_button(surface, color, x, y, width, height, text, text_color=BLACK):
    
    pygame.draw.rect(surface, color, (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    surface.blit(text_surface, text_rect)

def main():
    
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

    resetButton = Button("EasyButton.png", 0, button_y_location, button_width, button_height)
    restartButton = Button("NormalButton.png", button_width, button_y_location, button_width, button_height)
    quitButton = Button("HardButton.png", 2 * button_width, button_y_location, button_width, button_height)


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
                    initial_board = board
                    print("Easy button clicked!")
                    board.draw()
                elif normalButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 'medium'
                    board = Board(width, height, screen, difficulty)
                    initial_board = board
                    print("Normal button clicked!")
                elif hardButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 'hard'
                    board = Board(width, height, screen, difficulty)
                    initial_board = board
                    print("Hard button clicked!")
        
        if menu:
            # Should draw a full menu every time. Until this is done. The restart button will not work properly
            # Needs designing

            easyButton.draw(screen)
            normalButton.draw(screen)
            hardButton.draw(screen)
        else:

            restart_button_rect = pygame.Rect(0, button_y_location, button_width, button_height)
            draw_button(screen, GRAY, restart_button_rect.x, restart_button_rect.y, restart_button_rect.width, restart_button_rect.height, "Restart")
            
            reset_button_rect = pygame.Rect(button_width, button_y_location, button_width, button_height)
            draw_button(screen, GRAY, reset_button_rect.x, reset_button_rect.y, reset_button_rect.width, reset_button_rect.height, "Reset")
            
            quit_button_rect = pygame.Rect(2 * button_width, button_y_location, button_width, button_height)
            draw_button(screen, GRAY, quit_button_rect.x, quit_button_rect.y, quit_button_rect.width, quit_button_rect.height, "Quit")
            
            board.draw()

            last_cell = [-1, -1] # this variable will keep track of selected cell
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    game_status = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if the mouse click is on the buttons
                    if restart_button_rect.collidepoint(mouse_pos):
                        print("Restart button clicked!")
                        menu = True
                    elif reset_button_rect.collidepoint(mouse_pos):
                        print("Reset button clicked!")
                        board = initial_board
                    elif quit_button_rect.collidepoint(mouse_pos):
                        print("Quit button clicked!")
                        game_status = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        screen.fill((255, 255, 255))

                        # NOTE: THIS IS WHERE WE WILL REPLACE THE BUTTONS WITH RESET, QUIT, ETC.
                        easyButton.draw(screen)
                        normalButton.draw(screen)
                        hardButton.draw(screen)

                        if board.click(x, y) is not None:

                            # Cover over the last selected cell:
                            if last_cell != [-1,-1]:
                                board.cells[last_cell[0]][last_cell[1]].selected = False 

                            mouse_row, mouse_col = board.click(x, y) # board.click() returns the row and col of a click
                            board.cells[mouse_row][mouse_col].selected = True

            # Add additional buttons here:

            # These buttons should change the value of Menu to False or close the game

        # Update the display using flip 
        pygame.display.flip()

    

if __name__ == "__main__":
    main()