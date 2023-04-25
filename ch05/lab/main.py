import pygame

# Part A
def threenp1(n):
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count


def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2, upper_limit + 1):
        value = threenp1(i)
        objs_in_sequence[i] = value
    return objs_in_sequence


# Part B
def graph_coordinates(threenp1_iters_dict):
    coordinates = list(threenp1_iters_dict.items())
    print(coordinates)
    window = pygame.display.set_mode((640, 480))
    window.fill("white")
    pygame.draw.lines(window, "black", True, points=coordinates)
    new_display = pygame.transform.flip(window, False, True)
    window.blit(new_display, (0, 0))
    
    # Scale the display
    width, height = new_display.get_size()
    factor = 5
    new_display = pygame.transform.scale(new_display, (width * factor, height * factor))

# Blit the scaled image onto the window
    window.blit(new_display, (width * factor, height * factor))

        # Find the maximum iterations value
    max_so_far = max(threenp1_iters_dict.values())

    # Create a font object to display the message
    font = pygame.font.Font(None, 24)
    msg = font.render(f"Max iterations so far: {max_so_far}", True, "black")

    # Scale the display and add the message
    width, height = new_display.get_size()
    factor = 5
    new_display = pygame.transform.scale(new_display, (width * factor, height * factor))
    window.blit(new_display, (width * factor, height * factor))
    window.blit(msg, (10, 10))
    
    pygame.display.flip()

def main():
    dictionary = threenp1range(100)
    print(dictionary)
    graph_coordinates(dictionary)

pygame.init()

while 1:
    pygame.event.pump()
    main()
    pygame.time.wait(5000)
    break