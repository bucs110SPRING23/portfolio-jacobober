import random
import pygame
import math

#Part A
pygame.init()
while 1:
    pygame.event.pump()
    screen = pygame.display.set_mode((800,800))
    screen_size = pygame.display.get_window_size()
    print(screen_size[0], screen_size [1])
    width = screen_size[0]
    #1440 width by 900 height
    center_point = (screen_size[0] // 2, screen_size[1] // 2)
    screen.fill("orange")
    pygame.draw.circle(screen, "light blue", center_point, screen_size[1] / 2)
    pygame.draw.circle(screen, "black", center_point, screen_size[1] / 2, 5)
    # pygame.draw.line(screen, "black", [screen_size[0] / 2, 0], [screen_size[1] / 2, 0])
#Part B
    # pygame.display.flip()
    # pygame.time.wait(6000)
    
    for throw in range(10):
        randomX = random.randrange(0, screen_size[0])
        randomY = random.randrange(0, screen_size[1])
        dartpoint = (randomX, randomY)
        distance_from_center = math.hypot(center_point[0] - randomX, center_point[1] - randomY) #the distance formula
        is_in_circle = distance_from_center <= width/2 #screen width
       
        
        if is_in_circle:
            pygame.draw.circle(screen, "green", dartpoint, 10)
        else:
            pygame.draw.circle(screen, "red", dartpoint, 10)
        pygame.display.flip()
        pygame.time.wait(2000)
    
    # pygame.draw.circle(screen, "dark blue", dartpoint, 10)
    #     pygame.display.flip()
    #     pygame.time.wait(2000)
    pygame.time.wait(6000)

#   for throw in range(10):
#         randomX = random.randrange(0, screen_size[0])
#         randomY = random.randrange(0, screen_size[1])
#         dartpoint = (randomX, randomY)
#         pygame.draw.circle(screen, "dark blue", dartpoint, 10)
#         pygame.display.flip()
#         pygame.time.wait(2000)
    
   
#     pygame.time.wait(6000)
    break


