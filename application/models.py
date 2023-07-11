# Used to create the game tiles and manage transactions within the game

import time
import random
import itertools
from application import tiles

class Game():

    def __init__(self, seed=None, starts_east=1) -> None:
        if not seed:
            random.seed(seed)
        self.starts_east = starts_east
        self.east = self.starts_east
        p1_hand = random.sample(tiles.all_tiles, 14 if self.east == 1 else 13)
        self.player1 = {
            "hand": p1_hand,
            "out": []
        }
        p2_hand = random.sample([x for x in tiles.all_tiles if x not in self.player1['hand']], 14 if self.east == 2 else 13)
        self.player2 = {
            "hand": p2_hand,
            "out": []
        }
        p3_hand = random.sample([x for x in tiles.all_tiles if x not in self.player1['hand'] + self.player2['hand']], 14 if self.east == 3 else 13)
        self.player3 = {
            "hand": p3_hand,
            "out": []
        }
        p4_hand = random.sample([x for x in tiles.all_tiles if x not in self.player1['hand'] + self.player2['hand'] + self.player3['hand']], 14 if self.east == 4 else 13)
        self.player4 = {
            "hand": p4_hand,
            "out": []
        }
        self.wall = [x for x in tiles.all_tiles if x not in self.player1['hand'] and x not in self.player1['hand'] + self.player2['hand'] + self.player3['hand'] + self.player4['hand']]

        self.all_hands = [self.player1['hand'], self.player2['hand'], self.player3['hand'], self.player4['hand']]
        
        self.out = self.player1['out'] + self.player2['out'] + self.player3['out'] + self.player4['out']

        self.open = []

    def checksum(self):
        wall = len(self.wall)
        hands = len(list(itertools.chain.from_iterable(self.all_hands)))
        out = len(self.out)
        return wall + hands + out

    def show_hand(self, player_num:int):
        t = getattr(self, f'player{player_num}')['hand']
        t.sort(key=lambda x: str(x["type"]))
        t.sort(key=lambda x: x["suit"])
        return t

    def show_outs(self, player_num:int):
        return getattr(self, f'player{player_num}')['out']

    def show_wall(self):
        self.wall.sort(key=lambda x: str(x["type"]))
        self.wall.sort(key=lambda x: x["suit"])
        return self.wall

    def exchange_flowers(self,num=None):
        # if a player number is specified, exchange flowers only for that player
        # if a player number has not been specified, exchange flowers for all players
        for rep in range(8):
            for i in range(1,5) if not num else num:
                hand = getattr(self, f'player{i}')['hand']
                for tile in hand:
                    if tile['suit'] == 'flowers':
                        getattr(self, f'player{i}')['out'].append(tile)
                        getattr(self, f'player{i}')['hand'].remove(tile)
                        new_tile = random.sample(self.wall, 1)[0]
                        print(f'Player{i} exchanged {tile["name"]} for {new_tile["name"]}')
                        getattr(self, f'player{i}')['hand'].append(new_tile)
                        self.wall.remove(new_tile)
        return                    

    # def pung():
    #     pass

    # def chow():
    #     pass

    # def kong():
    #     pass

    # def mahjong():
    #     pass

    def next_player(self, player:int):
        return player + 1 if player != 4 else 1

    def play_turn(self, player:int):
        player = getattr(self, f'player{player}')
        
        # if player has less than 14 tiles, draw a tile from the wall
        if len(player['hand']) < 14:
            draw = random.choice(self.wall)
            player['hand'].append(draw)
            self.wall.remove(draw)
        
        # discards random tile
        discard = random.choice(player['hand'])
        self.open.append(discard)
        player['hand'].remove(discard)

        return discard

    def play(self, east_player=1):
        player = east_player
        while len(self.wall) > 16:
            print(
                player, 
                self.play_turn(player)
            )
            player = self.next_player(player)
            
            # if any player announces pung/chow/kong/mahjong, call function
                # function returns discarded tile and next player
            
            # if no event has occured, the next player in line plays
            time.sleep(10)

