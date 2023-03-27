class Rectangle:
    """
    A class representing a rectangle with parameters x, y, h, w. 
    """
    def __init__(self, x, y, h, w):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)

    def __str__(self):
        """
        Returns the Rectangle dimensions.
        """
        return f"x: {self.x}, y: {self.y}, height: {self.height}, width: {self.width} "

 