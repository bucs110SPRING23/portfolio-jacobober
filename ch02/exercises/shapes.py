import pygame

pygame.init()

pygame.event.get()

screen = pygame.display.set_mode()

dimensions = screen.get_size() # [width, and height]

starting_point = (dimensions[0] // 2, dimensions[1] // 2)

#draw library

#For circle we need to tell it:
#Where to draw it
#Color: "red", [r,g,b] => [0-255, 0-255, 0-255]
#starting point: [x, y]
#radius: 50

radius = 200

pygame.draw.circle(screen, "light blue", starting_point, radius)
    
starting_point[1] = starting_point[1] - radius
radius = radius // 2
starting_point[1] = starting_point[1] - radius


pygame.display.flip()
pygame.time.wait(5000)