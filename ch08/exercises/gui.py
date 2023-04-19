class tube:
    def __init__(self, pos, tubecolor):
        self.green = tubecolor
        self.xy = pos
        self.transportable = False #Player can travel through tube
        
class block: 
    def __init__(self, height, ismystery, canbreak):
        self.xy = height
        self.ismystery = False
        self.canbreak = True

class enemy:
    def __init__(self, health, hitbox, size)
        self.h = health
        self.hbox = hitbox
        self.s = size