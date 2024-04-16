import pygame
class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.font = pygame.font.Font(None, 11)
        pass

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value
        self.value = value
    
    def draw(self):
        cell_width = 60 # Assuming each cell is 60 pixels
        x = self.col * cell_width  
        y = self.row * cell_width
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, cell_width, cell_width))  # Draw cell background
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_width, cell_width), 3)  # Draw red border if selected
        text = self.font.render(str(self.value), True, (0, 0, 0))
        self.screen.blit(text, (x + 20, y + 15))