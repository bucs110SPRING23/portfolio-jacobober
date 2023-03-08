stars = int(input("Enter how many rows you want: "))
def star_pyramid(stars):
    for i in range(1, stars + 1):
        print("*" * i)
star_pyramid(stars)
    
def rstar_pyramid(stars):
    for i in range(stars, 0, -1):
        print("*" * i)
rstar_pyramid(stars)