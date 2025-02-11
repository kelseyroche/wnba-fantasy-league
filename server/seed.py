# from app import app, db
# from models import Player, User, Team, RosterSpot
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# def clear_database():
#     """Clear existing data from the database."""
#     db.session.query(RosterSpot).delete()
#     db.session.query(Team).delete()
#     db.session.query(User).delete()
#     db.session.query(Player).delete()
#     db.session.commit()
#     print("Database cleared.")

# def seed_players():
#     """Seed the database with actual WNBA player names."""
#     players = [
#         {"name": "A'ja Wilson", "position": "Forward", "value": 10, "season_points": 120},
#         {"name": "Breanna Stewart", "position": "Forward", "value": 10, "season_points": 115},
#         {"name": "Brittney Griner", "position": "Center", "value": 9, "season_points": 110},
#         {"name": "Diana Taurasi", "position": "Guard", "value": 9, "season_points": 105},
#         {"name": "Candace Parker", "position": "Forward", "value": 9, "season_points": 100},
#         {"name": "Arike Ogunbowale", "position": "Guard", "value": 8, "season_points": 95},
#         {"name": "Nneka Ogwumike", "position": "Forward", "value": 8, "season_points": 90},
#         {"name": "Elena Delle Donne", "position": "Forward", "value": 8, "season_points": 88},
#         {"name": "Sue Bird", "position": "Guard", "value": 7, "season_points": 85},
#         {"name": "Sylvia Fowles", "position": "Center", "value": 8, "season_points": 83},
#         {"name": "Chelsea Gray", "position": "Guard", "value": 7, "season_points": 80},
#         {"name": "Skylar Diggins-Smith", "position": "Guard", "value": 7, "season_points": 78},
#         {"name": "Jonquel Jones", "position": "Center", "value": 9, "season_points": 95},
#         {"name": "Courtney Vandersloot", "position": "Guard", "value": 7, "season_points": 77},
#         {"name": "Liz Cambage", "position": "Center", "value": 8, "season_points": 85},
#         {"name": "Jackie Young", "position": "Guard", "value": 6, "season_points": 70},
#         {"name": "Allie Quigley", "position": "Guard", "value": 6, "season_points": 68},
#         {"name": "Kelsey Plum", "position": "Guard", "value": 7, "season_points": 75},
#         {"name": "Natasha Howard", "position": "Forward", "value": 6, "season_points": 72},
#         {"name": "Jewell Loyd", "position": "Guard", "value": 7, "season_points": 73},
#         {"name": "Tina Charles", "position": "Center", "value": 8, "season_points": 90},
#         {"name": "Kayla McBride", "position": "Guard", "value": 6, "season_points": 67},
#         {"name": "DeWanna Bonner", "position": "Forward", "value": 8, "season_points": 86},
#         {"name": "Alyssa Thomas", "position": "Forward", "value": 7, "season_points": 79},
#         {"name": "Emma Meesseman", "position": "Forward", "value": 7, "season_points": 76},
#         {"name": "Kristi Toliver", "position": "Guard", "value": 6, "season_points": 65},
#         {"name": "Myisha Hines-Allen", "position": "Forward", "value": 6, "season_points": 64},
#         {"name": "Kia Nurse", "position": "Guard", "value": 5, "season_points": 60},
#         {"name": "Brianna Turner", "position": "Forward", "value": 5, "season_points": 58},
#         {"name": "Riquna Williams", "position": "Guard", "value": 5, "season_points": 55},
#     ]

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
#         {"username": f"user{i+1}", "email": f"user{i+1}@example.com", "password": "password"}
#         for i in range(20)  # Create 20 users
#     ]

#     for user_data in users:
#         user = User(username=user_data["username"], email=user_data["email"])
#         user.set_password(user_data["password"])
#         db.session.add(user)

#     db.session.commit()
#     print("Database seeded with initial users.")

# def seed_teams():
#     """Seed the database with empty teams linked to users."""
#     users = User.query.all()

#     for user in users:
#         team = Team(user_id=user.id)
#         db.session.add(team)

#     db.session.commit()
#     print("Database seeded with teams for each user.")

# if __name__ == '__main__':
#     with app.app_context():
#         clear_database()
#         seed_players()
#         seed_users()
#         seed_teams()

#############################################################################

