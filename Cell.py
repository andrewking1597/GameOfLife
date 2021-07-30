import pygame

class Cell:
    def __init__(self, row, col, size, alive=True):
        self.row = row
        self.col = col
        self.size = size
        self.rect = pygame.Rect(col*size, row*size, size, size)
        self.alive = alive
        self.nextgen = alive # stay the same by default
        self.prevgen = alive # stay the same by default

    def draw_self(self, surface):
        if self.alive:
            pygame.draw.rect(surface, (255, 255, 255), self.rect)
        else:
            pygame.draw.rect(surface, (0, 0, 0), self.rect)

    def is_alive(self):
        return self.alive
        
