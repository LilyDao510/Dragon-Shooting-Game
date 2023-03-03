import pygame

from world import world

pygame.init()
clock = pygame.time.Clock()

if __name__ == '__main__':
    while True:
        
        world.check_event()
        
        if world.active == False:
            world.draw_start_screen()
        if world.active == True:    
            world.update()
        
        pygame.display.flip() # Chay man hinh
        clock.tick(60)