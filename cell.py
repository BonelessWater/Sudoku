import pygame

class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.width = screen.get_width()
        self.selected = False
        self.font = pygame.font.SysFont("arial", 30)

    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value
        self.value = value
    
    def draw(self):
        cell_width = self.width / 9
        x = self.col * cell_width  
        y = self.row * cell_width

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_width, cell_width), 3)  # Draw red border if selected

        text = self.font.render(str(self.value), True, (0, 0, 0))
        temp_surface = pygame.Surface(text.get_size())
        temp_surface.fill((255, 255, 255))
        temp_surface.blit(text, (x + 20, y + 15))

        self.screen.blit(temp_surface, (x + 20, y + 15))
        self.screen.blit(text, (x + 20, y + 15))