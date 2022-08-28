from genericpath import isdir
from cassiopeia import Champions
from cassiopeia.core.staticdata.champion import Champion 
from typing import List
import numpy as np
import json
import os

spells = {}


def save():
    with open("data.json", "w") as fp:
        json.dump(spells, fp, indent= 4)

def local_load():
    for file in os.listdir('files'):
        print(file)
        spells[file] = np.load('files/' + file)
        print(spells[file])

def web_loading():
    champions:List[Champion] = Champions(region='EUW')
    for champion in champions:
        keys = ["Q", "W", "E", "R"]
        for spell in champion.spells:
            img = np.array(spell.image_info.image)
            name = champion.name + "---" + str(keys.index(spell.keyboard_key.value))
            if not name in spells:
                spells[name] = np.array([img])
            else:
                np.append(spells[name], img)

def save():
    for value, array in spells.items():
        np.save('files/' + value, array)

def load():
    if os.path.isdir('files'):
        print("Data already saved, /files folder existing")
        local_load()
    else:
        print("Retrieving data, might take a lot of time")
        web_loading()
        save()


def compare(image):
    img = np.zeros((64, 64, 3))
    for i in range(64):
        for j in range(64):
            img[i, j] = image[i, j][:3]
    return min(spells.keys(), key=lambda a : min([np.linalg.norm(img - c) for c in spells[a]]))

load()