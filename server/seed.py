# from app import app, db
# from models import Player, User

# def seed_players():
#     """Seed the database with initial top 30 players."""
    # players = [
    #     {"name": "Player 1", "position": "Guard", "value": 8, "season_points": 100},
    #     {"name": "Player 2", "position": "Forward", "value": 7, "season_points": 90},
    #     {"name": "Player 3", "position": "Center", "value": 9, "season_points": 110},
    #     {"name": "Player 4", "position": "Guard", "value": 6, "season_points": 85},
    #     {"name": "Player 5", "position": "Forward", "value": 5, "season_points": 75},
    #     {"name": "Player 6", "position": "Center", "value": 10, "season_points": 120},
    #     {"name": "Player 7", "position": "Guard", "value": 4, "season_points": 65},
    #     {"name": "Player 8", "position": "Forward", "value": 3, "season_points": 60},
    #     {"name": "Player 9", "position": "Center", "value": 8, "season_points": 95},
    #     {"name": "Player 10", "position": "Guard", "value": 7, "season_points": 90},
    #     {"name": "Player 11", "position": "Forward", "value": 6, "season_points": 80},
    #     {"name": "Player 12", "position": "Center", "value": 5, "season_points": 70},
    #     {"name": "Player 13", "position": "Guard", "value": 9, "season_points": 110},
    #     {"name": "Player 14", "position": "Forward", "value": 8, "season_points": 100},
    #     {"name": "Player 15", "position": "Center", "value": 7, "season_points": 90},
    #     {"name": "Player 16", "position": "Guard", "value": 10, "season_points": 120},
    #     {"name": "Player 17", "position": "Forward", "value": 4, "season_points": 65},
    #     {"name": "Player 18", "position": "Center", "value": 3, "season_points": 55},
    #     {"name": "Player 19", "position": "Guard", "value": 2, "season_points": 50},
    #     {"name": "Player 20", "position": "Forward", "value": 6, "season_points": 85},
    #     {"name": "Player 21", "position": "Center", "value": 5, "season_points": 75},
    #     {"name": "Player 22", "position": "Guard", "value": 4, "season_points": 60},
    #     {"name": "Player 23", "position": "Forward", "value": 3, "season_points": 55},
    #     {"name": "Player 24", "position": "Center", "value": 9, "season_points": 105},
    #     {"name": "Player 25", "position": "Guard", "value": 8, "season_points": 95},
    #     {"name": "Player 26", "position": "Forward", "value": 7, "season_points": 85},
    #     {"name": "Player 27", "position": "Center", "value": 10, "season_points": 125},
    #     {"name": "Player 28", "position": "Guard", "value": 2, "season_points": 45},
    #     {"name": "Player 29", "position": "Forward", "value": 1, "season_points": 40},
    #     {"name": "Player 30", "position": "Center", "value": 5, "season_points": 70},
    # ]

#     for player_data in players:
#         player = Player(
#             name=player_data["name"],
#             position=player_data["position"],
#             value=player_data["value"],
#             season_points=player_data["season_points"]
#         )
#         db.session.add(player)

#     db.session.commit()
#     print("Database seeded with initial players.")


# def seed_users():
#     """Seed the database with initial users."""
#     users = [
#         {"username": "user1", "email": "user1@example.com", "password": "password1"},
#         {"username": "user2", "email": "user2@example.com", "password": "password2"},
#         # Add more users here
#     ]

#     for user_data in users:
#         user = User(username=user_data["username"], email=user_data["email"])
#         user.set_password(user_data["password"])  # Use the method to hash the password
#         db.session.add(user)

#     db.session.commit()
#     print("Database seeded with initial users.")


# if __name__ == '__main__':
#     with app.app_context():
#         seed_players()
#         seed_users()

from app import app, db
from models import Player, User, Team, RosterSpot

def clear_database():
    """Clear existing data from the database."""
    db.session.query(RosterSpot).delete()
    db.session.query(Team).delete()
    db.session.query(User).delete()
    db.session.query(Player).delete()
    db.session.commit()
    print("Database cleared.")

