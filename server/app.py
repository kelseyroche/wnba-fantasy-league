from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialize Flask app, database, and bcrypt
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wnba_fantasy_league.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Models
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    week_score = db.Column(db.Integer, default=0)
    season_score = db.Column(db.Integer, default=0)


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    value = db.Column(db.Float, nullable=False)
    player_week_points = db.Column(db.Integer, default=0)
    player_season_points = db.Column(db.Integer, default=0)


class RosterSpot(db.Model):
    __tablename__ = 'roster_spots'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)
    week_points = db.Column(db.Integer, default=0)


# Initialize the database
with app.app_context():
    db.create_all()


# Routes

# --- User Authentication Routes ---
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return jsonify({"error": "User with this username or email already exists"}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201


@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return jsonify({"message": "Login successful!", "user": {"id": user.id, "username": user.username}}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401


# --- Team Routes ---
@app.route('/teams/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = Team.query.get_or_404(team_id)
    return jsonify({
        "id": team.id,
        "user_id": team.user_id,
        "week_score": team.week_score,
        "season_score": team.season_score
    })


@app.route('/teams', methods=['POST'])
def create_team():
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    new_team = Team(user_id=user_id)
    db.session.add(new_team)
    db.session.commit()

    return jsonify({"message": "Team created successfully!", "team": {"id": new_team.id}}), 201


# --- Player Routes ---
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    players_list = [{
        "id": player.id,
        "name": player.name,
        "position": player.position,
        "value": player.value,
        "player_week_points": player.player_week_points,
        "player_season_points": player.player_season_points
    } for player in players]

    return jsonify(players_list)


# --- Roster Routes ---
@app.route('/roster/<int:team_id>', methods=['GET'])
def get_roster(team_id):
    roster = RosterSpot.query.filter_by(team_id=team_id).all()
    roster_list = [{
        "id": spot.id,
        "player_id": spot.player_id,
        "date_added": spot.date_added,
        "week_points": spot.week_points
    } for spot in roster]

    return jsonify(roster_list)


@app.route('/roster', methods=['POST'])
def add_player_to_roster():
    data = request.json
    team_id = data.get('team_id')
    player_id = data.get('player_id')

    if not team_id or not player_id:
        return jsonify({"error": "Team ID and Player ID are required"}), 400

    new_roster_spot = RosterSpot(team_id=team_id, player_id=player_id, date_added=db.func.now())
    db.session.add(new_roster_spot)
    db.session.commit()

    return jsonify({"message": "Player added to roster!"}), 201


# --- Main Entry Point ---
if __name__ == '__main__':
    app.run(debug=True)