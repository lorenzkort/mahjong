import random
from tiles import all_tiles



class Game():

    def __init__(self, seed=987, east=False) -> None:
        # random.seed(seed)
        self.east = east
        self.tile_amt = 14 if east else 13
        self.hand = random.sample(all_tiles, self.tile_amt)
        self.player2 = random.sample(
            [x for x in all_tiles if x not in self.hand]
            , 13 if east else 14)
        self.player3 = random.sample(
            [x for x in all_tiles if x not in self.hand + self.player2]
            , 13)
        self.player4 = random.sample(
            [x for x in all_tiles if x not in self.hand + self.player2 + self.player3]
            , 13)
        self.wall = [x for x in all_tiles if x not in self.hand and x not in self.hand + self.player2 + self.player3 + self.player4]
        self.out = []

    def show_hand(self):
        self.hand.sort(key=lambda x: x["suit"])
        for tile in self.hand:
            print(tile["name"])

    def show_stats(self):
        print(
            f"""
------------- STATS -------------
Tiles in wall    : {len(self.wall)}
Tiles in my hand : {len(self.hand)}
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