# from app import app, db
# from models import Player, User, Team, RosterSpot
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# def clear_database():
#     """Clear existing data from the database."""
#     db.session.query(RosterSpot).delete()
#     db.session.query(Team).delete()
#     db.session.query(User).delete()
#     db.session.query(Player).delete()
#     db.session.commit()
#     print("Database cleared.")

# def seed_players():
#     """Seed the database with initial top 30 players."""
#     players = [
#         {"name": "A'ja Wilson", "position": "Forward", "value": 10, "season_points": 120},
#         {"name": "Breanna Stewart", "position": "Forward", "value": 10, "season_points": 115},
#         {"name": "Brittney Griner", "position": "Center", "value": 9, "season_points": 110},
#         {"name": "Diana Taurasi", "position": "Guard", "value": 9, "season_points": 105},
#         {"name": "Candace Parker", "position": "Forward", "value": 9, "season_points": 100},
#         {"name": "Arike Ogunbowale", "position": "Guard", "value": 8, "season_points": 95},
#         {"name": "Nneka Ogwumike", "position": "Forward", "value": 8, "season_points": 90},
#         {"name": "Elena Delle Donne", "position": "Forward", "value": 8, "season_points": 88},
#         {"name": "Sue Bird", "position": "Guard", "value": 7, "season_points": 85},
#         {"name": "Sylvia Fowles", "position": "Center", "value": 8, "season_points": 83},
#         {"name": "Chelsea Gray", "position": "Guard", "value": 7, "season_points": 80},
#         {"name": "Skylar Diggins-Smith", "position": "Guard", "value": 7, "season_points": 78},
#         {"name": "Jonquel Jones", "position": "Center", "value": 9, "season_points": 95},
#         {"name": "Courtney Vandersloot", "position": "Guard", "value": 7, "season_points": 77},
#         {"name": "Liz Cambage", "position": "Center", "value": 8, "season_points": 85},
#         {"name": "Jackie Young", "position": "Guard", "value": 6, "season_points": 70},
#         {"name": "Allie Quigley", "position": "Guard", "value": 6, "season_points": 68},
#         {"name": "Kelsey Plum", "position": "Guard", "value": 7, "season_points": 75},
#         {"name": "Natasha Howard", "position": "Forward", "value": 6, "season_points": 72},
#         {"name": "Jewell Loyd", "position": "Guard", "value": 7, "season_points": 73},
#         {"name": "Tina Charles", "position": "Center", "value": 8, "season_points": 90},
#         {"name": "Kayla McBride", "position": "Guard", "value": 6, "season_points": 67},
#         {"name": "DeWanna Bonner", "position": "Forward", "value": 8, "season_points": 86},
#         {"name": "Alyssa Thomas", "position": "Forward", "value": 7, "season_points": 79},
#         {"name": "Emma Meesseman", "position": "Forward", "value": 7, "season_points": 76},
#         {"name": "Kristi Toliver", "position": "Guard", "value": 6, "season_points": 65},
#         {"name": "Myisha Hines-Allen", "position": "Forward", "value": 6, "season_points": 64},
#         {"name": "Kia Nurse", "position": "Guard", "value": 5, "season_points": 60},
#         {"name": "Brianna Turner", "position": "Forward", "value": 5, "season_points": 58},
#         {"name": "Riquna Williams", "position": "Guard", "value": 5, "season_points": 55},
#     ]

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
#         {"username": "user3", "email": "user3@example.com", "password": "password3"},
#     ]

#     for user_data in users:
#         user = User(username=user_data["username"], email=user_data["email"])
#         user.set_password(user_data["password"])
#         db.session.add(user)

#     db.session.commit()
#     print("Database seeded with initial users.")

# def seed_teams():
#     """Seed the database with 20 teams."""
#     users = User.query.all()
#     user_ids = [user.id for user in users]

#     # Create 20 teams
#     for i in range(20):
#         # Assign a user ID to the first few teams, and leave the rest with no user
#         user_id = user_ids[i] if i < len(user_ids) else None
#         team = Team(user_id=user_id if user_id else None)
#         db.session.add(team)

#     db.session.commit()
#     print("Database seeded with teams.")

# if __name__ == '__main__':
#     with app.app_context():
#         clear_database()
#         seed_players()
#         seed_users()
#         seed_teams()
from app import app, db
from models import Player, User, Team, RosterSpot
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def clear_database():
    """Clear existing data from the database."""
    db.session.query(RosterSpot).delete()
    db.session.query(Team).delete()
    db.session.query(User).delete()
    db.session.query(Player).delete()
    db.session.commit()
    print("Database cleared.")

