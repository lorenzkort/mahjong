# Tools to calculate the odds in a game

from game import Game

class Odds():

    def __init__(self, hand) -> None:
        self.hand = hand
        self.odds = []

    def odds_on_tile_per_round(self, set_type, target_tiles_left, total_tiles_left=122):
        if set_type == 'pung':
            discards = 3 # discards can be more or less if people pung in between
            odds_per_discard = target_tiles_left / total_tiles_left
            odds = odds_per_discard * discards
        if set_type == 'chow':
            discards = 1
            odds_per_discard = target_tiles_left / total_tiles_left
            odds = odds_per_discard * discards
        return odds