# 🌲 🌊 🚁 🟩 🔥 🏥 💛 🪣 🏦 ☁️ ⚡️ 🏆

from pynput import keyboard
from map import Map
import time
import os
from helicopter import Helicopter as Helico


TICK_SLEEP = 0.2
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_WIDTH = 20
MAP_HEIGHT = 10

map = Map(MAP_WIDTH, MAP_HEIGHT)
map.generate_forest(3, 10)
map.generate_river(10)
map.generate_river(10)
map.generate_river(10)


helico = Helico(MAP_WIDTH, MAP_HEIGHT)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
def process_key(key, injected):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx = MOVES[c][0]
        dy = MOVES[c][1]
        helico.move(dx, dy)

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

tick = 1
while True:
    os.system("cls")
    print("TICK", tick)
    map.print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        map.generate_tree()
    if tick % FIRE_UPDATE == 0:
        map.update_fires()