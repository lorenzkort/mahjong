# Used to create the game tiles and manage transactions within the game

import random
from application import tiles

class Game():

    def __init__(self, seed=None, east=True) -> None:
        if not seed:
            random.seed(seed)
        self.east = east
        self.tile_amt = 14 if east else 13
        self.player1 = random.sample(tiles.all_tiles, self.tile_amt)
        self.player1_out = []
        self.player2 = random.sample(
            [x for x in tiles.all_tiles if x not in self.player1]
            , 13 if east else 14)
        self.player2_out = []
        self.player3 = random.sample(
            [x for x in tiles.all_tiles if x not in self.player1 + self.player2]
            , 13)
        self.player3_out = []
        self.player4 = random.sample(
            [x for x in tiles.all_tiles if x not in self.player1 + self.player2 + self.player3]
            , 13)
        self.player4_out = []
        self.wall = [x for x in tiles.all_tiles if x not in self.player1 and x not in self.player1 + self.player2 + self.player3 + self.player4]
        self.out = self.player1_out + self.player2_out + self.player3_out + self.player4_out

    def show_hand(self, player_num:int):
        t = getattr(self, f'player{player_num}')
        t.sort(key=lambda x: str(x["type"]))
        t.sort(key=lambda x: x["suit"])
        return t

    def show_wall(self):
        self.wall.sort(key=lambda x: str(x["type"]))
        self.wall.sort(key=lambda x: x["suit"])
        return self.wall

    def show_stats(self):
        return(
            f"""
------------- STATS -------------
Tiles in wall    : {len(self.wall)}
Tiles in my hand : {len(self.player1)}
Tiles player 2   : {len(self.player2)}
Tiles player 3   : {len(self.player3)}
Tiles player 4   : {len(self.player4)}
---------------------------------
            """
        )
    
    # def play_round():
    #     pass

    # def exchange_flower():
    #     pass

    # def pung():
    #     pass

    # def chow():
    #     pass

    # def kong():
    #     pass

    # def mahjong():
    #     pass