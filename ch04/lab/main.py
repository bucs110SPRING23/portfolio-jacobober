import random
import pygame
import math


pygame.init()
#Part B
screen = pygame.display.set_mode((800,800))
screen_size = pygame.display.get_window_size()
    
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
WHITE = (255, 255, 255)

player1_box = pygame.Rect(50, 50, 200, 200)
player2_box = pygame.Rect(550, 50, 200, 200)

# Draw boxes
pygame.draw.rect(screen, RED, player1_box)
pygame.draw.rect(screen, BLUE, player2_box)

# Display instructions
font = pygame.font.Font(None, 36)
text = font.render("Select the player you think will win!", True, WHITE)
screen.blit(text, (200, 300))

pygame.display.flip()

# Wait for user to select player
selected_player = None
while selected_player is None:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if player1_box.collidepoint(pos):
                selected_player = 1
            elif player2_box.collidepoint(pos):
                selected_player = 2




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
    pygame.draw.line(screen, "black", (center_point[0], center_point[1] - width/2), (center_point[0], center_point[1] + width/2), 5)
    pygame.draw.line(screen, "black", (center_point[0] - width/2, center_point[1]), (center_point[0] + width/2, center_point[1]), 5)
    
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
        text = font.render("Player Red wins!", True, "white")
        screen.blit(text, (300, 100))
    elif sum(results[0]) < sum(results[1]):
        font = pygame.font.Font(None, 48)
        text = font.render("Player Blue wins!", True, "white")
        screen.blit(text, (300, 100)) 
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("Tie!", True, "white")
        screen.blit(text, (300, 100))

    if selected_player == 1 and sum(results[0]) > sum(results[1]):
        text = font.render("You guessed correctly! Player Red wins!", True, WHITE)
        screen.blit(text, (150, 500))
    elif selected_player == 2 and sum(results[0]) < sum(results[1]):
        text = font.render("You guessed correctly! Player Blue wins!", True, WHITE)
        screen.blit(text, (150, 500))
    else:
        text = font.render("You guessed incorrectly.", True, WHITE)
        screen.blit(text, (250, 500))
    pygame.display.flip()
    pygame.time.wait(6000)
    break

