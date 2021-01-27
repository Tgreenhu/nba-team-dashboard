# Import Dependencies
import os
import pandas as pd
from flask import Flask, jsonify, render_template, request, redirect
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from config import username, password

# Create Engine & Start Session
engine = create_engine(f"postgresql://{username}:{password}@localhost:5432/nba_comp")
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
    
    team_names = engine.execute('''Select team from nba group by team order by team''')
    all_team_lists = []
    team_names_dict = [list(t) for t in team_names]
    for team in team_names_dict:
        team_data = {}
        team_list = []
        order_by_teams = engine.execute('''Select * from nba order by team''')
        for row in order_by_teams:
            if (team[0] == row.team):
                player_dict = {}
                # player_dict[str(team)] = team
                player_dict["team"] = row.team
                player_dict["name"] = row.name
                player_dict["age"] = row.age
                player_dict["minutes"] = row.minutes
                player_dict["turnover"] = row.turnover
                player_dict["usg"] = row.usg
                player_dict["vorp"] = row.vorp
                team_list.append(player_dict)
        team_data[str(team[0])] = team_list
        all_team_lists.append(team_data)

    # return jsonify(player_data) 
    return jsonify([player_data, all_names, all_team_lists])

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