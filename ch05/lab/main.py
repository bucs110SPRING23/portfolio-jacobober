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