# 🌲 🌊 🚁 🟩 🔥 🏥 💛 🪣 🏦 ☁️ ⚡️ 🏆

from pynput import keyboard
from map import Map
import time
import os
import json
from helicopter import Helicopter as Helico
from clouds import Clouds


TICK_SLEEP = 0.1
TREE_UPDATE = 50
FIRE_UPDATE = 75
CLOUDS_UPDATE = 100
MAP_WIDTH = 20
MAP_HEIGHT = 10

map = Map(MAP_WIDTH, MAP_HEIGHT)
clouds = Clouds(MAP_WIDTH, MAP_HEIGHT)
helico = Helico(MAP_WIDTH, MAP_HEIGHT)
tick = 1

MOVES = {
    'w': (-1, 0), 'up': (-1, 0),
    'd': (0, 1), 'right': (0, 1),
    's': (1, 0), 'down': (1, 0),
    'a': (0, -1), 'left': (0, -1)
    }

# f - save, g - load
def process_key(key, injected):
    global helico, tick, clouds, map

    try:
        if hasattr(key, 'name'):
            c = key.name
        else:
            c = key.char.lower()
    except Exception:
        return

    if c in MOVES.keys():
        dx = MOVES[c][0]
        dy = MOVES[c][1]
        helico.move(dx, dy)

    elif c == 'f':
        data = {
            "helicopter": helico.export_data(),
            "clouds": clouds.export_data(),
            "map": map.export_data(),
            "tick": tick
        }
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)

    elif c == 'g':
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            tick = data["tick"] or 1
            helico.import_data(data["helicopter"])
            map.import_data(data["map"])
            clouds.import_data(data["clouds"])

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

while True:
    os.system("cls")
    map.process_helicopter(helico, clouds)
    helico.print_stats()
    map.print_map(helico, clouds)
    print("TICK", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        map.generate_tree()
    if tick % FIRE_UPDATE == 0:
        map.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()