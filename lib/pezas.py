import logging
logger = logging.getLogger(__name__)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        try:
            return Vector(self.x*other, self.y*other)
        except:
            print(f"{other} should be a scalar.")
    def __rmul__(self, other):
        return self.__mul__(other)
MOVS = {
    "Recto" : [Vector(1, 0), Vector(-1, 0), Vector(0, 1), Vector(0, -1)],
    "Vertical" : [Vector(1, 1), Vector(-1, 1), Vector(-1, -1), Vector(1, -1)],
    "Peon" : [Vector(1, 0)],
    "Cabalo" : [],
}

class Peza:
    def __init__(self, id, color, movimientos, range_1, initial_position, special = None, representation = None):
        self.id = id #Peza: cabalo, rei ...
        self.color = color #blanco ou negro
        self.movimientos = [] #movimientos que pode facer a peza.
        for key in movimientos:
            self.movimientos = self.movimientos + MOVS.get(key)
        self.range = range
        self.position = initial_position
        self.special = special #Enroque ...
        self.representation = representation

class Rei(Peza):
    def __init__(self, color, position):
        super().__init__("Rei", color, ("Recto"), True, position, None, 'K')

class Reina(Peza):
    def __init__(self, color, position):
        super().__init__("Reina", color, ("Recto", "Vertical"), False, position, None, 'Q')

class Torre(Peza):
    def __init__(self, color, position):
        super().__init__("Torre", color, ("Recto"), False, position, None, 'T')

class Alfil(Peza):
    def __init__(self, color, position):
        super().__init__("Alfil", color, ("Vertical"), False, position, None, 'S')

class Cabalo(Peza):
    def __init__(self, color, position):
        super().__init__("Cabalo", color, ("Cabalo"), False, position, None, 'C')

class Peon(Peza):
    def __init__(self, color, position):
        super().__init__("Peon", color, "Peon", True, position, None, 'p')

if __name__ == '__main__':
    a = Reina("blanco", Vector(3,4))
    for i in a.movimientos:
        print(i)