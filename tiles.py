# Creates a dictionary of all Mahjong tiles

import secrets

suits = {
    'bamboo':[1,2,3,4,5,6,7,8,9],
    'numbers':[1,2,3,4,5,6,7,8,9],
    'circles':[1,2,3,4,5,6,7,8,9], 
    'dragon':['white', 'red', 'green'], 
    'wind':['south', 'east', 'north', 'west'],
}

def create_all(unique=False):
    tiles = []
    for counter in range(4 if not unique else 1):
        for suit, types in suits.items():
            for type in types:
                tiles.append(
                        {
                            "suit":suit,
                            "type":type,
                            "name":f"{type} {suit}",
                            "id": secrets.token_urlsafe(8)
                        } 
                    )
    for r in range(1,9):
                tiles.append(
                        {
                            "suit":"flowers",
                            "type":r,
                            "name":f"flowers {r}",
                            "id": secrets.token_urlsafe(8)
                        }
                    )
    return tiles

all_tiles = create_all()