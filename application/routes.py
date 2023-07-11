from flask import Flask, render_template, request
from application import app, models
from application.forms import GameStart

@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def home():
    game = models.Game(seed=7)
    checksum = game.checksum()
    player1_hand = game.show_hand(1)
    p1_outs = game.show_outs(1)
    player2_hand = game.show_hand(2)
    p2_outs = game.show_outs(2)
    player3_hand = game.show_hand(3)
    p3_outs = game.show_outs(3)
    player4_hand = game.show_hand(4)
    p4_outs = game.show_outs(4)
    wall = game.show_wall()
    form = GameStart()
    if request.method == 'GET':
        if request.form.get('submit') == 'Exchange flowers':
            game.exchange_flowers()
            return render_template(
                'home.html',
                game=game,
                checksum=checksum,
                player1_hand = player1_hand,
                player2_hand = player2_hand,
                player3_hand = player3_hand,
                player4_hand = player4_hand,
                p1_outs = p1_outs,
                p2_outs = p2_outs,
                p3_outs = p3_outs,
                p4_outs = p4_outs,
                wall = wall,
                form=form
                )
    return render_template(
                'home.html',
                game=game,
                checksum=checksum,
                player1_hand = player1_hand,
                player2_hand = player2_hand,
                player3_hand = player3_hand,
                player4_hand = player4_hand,
                p1_outs = p1_outs,
                p2_outs = p2_outs,
                p3_outs = p3_outs,
                p4_outs = p4_outs,
                wall = wall,
                form=form
                )
