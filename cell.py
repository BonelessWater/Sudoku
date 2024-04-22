import pygame


class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.font = pygame.font.SysFont("arial", 30)
        self.selected = False

    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value
    
    def draw(self):
        bs_dimensions = self.screen.get_width() // 3
        ss_dimensions = bs_dimensions // 3
        bs_line_width = 3
        ss_line_width = 1
        cell_width = bs_dimensions // 3
        cell_height = bs_dimensions // 3
        x = (self.col * ss_dimensions) + ss_line_width
        y = (self.row * ss_dimensions) + ss_line_width
        rect = pygame.Rect(x, y, cell_width, cell_height)


        if self.value != 0:
            text = self.font.render(str(self.value), True, pygame.Color('black'))
            text_rect = text.get_rect(center=(x + cell_width // 2, y + cell_height // 2))
            self.screen.blit(text, text_rect)


        if self.selected is True:
            pygame.draw.rect(self.screen, (255, 0, 0), rect, bs_line_width)
