#Part A
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
    for i in range(2, upper_limit + 1, 1):
        value = threenp1(i)
        objs_in_sequence[i] = value
    return objs_in_sequence


def main():
    upper_limit = int(input("Enter a value greater than or equal to 2: "))
    print(threenp1range(upper_limit))

main()

#Part B
def graph_coordinates(threenp1_iters_dict):
    pygame.init()
    window = pygame.display.set_mode()
    window.fill("white")
    new_display = pygame.transform.flip(window, False, True)
    width, height = new_display.get_size()
    factor = 2
    new_display = pygame.transform.scale(new_display, (width * factor, height * factor))
    window.blit(new_display, (0, 0))
    max_so_far = 0