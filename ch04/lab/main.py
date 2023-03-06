import random
import pygame
import math


pygame.init()
#Part B
screen = pygame.display.set_mode((800,800))
screen_size = pygame.display.get_window_size()
    
width = screen_size[0]
height = screen_size[1]
hit_box_width = width / 2
hit_box_height = height / 2

hitboxes = {
    "red": pygame.Rect(100, 600, hit_box_width, hit_box_height),
    "green": pygame.Rect(400, 600, hit_box_width, hit_box_height),
}

main_colors = {
 "red": (200, 0, 0),
 "green": (0, 200, 0),
}

pygame.display.flip()
pygame.time.wait(3000)
#Part A
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
    
    num_players = 2
    colors = ["green", "yellow"]
    wrong_colors = ["red", "purple"]
    
    player = 0
    results = [[], []]
    for throw in range(10 * num_players):
        ax, ay = random.randrange(0, screen_size[0]), random.randrange(0, screen_size[0])
        dartpoint = (ax, ay)
        distance_from_center = math.hypot(center_point[0] - ax, center_point[1] - ay) #the distance formula
        is_in_circle = distance_from_center <= width/2 #screen width
        # randomX1 = random.randrange(0, screen_size[0])
        # randomY1 = random.randrange(0, screen_size[1])
        # dartpoint1 = (randomX1, randomY1)
        # distance_from_center1 = math.hypot(center_point[0] - randomX1, center_point[1] - randomY1) #the distance formula
        # is_in_circle1 = distance_from_center1 <= width/2 #screen width

        # randomX2 = random.randrange(0, screen_size[0])
        # randomY2 = random.randrange(0, screen_size[1])
        # dartpoint2 = (randomX2, randomY2)
        # distance_from_center2 = math.hypot(center_point[0] - randomX2, center_point[1] - randomY2) #the distance formula
        # is_in_circle2 = distance_from_center2 <= width/2 #screen width
     
        if is_in_circle:
            pygame.draw.circle(screen, colors[player], dartpoint, 10)
        else:
            pygame.draw.circle(screen, wrong_colors[player], dartpoint, 10)

        results[player].append(is_in_circle)
        # print("Player", player, " hits: ", sum(results[player]))
        player = (player + 1) % num_players
 
        pygame.display.flip()
        pygame.time.wait(200)
        
        
    for i in range(num_players):
        print("Player", i + 1, " hits: ", sum(results[i]))
    # print("Player 2 hits: ", results[1])
    if sum(results[0]) > sum(results[1]):
        font = pygame.font.Font(None, 48)
        text = font.render("Player 1 wins!", True, "white")
        screen.blit(text, (300, 100))
    elif sum(results[0]) < sum(results[1]):
        font = pygame.font.Font(None, 48)
        text = font.render("Player 2 wins!", True, "white")
        screen.blit(text, (300, 100)) 
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("Tie!", True, "white")
        screen.blit(text, (300, 100))
    pygame.display.flip()
    pygame.time.wait(6000)
    break