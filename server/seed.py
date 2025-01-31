from app import app, db  # Ensure your Flask app is imported properly
from models import Player  # Import your Player model

def seed_players():
    """Seed the database with initial top 30 players."""
    players = [
        {"name": "Player 1", "position": "Guard", "value": 0},
        {"name": "Player 2", "position": "Forward", "value": 0},
        # Add more players here
    ]

    for player_data in players:
        player = Player(name=player_data["name"], position=player_data["position"], value=player_data["value"])
        db.session.add(player)

    db.session.commit()
    print("Database seeded with initial players.")

if __name__ == '__main__':
    with app.app_context():
        seed_players()