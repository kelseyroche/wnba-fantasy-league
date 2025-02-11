from flask import Flask, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, bcrypt, User, Team, Player, RosterSpot
import logging

load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})  # Allow all origins for testing

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wnba_fantasy_league.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_COOKIE_NAME"] = "wnba_fantasy_session"
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set to DEBUG level for detailed logs


db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)

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
# @app.route('/register', methods=['POST'])
# def register_user():
#     """Register a new user and create a team for them."""
#     data = request.json
#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')

#     if not username or not email or not password:
#         return jsonify({"error": "All fields are required"}), 400

#     existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
#     if existing_user:
#         return jsonify({"error": "User with this username or email already exists"}), 400

#     try:
#         # Create a new user
#         new_user = User(username=username, email=email)
#         new_user.set_password(password)
#         db.session.add(new_user)
#         db.session.flush()  # Flush to get the new user's ID

#         # Create a new team for the user
#         new_team = Team(user_id=new_user.id)
#         db.session.add(new_team)

#         db.session.commit()
#         app.logger.info(f"User {new_user.username} and their team created successfully.")

#         session["user_id"] = new_user.id
#         return jsonify({"message": "User registered successfully!", "user_id": new_user.id}), 201
#     except Exception as e:
#         db.session.rollback()
#         app.logger.error("Error creating user and team: %s", e)
#         return jsonify({"error": "Database error", "details": str(e)}), 500

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user and create a team for them."""
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
        # Create a new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.flush()  # Flush to get the new user's ID
        logging.debug(f"User created: {new_user}")

        # Create a new team for the user
        new_team = Team(user_id=new_user.id)
        db.session.add(new_team)
        logging.debug(f"Team created for user {new_user.id}")

        # Commit the transaction
        db.session.commit()
        logging.info(f"User {new_user.username} and their team committed to the database.")

        session["user_id"] = new_user.id
        return jsonify({"message": "User registered successfully!", "user_id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        logging.error("Error creating user and team: %s", e)
        return jsonify({"error": "Database error", "details": str(e)}), 500

# Login route
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

# Check session
@app.route('/check_session', methods=['GET'])
def check_session():
    """Check if a user is logged in and return their details."""
    user = get_current_user()
    if not user:
        return jsonify({"error": "Not logged in"}), 401

    return jsonify({"user": {"id": user.id, "username": user.username, "email": user.email}}), 200

# Edit profile
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
    
#Delete Account
@app.route('/delete_account', methods=['DELETE'])
def delete_account():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        # Delete user's team and associated roster spots
        if user.team:
            RosterSpot.query.filter_by(team_id=user.team.id).delete()
            db.session.delete(user.team)

        # Delete the user
        db.session.delete(user)
        db.session.commit()

        session.clear()  # Clear session after deletion
        return jsonify({"message": "Account deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        app.logger.error("Error deleting account: %s", e)
        return jsonify({"error": "An error occurred while deleting the account", "details": str(e)}), 500

# List players
@app.route('/players', methods=['GET'])
def get_players():
    """Retrieve all players from the database."""
    players = Player.query.all()
    players_data = [
        {
            "id": player.id,
            "name": player.name,
            "position": player.position,
            "value": player.value,  # Ensure this is included and correct
            "season_points": player.season_points
        }
        for player in players
    ]
    app.logger.debug(f"Players data: {players_data}")  # Log the players data
    return jsonify(players_data), 200

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
       user = get_current_user()
       if not user:
           return jsonify({"error": "Unauthorized"}), 401

       team = Team.query.filter_by(user_id=user.id).first()
       if not team:
           return jsonify({"error": "No team found for this user"}), 404

       if team.locked:
           return jsonify({"error": "Roster is already locked and cannot be changed"}), 400

       data = request.json
       if not data or 'player_ids' not in data:
           return jsonify({"error": "Invalid request format"}), 400

       app.logger.info(f"Received player IDs: {data.get('player_ids')}")  # Log received data

       player_ids = data.get('player_ids', [])
       if len(player_ids) != 5:
           return jsonify({"error": "You must submit exactly 5 players"}), 400

       total_value = 0
       for player_id in player_ids:
           player = Player.query.get(player_id)
           if not player:
               return jsonify({"error": f"Player with ID {player_id} not found"}), 404
           total_value += player.value

       if total_value > 40:  # Check if the total value exceeds the limit
           return jsonify({"error": "Total value of selected players exceeds the limit"}), 400

       try:
           RosterSpot.query.filter_by(team_id=team.id).delete()
           for player_id in player_ids:
               new_spot = RosterSpot(team_id=team.id, player_id=player_id)
               db.session.add(new_spot)

           team.locked = True
           db.session.commit()

           return jsonify({"message": "Roster submitted and locked successfully!"}), 200
       except Exception as e:
           db.session.rollback()
           app.logger.error("Error submitting roster: %s", e)
           return jsonify({"error": "An error occurred while submitting the roster", "details": str(e)}), 500
       
# leaderboard route


# @app.route('/leaderboard', methods=['GET'])
# def get_leaderboard():
#     """Fetch all users and calculate their team's scores directly from roster spots."""
#     users = User.query.all()
#     leaderboard_data = []

