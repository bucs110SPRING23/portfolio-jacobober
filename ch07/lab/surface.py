from rectangle import Rectangle

class Surface: 
    """
    A class representing a surface with an image and a rectangular area on it.
    """
    def __init__(self, filename, x, y, h, w):
        self.rect = Rectangle(x, y, h, w)
        self.image = filename

    def getRect(self):
        """
        Returns the rectangle attribute in self.rect.
        """
        return self.rect