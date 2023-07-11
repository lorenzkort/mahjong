# Creates a dictionary of all Mahjong tiles
import json

suits = {
    'bamboo':[1,2,3,4,5,6,7,8,9],
    'caracters':[1,2,3,4,5,6,7,8,9],
    'circles':[1,2,3,4,5,6,7,8,9], 
    'dragon':['white', 'red', 'green'], 
    'wind':['south', 'east', 'north', 'west'],
}

def load_from_file(path:str) -> dict:
    with open(path) as f:
        tiles = json.load(f)
    return tiles

all_tiles = load_from_file('/Users/lorenzkort/Dropbox/2022/Code/mahjong/data/tiles.json')