#     for user in users:
#         if user.team:
#             # Calculate the season score by summing the season points of all roster spots
#             season_score = sum(rs.season_points for rs in user.team.roster_spots)
#             leaderboard_data.append({
#                 "username": user.username,
#                 "season_score": season_score
#             })
#         else:
#             leaderboard_data.append({
#                 "username": user.username,
#                 "season_score": 0
#             })

#     return jsonify(leaderboard_data), 200

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Fetch all users and calculate their team's scores directly from roster spots."""
    users = User.query.all()
    leaderboard_data = []

    for user in users:
        if user.team:
            # Calculate the season score by summing the season points of all roster spots
            season_score = sum(rs.player.season_points for rs in user.team.roster_spots)
            leaderboard_data.append({
                "username": user.username,
                "season_score": season_score
            })
        else:
            leaderboard_data.append({
                "username": user.username,
                "season_score": 0
            })

    return jsonify(leaderboard_data), 200

##ADMIN

@app.route('/admin/update_player_score', methods=['POST'])
def update_player_score():
    """Admin route to manually update player scores."""
    try:
        data = request.json
        player_id = data.get('player_id')
        new_season_points = data.get('season_points')

        app.logger.debug(f"Player ID: {player_id}, New Season Points: {new_season_points}")

        player = Player.query.get(player_id)
        if not player:
            app.logger.error(f"Player with ID {player_id} not found")
            return jsonify({"error": "Player not found"}), 404

        player.season_points = new_season_points
        db.session.commit()

        # Recalculate team scores affected by this change
        teams = Team.query.join(RosterSpot).filter(RosterSpot.player_id == player.id).all()
        for team in teams:
            team.calculate_season_score()

        return jsonify({"message": f"Player {player.name}'s score updated successfully!"}), 200

    except Exception as e:
        app.logger.error(f"Error updating player score: {e}")
        return jsonify({"error": "An internal error occurred", "details": str(e)}), 500


@app.route('/team_roster', methods=['GET'])
def get_team_roster():
    user = get_current_user()
    if not user:
        app.logger.debug("Unauthorized access attempt.")
        return jsonify({"error": "Unauthorized"}), 401

    team = user.team
    if not team:
        app.logger.debug(f"No team found for user ID {user.id}")
        return jsonify({"error": "No team found for this user"}), 404

    roster_spots = RosterSpot.query.filter_by(team_id=team.id).all()
    if not roster_spots:
        app.logger.debug(f"No roster spots found for team ID {team.id}")
        return jsonify({"error": "No roster spots found for this team"}), 404

    roster_data = [
        {
            "player_id": rs.player.id,
            "player_name": rs.player.name,
            "position": rs.player.position,
            "season_points": rs.player.season_points,
            "value": rs.player.value
        }
        for rs in roster_spots
    ]

    return jsonify({"roster": roster_data}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5555)  