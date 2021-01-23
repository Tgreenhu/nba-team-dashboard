# Import Dependencies
import os
import pandas as pd
from flask import Flask, jsonify, render_template, request, redirect
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Create Engine & Start Session
engine = create_engine("postgresql://postgres:Georgia-07@localhost:5432/nba_comp")
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)

# Create our flask app
app = Flask(__name__)

# Route 1
@app.route("/")
def home():
    return render_template("index.html")

# Route 2
@app.route("/data")
def playerNames():
    player_data = {}
    nba_players = engine.execute('''Select * from nba''')
    all_names = []
    for x in nba_players:
        player = {}
        player["name"] = x.name
        player["age"] = x.age
        player["team"] = x.team
        player["minutes"] = x.minutes
        player["turnover"] = x.turnover
        player["usg"] = x.usg
        player["vorp"] = x.vorp
        all_names.append(player)
    player_data["players"] = all_names
    return jsonify(player_data)

# Route 3
# @app.route("/chart")
# def pie():
#     pie_labels = players.name
#     pie_values = players.minutes
#     return render_template('...', title = 'Player Minutes', )

# Close our session
session.close()

# Run app
if __name__ == "__main__":
    app.run()