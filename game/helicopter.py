from utils import randcell
import os

class Helicopter:

    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.h = h
        self.w = w
        self.y = ry

        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 20


    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if nx >= 0 and ny >= 0 and nx < self.h and ny < self.w:
            self.x, self.y = nx, ny

    def print_stats(self):
        print("🪣  ", self.tank, "/", self.mxtank, sep='', end=' | ')
        print("🏆 ", self.score, end=' | ')
        print("💛 ", self.lives)

    def game_over(self):
        os.system("cls")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("                                      ")
        print("GAME OVER, YOUR SCORE IS", self.score)
        print("                                      ")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit(0)