def seed_players():
    """Seed the database with initial top 30 players."""
    players = [
        {"name": "Player 1", "position": "Guard", "value": 8, "season_points": 100},
        {"name": "Player 2", "position": "Forward", "value": 7, "season_points": 90},
        {"name": "Player 3", "position": "Center", "value": 9, "season_points": 110},
        {"name": "Player 4", "position": "Guard", "value": 6, "season_points": 85},
        {"name": "Player 5", "position": "Forward", "value": 5, "season_points": 75},
        {"name": "Player 6", "position": "Center", "value": 10, "season_points": 120},
        {"name": "Player 7", "position": "Guard", "value": 4, "season_points": 65},
        {"name": "Player 8", "position": "Forward", "value": 3, "season_points": 60},
        {"name": "Player 9", "position": "Center", "value": 8, "season_points": 95},
        {"name": "Player 10", "position": "Guard", "value": 7, "season_points": 90},
        {"name": "Player 11", "position": "Forward", "value": 6, "season_points": 80},
        {"name": "Player 12", "position": "Center", "value": 5, "season_points": 70},
        {"name": "Player 13", "position": "Guard", "value": 9, "season_points": 110},
        {"name": "Player 14", "position": "Forward", "value": 8, "season_points": 100},
        {"name": "Player 15", "position": "Center", "value": 7, "season_points": 90},
        {"name": "Player 16", "position": "Guard", "value": 10, "season_points": 120},
        {"name": "Player 17", "position": "Forward", "value": 4, "season_points": 65},
        {"name": "Player 18", "position": "Center", "value": 3, "season_points": 55},
        {"name": "Player 19", "position": "Guard", "value": 2, "season_points": 50},
        {"name": "Player 20", "position": "Forward", "value": 6, "season_points": 85},
        {"name": "Player 21", "position": "Center", "value": 5, "season_points": 75},
        {"name": "Player 22", "position": "Guard", "value": 4, "season_points": 60},
        {"name": "Player 23", "position": "Forward", "value": 3, "season_points": 55},
        {"name": "Player 24", "position": "Center", "value": 9, "season_points": 105},
        {"name": "Player 25", "position": "Guard", "value": 8, "season_points": 95},
        {"name": "Player 26", "position": "Forward", "value": 7, "season_points": 85},
        {"name": "Player 27", "position": "Center", "value": 10, "season_points": 125},
        {"name": "Player 28", "position": "Guard", "value": 2, "season_points": 45},
        {"name": "Player 29", "position": "Forward", "value": 1, "season_points": 40},
        {"name": "Player 30", "position": "Center", "value": 5, "season_points": 70},
    ]

    for player_data in players:
        player = Player(
            name=player_data["name"],
            position=player_data["position"],
            value=player_data["value"],
            season_points=player_data["season_points"]
        )
        db.session.add(player)

    db.session.commit()
    print("Database seeded with initial players.")

def seed_users_and_teams():
    """Seed the database with initial users and their teams."""
    users = [
        {"username": "user1", "email": "user1@example.com", "password": "password1"},
        {"username": "user2", "email": "user2@example.com", "password": "password2"},
        {"username": "kelsey", "email": "kelsey@email.com", "password": "kelsey"},
        # Add more users here
    ]

    players = Player.query.all()

    for user_data in users:
        user = User(username=user_data["username"], email=user_data["email"])
        user.set_password(user_data["password"])
        db.session.add(user)
        db.session.flush()

        team = Team(user_id=user.id)
        db.session.add(team)
        db.session.flush()

        selected_players = players[:5]
        for player in selected_players:
            roster_spot = RosterSpot(team_id=team.id, player_id=player.id, season_points=player.season_points)
            db.session.add(roster_spot)

        team.calculate_season_score()

    db.session.commit()
    print("Database seeded with initial users and teams with players.")

if __name__ == '__main__':
    with app.app_context():
        clear_database()  # Clear existing data before seeding
        seed_players()
        seed_users_and_teams()