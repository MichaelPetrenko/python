from utils import randcell, randbool, randcell2

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп

CELL_TYPES = "⬜🌲🌊🏥🏦"

class Map:
    width = 0
    height = 0
    cells = [[]]

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = [[0 for i in range(self.width)] for j in range(self.height)]

    def generate_river(self, l):
        rc = randcell(self.width, self.height)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1


    def generate_forest(self, r, mxr): # 3, 10 = 30%
        for ri in range(self.height):
            for ci in range(self.width):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def check_bounds(self, x, y):
        if (x < 0) or (y < 0) or (x >= self.height) or (y >= self.width):
            return False
        else:
            return True

    def print_map(self):
        print("⬛" * (self.width + 2))
        for row in self.cells:
            print("⬛", end='')
            for cell in row:
                if (cell >= 0) and (cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end='')
            print("⬛")
        print("⬛" * (self.width + 2))

map = Map(20, 10)
map.generate_forest(3, 10)
map.generate_river(10)
map.generate_river(10)
map.generate_river(10)
map.print_map()