from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
import requests
from dotenv import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, bcrypt, User, Team, Player, RosterSpot

# Initialize Flask app
app = Flask(__name__)
CORS(app, supports_credentials=True)  # Allow frontend to send cookies

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wnba_fantasy_league.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")  # Required for session security
app.config["SESSION_COOKIE_NAME"] = "wnba_fantasy_session"  # Custom session cookie name

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
load_dotenv()

# API Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")
print(f"Loaded RAPIDAPI_HOST: {RAPIDAPI_HOST}")
print(f"Loaded RAPIDAPI_KEY: {RAPIDAPI_KEY}")

def fetch_wnba_data(endpoint, params={}):
       headers = {
           "x-rapidapi-host": RAPIDAPI_HOST,
           "x-rapidapi-key": RAPIDAPI_KEY
       }
       try:
           response = requests.get(f"https://{RAPIDAPI_HOST}/{endpoint}", headers=headers, params=params)
           response.raise_for_status()  # Raises an HTTPError for bad responses
           return response.json()
       except requests.exceptions.RequestException as e:
           return {"error": str(e)}



# Home route
@app.route('/')
def home():
    return "Welcome to the WNBA Fantasy League!"



# --- User Authentication Routes ---
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username, email, password = data.get('username'), data.get('email'), data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "User with this username or email already exists"}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    session["user_id"] = new_user.id  # Log in the user automatically after registering
    return jsonify({"message": "User registered successfully!", "user": {"id": new_user.id, "username": new_user.username}}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email, password = data.get('email'), data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        session["user_id"] = user.id  # Store user ID in session
        return jsonify({"message": "Login successful!", "user": {"id": user.id, "username": user.username}}), 200

    return jsonify({"error": "Invalid email or password"}), 401

@app.route('/logout', methods=['POST'])
def logout_user():
    session.clear()  # Clears session to log user out
    return jsonify({"message": "Logout successful!"}), 200

@app.route('/check_session', methods=['GET'])
def check_session():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.get(user_id)
        if user:
            return jsonify({"id": user.id, "username": user.username}), 200
    return jsonify({"error": "Not logged in"}), 401

# --- Helper Function: Check if User is Logged In ---
def get_current_user():
    user_id = session.get("user_id")
    return User.query.get(user_id) if user_id else None

# --- Protected Routes ---
@app.route('/teams', methods=['POST'])
def create_team():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    new_team = Team(user_id=user.id)
    db.session.add(new_team)
    db.session.commit()
    return jsonify({"message": "Team created successfully!", "team": {"id": new_team.id}}), 201

@app.route('/roster', methods=['POST'])
def add_player_to_roster():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    team_id, player_id, week = data.get('team_id'), data.get('player_id'), data.get('week')

    team = Team.query.get(team_id)
    if not team or team.user_id != user.id:
        return jsonify({"error": "Unauthorized or invalid team"}), 403

    new_roster_spot = RosterSpot(team_id=team.id, player_id=player_id, week=week)
    new_roster_spot.set_week_points()
    db.session.add(new_roster_spot)
    db.session.commit()
    
    return jsonify({"message": "Player added to roster!"}), 201

# --- API Routes ---
@app.route("/wnba/games/<string:date>")
def get_games(date):
    return jsonify(fetch_wnba_data(date))

@app.route("/wnba/teams")
def get_teams():
    return jsonify(fetch_wnba_data("teams"))

@app.route("/wnba/players")
def get_players_from_api():
    return jsonify(fetch_wnba_data("players"))

@app.route('/update_scores', methods=['POST'])
def update_scores():
    teams = Team.query.all()
    for team in teams:
        team.update_season_score()
    return jsonify({"message": "Scores updated successfully!"}), 200

#testing other api route
@app.route('/api/wnba_games', methods=['GET'])
def list_wnba_games():
    game_date = request.args.get('game_date')
    team_name = request.args.get('team_name')
    # Assuming fetch_wnba_data is correctly set up to call your API
    response = fetch_wnba_data("api/wnba_games_id", {"game_date": game_date, "team_name": team_name})
    # return jsonify(response)
    return jsonify({"message": "Endpoint is working"})

@app.route('/api/wnba_team_data')
def get_team_data():
    game_id = request.args.get('game_id')
    return jsonify(fetch_wnba_data("wnba_team_data", {"game_id": game_id}))

##test route to check values of api
@app.route('/check_env')
def check_env():
    return jsonify({
        "RAPIDAPI_HOST": RAPIDAPI_HOST,
        "RAPIDAPI_KEY": RAPIDAPI_KEY
    })

if __name__ == "__main__":
    app.run(debug=True)