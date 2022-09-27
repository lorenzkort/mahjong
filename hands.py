from tiles import create_all

class Hands():

    def __init__(self, current_hand) -> None:
        self.current_hand = current_hand

    def get_missing_tiles(self):
        self.current_hand
        # get current hand
        # identify possible pungs
        # identify possible chows
        # identify the missing tiles
        pass

    def generate_discard_scores(self):
        # order tiles by how often they DO NOT occur in the top x% of possible Mahjongs
        # calculate likeliness to get the tiles
        # form concept mahjong
        # identify all redundant tiles
        pass

    # def generate_all_chows(self) -> list:
    #     chows = []
    #     for suit in ['bamboo', 'cirlces', 'numbers']:
    #         for n in range(2,9):
    #             chow = []
    #             for t in [n - 1, n, n + 1]:
    #                 chow.append({
    #                     "suit":suit,
    #                     "type":t
    #                 })
    #             chows.append(chow)
    #     return chows

    # def generat_all_pungs(self):
    #     pungs = []
    #     cleaned_tiles = []
    #     for item in create_all(unique=True):
    #         if item['suit'] != 'flowers':
    #             cleaned_tiles.append(
    #                 {
    #                     "suit":item["suit"],
    #                     "type":item["type"]
    #                 }
    #             )
    #     for tile in cleaned_tiles:
    #         pung = [tile for n in range(3)]
    #         pungs.append(pung)
    #     return pungs

    def id_pungs_from_hand(self)

    def vanilla_mahjongs(self) -> list:
        

        return # list of all possible mahjongs