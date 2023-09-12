#🌲🌊🚁🟩🔥🏬🧡🧯🏥☁️⚡🏆⬛ 


from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

from map import Map
from helicopter import Helicopter as Helico
from clouds import Clouds
import time
import os
import json

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
CLOUDS_UPDATA = 100
MAP_W,MAP_H = 20,10

field = Map(MAP_H,MAP_W)
clouds = Clouds(MAP_H,MAP_W)
helico = Helico(MAP_H,MAP_W)
tick = 1

MOVES = {'w':(-1,0), 'd':(0,1), 's':(1,0), 'a':(0,-1)}

def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower() 
    
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
   
    elif c == 'f':
        data = {'helicopter': helico.export_data(), 
                'clouds': clouds.export_data(), 
                'field': field.export_data(),
                'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
   
    elif c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.import_data(data['helicopter'])
            field.import_data(data['field'])
            clouds.import_data(data['clouds'])


listener = keyboard.Listener(
    on_press=None,
    on_release=process_key,)
listener.start()



while True:
    os.system("clear")
    field.process_helicopter(helico)
    helico.print_stats()
    field.print_map(helico)
    print ("TICK", tick)
    tick +=1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.denerate_free()
    if (tick % TREE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATA == 0):
        field.clouds.update()
    
