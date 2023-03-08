import pygame

pygame.init()

screen = pygame.display.set_mode()
#screen: variable
#pygame: module/library we are using
#display: submodule of podgame
#set_mode: function of the display submodule

screen.fill("red")
pygame.display.flip
pygame.time.wait(1000)
screen.fill("blue")
pygame.display.flip
pygame.time.wait(1000)
screen.fill("green")
pygame.display.flip
pygame.time.wait(1000)

screen_size = screen.get_size()


#[x, y, width, height]
dimensions = [100, 100, 250, 250]

pygame.draw.rect(screen, "red", [100, 100, 250, 250])
pygame.display.flip
pygame.time.wait(1000)