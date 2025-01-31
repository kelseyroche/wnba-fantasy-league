from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, bcrypt, User, Team, Player, RosterSpot

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app, supports_credentials=True)

# Database & session configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wnba_fantasy_league.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_COOKIE_NAME"] = "wnba_fantasy_session"
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)

# Helper to get current user
def get_current_user():
    user_id = session.get("user_id")
    return User.query.get(user_id) if user_id else None

# View user's team
@app.route('/my_team', methods=['GET'])
def view_my_team():
    """View the current user's team and their season score."""
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    team = user.team
    if not team:
        return jsonify({"error": "No team found for this user"}), 404

    # Update the season score
    team.calculate_season_score()

    roster = [
        {
            "player_id": rs.player.id,
            "player_name": rs.player.name,
            "position": rs.player.position,
            "season_points": rs.player.season_points
        }
        for rs in team.roster_spots
    ]

    return jsonify({"team": roster, "season_score": team.season_score}), 200

# Submit and lock roster
@app.route('/submit_roster', methods=['POST'])
def submit_roster():
    """Submit and lock the user's roster for the season."""
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    team = user.team
    if not team:
        return jsonify({"error": "No team found for this user"}), 404

    if team.locked:
        return jsonify({"error": "Roster is already locked and cannot be changed"}), 400

    data = request.json
    player_ids = data.get('player_ids')

    # Clear existing roster spots (if any)
    db.session.query(RosterSpot).filter_by(team_id=team.id).delete()

    # Add new players to the roster
    for player_id in player_ids:
        player = Player.query.get(player_id)
        if player:
            new_spot = RosterSpot(team_id=team.id, player_id=player_id)
            db.session.add(new_spot)

    # Lock the team
    team.locked = True
    db.session.commit()

    return jsonify({"message": "Roster submitted and locked successfully!"}), 200

# Run app
if __name__ == '__main__':
    app.run(debug=True)