from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import event


# Initialize SQLAlchemy and Bcrypt
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
        return f"<User {self.email}>"

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    week_score = db.Column(db.Integer, default=0)
    season_score = db.Column(db.Integer, default=0)

    user = db.relationship("User", back_populates="team")
    roster_spots = db.relationship("RosterSpot", back_populates="team", cascade="all, delete-orphan")

    def update_season_score(self):
        """Recalculate the season score based on rostered players' points."""
        self.season_score = sum(rs.week_points for rs in self.roster_spots)
        db.session.commit()


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    value = db.Column(db.Integer, nullable=False)

    # Explicitly define columns for week 1 to week 44 points
    week_1_points = db.Column(db.Integer, default=0)
    week_2_points = db.Column(db.Integer, default=0)
    week_3_points = db.Column(db.Integer, default=0)
    week_4_points = db.Column(db.Integer, default=0)
    week_5_points = db.Column(db.Integer, default=0)
    week_6_points = db.Column(db.Integer, default=0)
    week_7_points = db.Column(db.Integer, default=0)
    week_8_points = db.Column(db.Integer, default=0)
    week_9_points = db.Column(db.Integer, default=0)
    week_10_points = db.Column(db.Integer, default=0)
    week_11_points = db.Column(db.Integer, default=0)
    week_12_points = db.Column(db.Integer, default=0)
    week_13_points = db.Column(db.Integer, default=0)
    week_14_points = db.Column(db.Integer, default=0)
    week_15_points = db.Column(db.Integer, default=0)
    week_16_points = db.Column(db.Integer, default=0)
    week_17_points = db.Column(db.Integer, default=0)
    week_18_points = db.Column(db.Integer, default=0)
    week_19_points = db.Column(db.Integer, default=0)
    week_20_points = db.Column(db.Integer, default=0)
    week_21_points = db.Column(db.Integer, default=0)
    week_22_points = db.Column(db.Integer, default=0)
    week_23_points = db.Column(db.Integer, default=0)
    week_24_points = db.Column(db.Integer, default=0)
    week_25_points = db.Column(db.Integer, default=0)
    week_26_points = db.Column(db.Integer, default=0)
    week_27_points = db.Column(db.Integer, default=0)
    week_28_points = db.Column(db.Integer, default=0)
    week_29_points = db.Column(db.Integer, default=0)
    week_30_points = db.Column(db.Integer, default=0)
    week_31_points = db.Column(db.Integer, default=0)
    week_32_points = db.Column(db.Integer, default=0)
    week_33_points = db.Column(db.Integer, default=0)
    week_34_points = db.Column(db.Integer, default=0)
    week_35_points = db.Column(db.Integer, default=0)
    week_36_points = db.Column(db.Integer, default=0)
    week_37_points = db.Column(db.Integer, default=0)
    week_38_points = db.Column(db.Integer, default=0)
    week_39_points = db.Column(db.Integer, default=0)
    week_40_points = db.Column(db.Integer, default=0)
    week_41_points = db.Column(db.Integer, default=0)
    week_42_points = db.Column(db.Integer, default=0)
    week_43_points = db.Column(db.Integer, default=0)
    week_44_points = db.Column(db.Integer, default=0)

    @property
    def player_season_points(self):
        """Calculates season total by summing all weekly points."""
        return sum(getattr(self, f"week_{i}_points", 0) for i in range(1, 45))

    def __repr__(self):
        return f"<Player {self.name}>"

class RosterSpot(db.Model):
    __tablename__ = "roster_spots"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    week = db.Column(db.Integer, nullable=False)
    week_points = db.Column(db.Integer, default=0)

    team = db.relationship("Team", back_populates="roster_spots")
    player = db.relationship("Player")

    def set_week_points(self):
        """Sets `week_points` based on the player's corresponding weekly score."""
        if self.player:
            self.week_points = getattr(self.player, f"week_{self.week}_points", 0)

    def __repr__(self):
        return f"<RosterSpot Team {self.team_id}, Player {self.player_id}, Week {self.week}>"

# Listen for changes to the Player table and update RosterSpot
@event.listens_for(Player, "after_update", propagate=True)
def update_roster_spots(mapper, connection, target):
    """Automatically updates `week_points` for RosterSpot when Player stats change."""
    for roster_spot in RosterSpot.query.filter_by(player_id=target.id).all():
        roster_spot.week_points = getattr(target, f"week_{roster_spot.week}_points", 0)
    db.session.commit()

@event.listens_for(RosterSpot, "after_update")
def update_team_scores(mapper, connection, target):
    """Automatically updates `season_score` for Team when RosterSpot scores change."""
    team = Team.query.get(target.team_id)
    if team:
        team.update_season_score()