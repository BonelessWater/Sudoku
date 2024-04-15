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
        pass

    def set_sketched_value(self, value):
        self.value = value
        pass
    
    def draw(self):
        x = self.col * 60  # Assuming each cell is 60 pixels
        y = self.row * 60
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, 60, 60))  # Draw cell background
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, 60, 60), 3)  # Draw red border if selected
        text = self.font.render(str(self.value), True, (0, 0, 0))
        self.screen.blit(text, (x + 20, y + 15))
        pass