import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Player
import logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wnba_fantasy_league.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def seed_players():
    with app.app_context():
        players_data = [
            {"name": "A'ja Wilson", "position": "Forward", "value": 10, "season_points": 120},
            {"name": "Breanna Stewart", "position": "Forward", "value": 10, "season_points": 115},
            {"name": "Brittney Griner", "position": "Center", "value": 9, "season_points": 110},
            {"name": "Diana Taurasi", "position": "Guard", "value": 9, "season_points": 105},
            {"name": "Candace Parker", "position": "Forward", "value": 9, "season_points": 100},
            {"name": "Arike Ogunbowale", "position": "Guard", "value": 8, "season_points": 95},
            {"name": "Nneka Ogwumike", "position": "Forward", "value": 8, "season_points": 90},
            {"name": "Elena Delle Donne", "position": "Forward", "value": 8, "season_points": 88},
            {"name": "Sue Bird", "position": "Guard", "value": 7, "season_points": 85},
            {"name": "Sylvia Fowles", "position": "Center", "value": 8, "season_points": 83},
            {"name": "Chelsea Gray", "position": "Guard", "value": 7, "season_points": 80},
            {"name": "Skylar Diggins-Smith", "position": "Guard", "value": 7, "season_points": 78},
            {"name": "Jonquel Jones", "position": "Center", "value": 9, "season_points": 95},
            {"name": "Courtney Vandersloot", "position": "Guard", "value": 7, "season_points": 77},
            {"name": "Liz Cambage", "position": "Center", "value": 8, "season_points": 85},
            {"name": "Jackie Young", "position": "Guard", "value": 6, "season_points": 70},
            {"name": "Allie Quigley", "position": "Guard", "value": 6, "season_points": 68},
            {"name": "Kelsey Plum", "position": "Guard", "value": 7, "season_points": 75},
            {"name": "Natasha Howard", "position": "Forward", "value": 6, "season_points": 72},
            {"name": "Jewell Loyd", "position": "Guard", "value": 7, "season_points": 73},
            {"name": "Tina Charles", "position": "Center", "value": 8, "season_points": 90},
            {"name": "Kayla McBride", "position": "Guard", "value": 6, "season_points": 67},
            {"name": "DeWanna Bonner", "position": "Forward", "value": 8, "season_points": 86},
            {"name": "Alyssa Thomas", "position": "Forward", "value": 7, "season_points": 79},
            {"name": "Emma Meesseman", "position": "Forward", "value": 7, "season_points": 76},
            {"name": "Kristi Toliver", "position": "Guard", "value": 6, "season_points": 65},
            {"name": "Myisha Hines-Allen", "position": "Forward", "value": 6, "season_points": 64},
            {"name": "Kia Nurse", "position": "Guard", "value": 5, "season_points": 60},
            {"name": "Brianna Turner", "position": "Forward", "value": 5, "season_points": 58},
            {"name": "Riquna Williams", "position": "Guard", "value": 5, "season_points": 55},
        ]

        for player_data in players_data:
            player = Player.query.filter_by(name=player_data["name"]).first()
            if player:
                player.position = player_data["position"]
                player.value = player_data["value"]
                player.season_points = player_data["season_points"]
                logging.debug(f"Updated Player {player.name} with new data.")
            else:
                new_player = Player(**player_data)
                db.session.add(new_player)
                logging.debug(f"Added new Player {new_player.name}.")

        db.session.commit()
        print("Player data seeded successfully.")

if __name__ == "__main__":
    seed_players()