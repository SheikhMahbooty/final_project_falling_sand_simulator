import pygame
from simulation import Simulation

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 120
GREY = (29, 29, 29)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

while True:
    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        pos = pygame.mouse.get_pos()
        row = pos[1] // CELL_SIZE
        column = pos[0] // CELL_SIZE
        simulation.add_particle(row, column)
            
    #Updating state
    simulation.update()
    
    #Drawing
    window.fill(GREY)
    simulation.draw(window)
            
    pygame.display.flip()
    clock.tick(FPS)