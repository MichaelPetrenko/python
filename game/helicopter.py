from utils import randcell

class Helicopter:
    x = 0
    y = 0

    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.h = h
        self.w = w
        self.y = ry


    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if nx >= 0 and ny >= 0 and nx < self.h and ny < self.w:
            self.x, self.y = nx, ny