def seed_players():
    """Seed the database with initial top players."""
    players = [
        {"name": "A'ja Wilson", "position": "Forward", "value": 10, "season_points": 120},
        {"name": "Breanna Stewart", "position": "Forward", "value": 10, "season_points": 115},
        {"name": "Brittney Griner", "position": "Center", "value": 9, "season_points": 110},
        {"name": "Diana Taurasi", "position": "Guard", "value": 9, "season_points": 105},
        {"name": "Candace Parker", "position": "Forward", "value": 9, "season_points": 100},
        {"name": "Arike Ogunbowale", "position": "Guard", "value": 8, "season_points": 95},
        {"name": "Nneka Ogwumike", "position": "Forward", "value": 8, "season_points": 90},
        {"name": "Elena Delle Donne", "position": "Forward", "value": 8, "season_points": 88},
        {"name": "Sue Bird", "position": "Guard", "value": 7, "season_points": 85},
        {"name": "Sylvia Fowles", "position": "Center", "value": 8, "season_points": 83},
        {"name": "Chelsea Gray", "position": "Guard", "value": 7, "season_points": 80},
        {"name": "Skylar Diggins-Smith", "position": "Guard", "value": 7, "season_points": 78},
        {"name": "Jonquel Jones", "position": "Center", "value": 9, "season_points": 95},
        {"name": "Courtney Vandersloot", "position": "Guard", "value": 7, "season_points": 77},
        {"name": "Liz Cambage", "position": "Center", "value": 8, "season_points": 85},
        {"name": "Jackie Young", "position": "Guard", "value": 6, "season_points": 70},
        {"name": "Allie Quigley", "position": "Guard", "value": 6, "season_points": 68},
        {"name": "Kelsey Plum", "position": "Guard", "value": 7, "season_points": 75},
        {"name": "Natasha Howard", "position": "Forward", "value": 6, "season_points": 72},
        {"name": "Jewell Loyd", "position": "Guard", "value": 7, "season_points": 73},
        {"name": "Tina Charles", "position": "Center", "value": 8, "season_points": 90},
        {"name": "Kayla McBride", "position": "Guard", "value": 6, "season_points": 67},
        {"name": "DeWanna Bonner", "position": "Forward", "value": 8, "season_points": 86},
        {"name": "Alyssa Thomas", "position": "Forward", "value": 7, "season_points": 79},
        {"name": "Emma Meesseman", "position": "Forward", "value": 7, "season_points": 76},
        {"name": "Kristi Toliver", "position": "Guard", "value": 6, "season_points": 65},
        {"name": "Myisha Hines-Allen", "position": "Forward", "value": 6, "season_points": 64},
        {"name": "Kia Nurse", "position": "Guard", "value": 5, "season_points": 60},
        {"name": "Brianna Turner", "position": "Forward", "value": 5, "season_points": 58},
        {"name": "Riquna Williams", "position": "Guard", "value": 5, "season_points": 55},
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
    """Seed the database with initial users and their corresponding teams."""
    users = [
        {"username": "user1", "email": "user1@example.com", "password": "password1"},
        {"username": "user2", "email": "user2@example.com", "password": "password2"},
        {"username": "user3", "email": "user3@example.com", "password": "password3"},
        # Add more users if needed
    ]

    for user_data in users:
        # Create a new user
        user = User(username=user_data["username"], email=user_data["email"])
        user.set_password(user_data["password"])
        db.session.add(user)
        db.session.flush()  # Flush to get the user ID

        # Create a team with the same ID as the user
        team = Team(user_id=user.id)
        db.session.add(team)

    db.session.commit()
    print("Database seeded with initial users and teams.")

def seed_additional_teams(user_count):
    """Seed additional teams to reach a total of 20 teams."""
    for i in range(user_count, 20):
        # Create additional users to match the team count
        user = User(username=f"user{i+1}", email=f"user{i+1}@example.com")
        user.set_password("password")
        db.session.add(user)
        db.session.flush()

        # Create a team for each new user
        team = Team(user_id=user.id)
        db.session.add(team)

    db.session.commit()
    print("Additional teams seeded to reach a total of 20.")

if __name__ == '__main__':
    with app.app_context():
        clear_database()
        seed_players()
        seed_users_and_teams()
        seed_additional_teams(3)  # Starts adding teams after the initial 3 users