class Peza:
    def __init__(self, tipo, color, movimientos, x, y, special = None):
        self.tipo = tipo #Peza: cabalo, rei ...
        self.color = color #blanco ou negro
        self.movimientos = movimientos #movimientos que pode facer a peza [1,1]. [0,1] ...
        self.x = x
        self.y = y
        self.special = None
        self.moves = self.movimientos.split(",")
        for i, value in enumerate(self.moves):
            self.moves[i] = [int(value[:2]), int(value[2:])]
        print(self.moves)

    def move_or_eat(self, new_x, new_y):
        pass
