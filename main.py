import pygame
import random
from Cell import Cell

# Set window dimensions
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
NUM_ROWS = 20
NUM_COLS = 20
CELL_SIZE = 40

# Set window title
pygame.display.set_caption("Game of Life")

# Set color values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set update speed
FPS = 60

def create_cells(size, numrows, numcols):
    cells = []

    for i in range(numrows):
        for j in range(numcols):
            r = random.randint(1,5)
            if r == 1:
                alive = False
            else:
                alive = True
            cells.append(Cell(i, j, size, alive))

    return cells

def get_cell_index(r, c):
    """ Return index of CELLS array based on the given row and col """
    return r * NUM_COLS + c


CELLS = create_cells(size=CELL_SIZE, numrows=NUM_ROWS, numcols=NUM_COLS)

def set_cell_behaviors():
    # Loop through CELLS array
    for cell in CELLS:
        living_neighbors = 0

        # Northwest neighbor
        if cell.col > 0 and cell.row > 0:
            # if neighbor alive: add to living_neigh
            if CELLS[get_cell_index(cell.row-1, cell.col-1)].is_alive():
                living_neighbors += 1
        # North neighbor
        if cell.row > 0:
            # if neighbor alive: add to living_neigh
            if CELLS[get_cell_index(cell.row-1, cell.col)].is_alive():
                living_neighbors += 1
        # Northeast neighbor
        if cell.col < NUM_COLS-1 and cell.row > 0:
            # if neighbor alive: add to living_neigh
            if CELLS[get_cell_index(cell.row-1, cell.col+1)].is_alive():
                living_neighbors += 1
        # West neighbor
        if cell.col > 0:
            # if neighbor alive: add to living_neigh
            if CELLS[get_cell_index(cell.row, cell.col-1)].is_alive():
                living_neighbors += 1
        # East neighbor
        if cell.col < NUM_COLS-1:
            # if neighbor alive: add to living_neigh
            if CELLS[get_cell_index(cell.row, cell.col+1)].is_alive():
                living_neighbors += 1
        # Southwest neighbor
        if cell.col > 0 and cell.row < NUM_ROWS-1:
            # if neighbor alive: add to living_neigh
            if CELLS[get_cell_index(cell.row+1, cell.col-1)].is_alive():
                living_neighbors += 1
        # South neighbor
        if cell.row < NUM_ROWS-1:
            # if neighbor alive: add to living_neigh
            if CELLS[get_cell_index(cell.row+1, cell.col)].is_alive():
                living_neighbors += 1
        # Southeast neighbor
        if cell.col < NUM_COLS-1 and cell.row < NUM_ROWS-1:
            # if neighbor alive: add to living_neigh
            if CELLS[get_cell_index(cell.row+1, cell.col+1)].is_alive():
                living_neighbors += 1

        # Determine what each cell will do in the next frame
        if cell.is_alive():
            if living_neighbors < 2 or living_neighbors > 3:
                cell.nextgen = False
            else:
                cell.nextgen = True
        else:
            if living_neighbors == 3:
                cell.nextgen = True
            else:
                cell.nextgen = False

        

def game_scene():
    WINDOW.fill(WHITE)
    # Draw each cell
    for cell in CELLS:
        cell.draw_self(WINDOW)

    # Update display
    pygame.display.update()

def main():

    # Clock object to control game speed
    clock = pygame.time.Clock()

    run = True
    while run:
        # Next frame
        clock.tick(FPS)

        for event in pygame.event.get():
            # Check if user quits window
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    set_cell_behaviors()
                    for cell in CELLS:
                        cell.prevgen = cell.alive
                        cell.alive = cell.nextgen
                elif event.key == pygame.K_BACKSPACE:
                    for cell in CELLS:
                        cell.nextgen = cell.alive
                        cell.alive = cell.prevgen

        game_scene()
    
    pygame.quit()



if __name__ == '__main__':
    main()
