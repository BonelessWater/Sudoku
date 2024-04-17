import pygame

class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.font = pygame.font.SysFont("arial", 30)
        self.selected = False
        # self.value = value
        # self.row = row
        # self.col = col
        # self.screen = screen
        # self.width = screen.get_width()
        # self.selected = False
        # self.font = pygame.font.SysFont("arial", 30)

    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value
    
    def draw(self):
        cell_width = self.screen.get_width() // 9
        cell_height = self.screen.get_height() // 9
        x = self.col * cell_width
        y = self.row * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)

        # Code for drawing the cell background and border
        pygame.draw.rect(self.screen, pygame.Color('white'), rect, 0)  # Fill cell background
        pygame.draw.rect(self.screen, pygame.Color('black'), rect, 1)  # Cell border
        # cell_width = self.width / 9
        # x = self.col * cell_width
        # y = self.row * cell_width

        # x = self.col * (self.screen.get_width() // 9)
        # y = self.row * (self.screen.get_height() // 9)
        # rect = pygame.Rect(x, y, self.screen.get_width() // 9, self.screen.get_height() // 9)
        # pygame.draw.rect(self.screen, pygame.Color('white'), rect, 0)  # Fill cell background
        # pygame.draw.rect(self.screen, pygame.Color('black'), rect, 1

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)
            # pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_width, cell_width), 3)  # Draw red border if selected

        if self.value != 0:
            text = self.font.render(str(self.value), True, pygame.Color('black'))
            text_rect = text.get_rect(center=(x + cell_width // 2, y + cell_height // 2))
            self.screen.blit(text, text_rect)

        # text = self.font.render(str(self.value), True, (0, 0, 0))
        # temp_surface = pygame.Surface(text.get_size())
        # temp_surface.fill((255, 255, 255))
        # temp_surface.blit(text, (x + 20, y + 15))
        #
        # self.screen.blit(temp_surface, (x + 20, y + 15))
        # self.screen.blit(text, (x + 20, y + 15))