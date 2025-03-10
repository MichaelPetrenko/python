# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп

class Map:
    width = 0
    height = 0
    cells = [[]]

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = [[0 for i in range(self.width)] for j in range(self.height)]

    # def generate_rivers(self):

    # def generate_forest(self):

    def check_bounds(self, x, y):
        if (x < 0) or (y < 0) or (x >= self.height) or (y >= self.width):
            return False
        else:
            return True

    def print_map(self):
        print("◼️" * (self.width + 2))
        for row in self.cells:
            print("◼️", end='')
            for cell in row:
                if cell == 0:
                    print('◻️', end='')
                elif cell == 1:
                    print('🌲', end='')
                elif cell == 2:
                    print('🌊', end='')
                elif cell == 3:
                    print('🏥', end='')
                elif cell == 4:
                    print('🏦', end='')
            print("◼️")
        print("◼️" * (self.width + 2))