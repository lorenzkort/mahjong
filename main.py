import random

from game import Game
from hands import Hands
from odds import Odds

game = Game()

# game.show_hand()
# game.show_stats()

odds = Odds(hand=game.hand)

hands = Hands(game.hand)
chows = hands.generate_all_chows()
pungs = hands.generat_all_pungs()

random_chow = random.sample(chows, 1)[0]
random_pung = random.sample(pungs, 1)[0]

print(
    len(chows),
    len(pungs)
)