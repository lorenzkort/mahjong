from application import app, models
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    game = models.Game()
    stats = game.show_stats
    player1_hand = game.show_hand(1)
    player2_hand = game.show_hand(2)
    player3_hand = game.show_hand(3)
    player4_hand = game.show_hand(4)
    wall = game.show_wall()
    return render_template(
        'home.html',
        stat=stats,
        player1_hand=player1_hand,
        player2_hand=player2_hand,
        player3_hand=player3_hand,
        player4_hand=player4_hand,
        wall=wall
        )

