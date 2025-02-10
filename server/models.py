from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    team = db.relationship("Team", back_populates="user", uselist=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    season_score = db.Column(db.Integer, default=0)
    locked = db.Column(db.Boolean, default=False)

    user = db.relationship("User", back_populates="team")
    roster_spots = db.relationship("RosterSpot", back_populates="team", cascade="all, delete-orphan")

    def calculate_season_score(self):
        """Calculate the total season score based on player's season points."""
        self.season_score = sum(rs.season_points for rs in self.roster_spots)
        db.session.commit()

# class Team(db.Model):
#     __tablename__ = "teams"

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)  # Allow nullable user_id
#     season_score = db.Column(db.Integer, default=0)
#     locked = db.Column(db.Boolean, default=False)

#     user = db.relationship("User", back_populates="team")
#     roster_spots = db.relationship("RosterSpot", back_populates="team", cascade="all, delete-orphan")

#     def calculate_season_score(self):
#         """Calculate the total season score based on player's season points."""
#         self.season_score = sum(rs.season_points for rs in self.roster_spots)
#         db.session.commit()


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    value = db.Column(db.Integer, nullable=False)

    season_points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Player {self.name}>"


class RosterSpot(db.Model):
    __tablename__ = "roster_spots"

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    season_points = db.Column(db.Integer, default=0)

    player = db.relationship("Player")
    team = db.relationship("Team", back_populates="roster_spots")

    def update_season_points(self):
        """Update the season points for this roster spot based on the associated player's points."""
        self.season_points = self.player.season_points