# Import new files here 
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
width = 700
height = 800

def draw_button(surface, color, x, y, width, height, text, text_color=BLACK):
    
    pygame.draw.rect(surface, color, (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    surface.blit(text_surface, text_rect)


def main():
    
    key_presses = {
        pygame.K_1: 1,
        pygame.K_2: 2,
        pygame.K_3: 3,
        pygame.K_4: 4,
        pygame.K_5: 5,
        pygame.K_6: 6,
        pygame.K_7: 7,
        pygame.K_8: 8,
        pygame.K_9: 9,
    }

    # CONSTANTS: 
    pygame.init()
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
    main_background_picture = pygame.image.load('background.jpeg')
    main_background_picture = pygame.transform.scale(main_background_picture, (width, height))
    mainbuffer = pygame.Surface((width, height))
    while game_status:
        mainbuffer.fill((255,255,255))
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
                    initial_board_nums = board.generator
                    print("Easy button clicked!")
                    board.draw()
                elif normalButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 'medium'
                    board = Board(width, height, screen, difficulty)
                    initial_board = board
                    initial_board_nums = board.generator
                    print("Normal button clicked!")
                elif hardButton.is_clicked(mouse_pos) and menu:
                    menu = False
                    difficulty = 'hard'
                    board = Board(width, height, screen, difficulty)
                    initial_board = board
                    initial_board_nums = board.generator
                    print("Hard button clicked!")

        if menu:
            mainbuffer.blit(main_background_picture, (0,0))
            easyButton.draw(mainbuffer)
            normalButton.draw(mainbuffer)
            hardButton.draw(mainbuffer)
            # screen.blit(mainbuffer, (0,0,))
            width = 700  # in pixels (subject to change)
            height = 800  # in pixels (subject to change)
            pygame.display.set_caption('Sudoku')
            font_type = pygame.font.Font('text.ttf', 32)
            message_displayed = font_type.render("Welcome to Sudoku!!", True, BLACK)
            mainbuffer.blit(message_displayed,(190,200))
            screen.blit(mainbuffer,(0,0))

            easyButton.draw(screen)
            normalButton.draw(screen)
            hardButton.draw(screen)

        else:

            screen.fill((255,255,255))

            board.draw()

            if board.is_full() and board.check_board():
                game_won = pygame.image.load('wongame.jpg')
                game_won = pygame.transform.scale(game_won, (width, height))
                screen.blit(game_won, (0,0))
                pygame.display.set_caption('Game won!')
                font_type = pygame.font.Font('text.ttf', 50)
                message_displayed = font_type.render("Game Won!", True, BLACK)
                screen.blit(message_displayed, (210,380))

            elif board.is_full() and not board.check_board():
                game_lost = pygame.image.load('background.jpeg')
                game_lost = pygame.transform.scale(game_lost, (width, height))
                screen.blit(game_lost, (0,0))
                pygame.display.set_caption('Game lost :(')
                font_type = pygame.font.Font('text.ttf', 50)
                message_displayed = font_type.render("Game Lost :(", True, BLACK)
                screen.blit(message_displayed, (190,120))
            
            restart_button_rect = pygame.Rect(0, button_y_location, button_width, button_height)
            draw_button(screen, GRAY, restart_button_rect.x, restart_button_rect.y, restart_button_rect.width, restart_button_rect.height, "Restart")

            reset_button_rect = pygame.Rect(button_width, button_y_location, button_width, button_height)
            draw_button(screen, GRAY, reset_button_rect.x, reset_button_rect.y, reset_button_rect.width, reset_button_rect.height, "Reset")

            quit_button_rect = pygame.Rect(2 * button_width, button_y_location, button_width, button_height)
            draw_button(screen, GRAY, quit_button_rect.x, quit_button_rect.y, quit_button_rect.width, quit_button_rect.height, "Quit")

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    game_status = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if the mouse click is on the buttons
                    if restart_button_rect.collidepoint(mouse_pos):
                        print("Restart button clicked!")
                        menu = True
                        screen.fill(WHITE)
                    elif reset_button_rect.collidepoint(mouse_pos):
                        print("Reset button clicked!")
                        for row in range(9):
                            for col in range(9):
                                board.cells[row][col].set_cell_value(initial_board_nums[row][col])
                                if initial_board_nums[row][col] == 0:
                                    board.cells[row][col].set_sketched_value(0)
                        board.draw()
                    elif quit_button_rect.collidepoint(mouse_pos):
                        print("Quit button clicked!")
                        game_status = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        screen.fill((255, 255, 255))

                        if board.click(x, y) is not None:
                            mouse_row, mouse_col = board.click(x, y)
                            for row in range(9):
                                for col in range(9):
                                    if (row, col) != (mouse_row, mouse_col):
                                        board.cells[row][col].selected = False
                            if initial_board_nums[mouse_row][mouse_col] == 0:
                                board.cells[mouse_row][mouse_col].selected = True
                            board.draw()   

                elif event.type == pygame.KEYDOWN:
                    if event.key in key_presses:
                        board.sketch(key_presses[event.key])
                    elif event.key == pygame.K_RETURN:
                        print(board.selected_cell.sketched_value)
                        board.place_number(board.selected_cell.sketched_value)

        # Update the display using flip 
        pygame.display.flip()

if __name__ == "__main__":
    main()