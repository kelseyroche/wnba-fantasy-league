from flask import Flask, request, jsonify, session, redirect, url_for
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

# Landing page
@app.route('/')
def landing_page():
    """Landing page showing login and register options."""
    if 'user_id' in session:
        return redirect(url_for('view_my_team'))
    return "Welcome to the WNBA Fantasy League! Please login or register."

# Registration route
@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return jsonify({"error": "User with this username or email already exists"}), 400

    try:
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        session["user_id"] = new_user.id
        return jsonify({"message": "User registered successfully!", "user_id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500

# Login route
# @app.route('/login', methods=['POST'])
# def login_user():
#     """Log in a user."""
#     data = request.json
#     email = data.get('email')
#     password = data.get('password')

#     if not email or not password:
#         return jsonify({"error": "Email and password are required"}), 400

#     user = User.query.filter_by(email=email).first()
#     if user and user.check_password(password):
#         session["user_id"] = user.id
#         return redirect(url_for('view_my_team'))

#     return jsonify({"error": "Invalid email or password"}), 401

@app.route('/login', methods=['POST'])
def login_user():
    """Log in a user."""
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        session["user_id"] = user.id
        return jsonify({"message": "Login successful", "user": {"id": user.id, "username": user.username, "email": user.email}}), 200

    return jsonify({"error": "Invalid email or password"}), 401

# Logout route
@app.route('/logout', methods=['POST'])
def logout_user():
    """Log out the current user."""
    session.clear()
    return redirect(url_for('landing_page'))
#check session
@app.route('/check_session', methods=['GET'])
def check_session():
    """Check if a user is logged in and return their details."""
    user = get_current_user()
    if not user:
        return jsonify({"error": "Not logged in"}), 401

    return jsonify({"user": {"id": user.id, "username": user.username, "email": user.email}}), 200

#edit profile
@app.route('/edit_profile', methods=['POST'])
def edit_profile():
    """Edit user profile, including password update."""
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    username = data.get('username')
    email = data.get('email')
    new_password = data.get('new_password')
    current_password = data.get('current_password')

    if not username or not email:
        return jsonify({"error": "All fields are required"}), 400

    if new_password and not user.check_password(current_password):
        return jsonify({"error": "Current password is incorrect"}), 400

    try:
        user.username = username
        user.email = email
        if new_password:
            user.set_password(new_password)
        db.session.commit()
        return jsonify({"message": "Profile updated successfully!", "user": {"username": user.username, "email": user.email}}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500

# list players
@app.route('/players', methods=['GET'])
def get_players():
    """Retrieve all players from the database."""
    players = Player.query.all()
    players_data = [
        {
            "id": player.id,
            "name": player.name,
            "position": player.position,
            "season_points": player.season_points
        }
        for player in players
    ]
    return jsonify(players_data), 200

# View user's team
@app.route('/my_team', methods=['GET'])
def view_my_team():
    """View the current user's team and their season score."""
    user = get_current_user()
    if not user:
        return redirect(url_for('landing_page'))

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

    # Check if the number of selected players exceeds the limit
    if len(player_ids) > 5:
        return jsonify({"error": "Cannot have more than 5 players on the roster"}), 400

    # Calculate the total value of the selected players
    total_value = sum(Player.query.get(player_id).value for player_id in player_ids)

    # Check against the value limit
    if total_value > 30:
        return jsonify({"error": "Total value of selected players exceeds the limit"}), 400

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

#leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Fetch all users and their team's scores."""
    users = User.query.all()
    leaderboard_data = [
        {
            "username": user.username,
            "season_score": user.team.season_score if user.team else 0
        }
        for user in users
    ]
    return jsonify(leaderboard_data), 200

# Admin route
@app.route('/admin/update_player_score', methods=['POST'])
def update_player_score():
    """Admin route to manually update player scores."""
    data = request.json
    player_id = data.get('player_id')
    new_season_points = data.get('season_points')

    player = Player.query.get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404

    player.season_points = new_season_points
    db.session.commit()

    # Optionally, recalculate scores for all teams containing this player
    teams = Team.query.join(RosterSpot).filter(RosterSpot.player_id == player.id).all()
    for team in teams:
        team.calculate_season_score()

    return jsonify({"message": f"Player {player.name}'s score updated successfully!"}), 200


# Run app
if __name__ == '__main__':
    app.run(debug=True)