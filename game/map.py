# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп
# 5 - пожар

from utils import randcell, randbool, randcell2

CELL_TYPES = "🟩🌲🌊🏥🏦🔥"
TREE_BONUS = 100
UPGRADE_COST = 500

class Map:

    width = 0
    height = 0
    cells = [[]]


    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = [[0 for i in range(self.width)] for j in range(self.height)]

        self.generate_forest(3, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()


    def check_bounds(self, x, y):
        if (x < 0) or (y < 0) or (x >= self.height) or (y >= self.width):
            return False
        else:
            return True


    def print_map(self, helico):
        print("⬛" * (self.width + 2))
        for ri in range(self.height):
            print("⬛", end='')
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if helico.x == ri and helico.y == ci:
                    print('🚁', end='')
                elif (cell >= 0) and (cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end='')
            print("⬛")
        print("⬛" * (self.width + 2))


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


    def generate_tree(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1


    def generate_upgrade_shop(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4


    def add_fire(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5


    def update_fires(self):
        for ri in range(self.height):
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0

        for i in range(5):
            self.add_fire()


    def process_helicopter(self, helico):
        c = self.cells[helico.x][helico.y]
        if c == 2:
            helico.tank = helico.mxtank
        elif c == 5 and helico.tank > 0:
            helico.score += TREE_BONUS
            helico.tank -= 1
            self.cells[helico.x][helico.y] = 1
        elif c == 4 and helico.score >= UPGRADE_COST:
            helico.score -= UPGRADE_COST
            helico.mxtank += 1