from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialize SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Hash the password before saving it to the database
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Check the hashed password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    username = db.Column(db.String, nullable=False)
    week_score = db.Column(db.Integer, default=0)
    season_score = db.Column(db.Integer, default=0)
    user = db.relationship("User", back_populates="team")
    roster_spots = db.relationship("RosterSpot", back_populates="team")

class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    player_week_points = db.Column(db.Integer, default=0)
    player_season_points = db.Column(db.Integer, default=0)

class RosterSpot(db.Model):
    __tablename__ = "roster_spots"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    date_added = db.Column(db.DateTime, nullable=False)
    week_points = db.Column(db.Integer, default=0)
    team = db.relationship("Team", back_populates="roster_spots")
    player = db.relationship("Player")