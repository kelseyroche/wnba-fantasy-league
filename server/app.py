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
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")
app.config["SESSION_COOKIE_NAME"] = "wnba_fantasy_session"

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
load_dotenv()

# API Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

def fetch_wnba_data(endpoint, params={}):
    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }
    try:
        url = f"https://{RAPIDAPI_HOST}/{endpoint}"
        print(f"Requesting URL: {url} with headers: {headers} and params: {params}")
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("API Request Exception:", str(e))
        return {"error": f"Failed to fetch data: {str(e)}"}

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

    session["user_id"] = new_user.id
    return jsonify({"message": "User registered successfully!", "user": {"id": new_user.id, "username": new_user.username}}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email, password = data.get('email'), data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        session["user_id"] = user.id
        return jsonify({"message": "Login successful!", "user": {"id": user.id, "username": user.username}}), 200

    return jsonify({"error": "Invalid email or password"}), 401

@app.route('/logout', methods=['POST'])
def logout_user():
    session.clear()
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
@app.route("/api/wnba_teams", methods=['GET'])
def list_all_teams():
    response = fetch_wnba_data("api/wnba_teams")
    return jsonify(response)

@app.route("/api/wnba_games_id", methods=['GET'])
def list_games():
    game_date = request.args.get('game_date')
    team_name = request.args.get('team_name')
    params = {}
    if game_date:
        params['game_date'] = game_date
    if team_name:
        params['team_name'] = team_name
    response = fetch_wnba_data("api/wnba_games_id", params)
    return jsonify(response)

@app.route("/api/wnba_team_data", methods=['GET'])
def get_team_data():
    game_id = request.args.get('game_id')
    params = {}
    if game_id:
        params['game_id'] = game_id
    response = fetch_wnba_data("api/wnba_team_data", params)
    return jsonify(response)

@app.route("/api/wnba_player_data", methods=['GET'])
def get_player_data():
    player_name = request.args.get('player_name')
    if not player_name:
        return jsonify({"error": "player_name is required"}), 400
    params = {'player_name': player_name}
    response = fetch_wnba_data("api/wnba_player_data", params)
    return jsonify(response)

@app.route("/api/wnba_players_by_team", methods=['GET'])
def get_players_by_team():
    team_name = request.args.get('team_name')
    if not team_name:
        return jsonify({"error": "team_name is required"}), 400
    params = {'team_name': team_name}
    response = fetch_wnba_data("api/wnba_players_by_team", params)
    return jsonify(response)

@app.route("/api/wnba_team_stats", methods=['GET'])
def get_team_stats():
    team_name = request.args.get('team_name')
    if not team_name:
        return jsonify({"error": "team_name is required"}), 400
    params = {'team_name': team_name}
    response = fetch_wnba_data("api/wnba_team_stats", params)
    return jsonify(response)

@app.route("/api/wnba_player_avg_stats", methods=['GET'])
def get_player_avg_stats():
    player_name = request.args.get('player_name')
    if not player_name:
        return jsonify({"error": "player_name is required"}), 400
    params = {'player_name': player_name}
    response = fetch_wnba_data("api/wnba_player_avg_stats", params)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)